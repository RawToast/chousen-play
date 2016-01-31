package controllers

import java.io.InputStream

import org.scalatest.{Matchers, OptionValues, WordSpecLike}
import play.api.libs.json.Json
import play.api.mvc.Result
import play.api.test.FakeRequest
import play.api.test.Helpers._
import play.mvc.Http.Status.{NOT_FOUND, OK}

import scala.concurrent.Future
import scala.concurrent.duration._
import scala.language.postfixOps

class GameControllerSpec extends WordSpecLike with Matchers with OptionValues {

  implicit val defaultTimeout = 5 seconds

  val ValidGameId = 1
  val InvalidGameId = 5

  "The GameController" should {

    "return the game state when given a valid id" in {
      val result: Future[Result] = makeRequest(ValidGameId)

      status(result) shouldBe OK

      contentAsJson(result) shouldBe Json.parse(readResource("/responses/getStateSuccess.json"))
    }

    "return 404 Not Found when given an invalid id" in {
      val result = makeRequest(InvalidGameId)

      status(result) shouldBe NOT_FOUND
    }
  }


  def makeRequest(gameId: Int) = {
    GameController.getGameState(gameId).apply(FakeRequest())
  }

  def readResource(location: String): InputStream = getClass().getResourceAsStream(location)
}
