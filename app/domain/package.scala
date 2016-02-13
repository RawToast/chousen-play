import play.api.libs.json.Json

package object domain {
  implicit val characterFormat = Json.format[domain.Character]
  implicit val playerFormat = Json.format[domain.Player]
  implicit val gameStateFormat = Json.format[GameState]

}
