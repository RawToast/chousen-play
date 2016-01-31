package domain

import scala.concurrent.Future

case class GameState(id: Int, players: List[Player]) {

}

object GameState {

  val stateMap = Map(1 -> List(Player(1, "TestUser1"), Player(2, "TestUser2")),
                     2 -> List(Player(3, "TestUser3"), Player(4, "TestUser4")))

  def fetch(id: Int): Future[Option[GameState]] = {
    if (stateMap.contains(id)) {
      Future.successful(Some(GameState(id, stateMap(id))))
    } else {
      Future.successful(None)
    }
  }
}
