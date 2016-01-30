package domain

case class GameState(id: Int, players: List[Player]) {

}

object GameState {
  def fetch(id: Int): GameState = {
    val players = List(Player(1, "TestUser1"), Player(2, "TestUser2"))
    GameState(id, players)
  }
}
