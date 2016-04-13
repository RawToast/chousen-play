package domain

import scala.concurrent.Future

case class GameState(id: Int, players: List[Player]) {

}

object GameState {

  val stateMap = Map(1 -> List(Player(1, "TestUser1", List(Character("Bob"))),
                               Player(2, "TestUser2", List(Character("Dole")))),
                     2 -> List(Player(3, "TestUser3", List(Character("Dave"))),
                               Player(4, "TestUser4", List(Character("Ed")))))

  def fetch(id: Int): Future[Option[GameState]] = {

    val gameState = stateMap.find(_._1 == id)
                            .map(game => GameState(game._1, game._2))
    Future.successful(gameState)
  }
}
