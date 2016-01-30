package controllers

import domain.GameState
import play.api.libs.json.Json
import play.api.mvc._

object GameController extends Controller {

  def getGameState(id: Int) = Action {
    val state = GameState.fetch(id)
    Ok(Json.toJson(state))
  }
}
