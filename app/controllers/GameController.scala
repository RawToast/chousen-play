package controllers

import domain.GameState
import play.api.libs.json.Json
import play.api.mvc.{Action, AnyContent, Controller}

import scala.concurrent.ExecutionContext.Implicits.global

class GameController extends Controller {

  def getGameState(id: Int): Action[AnyContent] = Action.async {
    GameState.fetch(id).map {
      case gameState: Some[GameState] => Ok(Json.toJson(gameState))
      case None => NotFound
    } recover {
      case error: Throwable => InternalServerError
    }
  }
}
