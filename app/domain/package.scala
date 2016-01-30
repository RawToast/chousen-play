import play.api.libs.json.Json

package object domain {

  implicit val playerFormat = Json.format[domain.Player]
  implicit val gameStateFormat = Json.format[GameState]

}
