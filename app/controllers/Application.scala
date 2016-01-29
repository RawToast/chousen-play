package controllers

import play.api.mvc._

object Application extends Controller {

  def index = Action {
    Ok(views.html.index(null))
  }

  def db = Action {
    val out = "Hello"
    Ok(out)
  }
}
