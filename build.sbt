name := """chousen-stub"""

version := "1.0-SNAPSHOT"

lazy val root = (project in file(".")).enablePlugins(PlayScala)

scalaVersion := "2.11.7"

libraryDependencies ++= Seq(
  cache,
  ws
)

libraryDependencies <+= scalaVersion("org.scala-lang" % "scala-compiler" % _ )

// Scala test
libraryDependencies += "org.scalactic" %% "scalactic" % "2.2.6"
libraryDependencies += "org.scalatest" %% "scalatest" % "2.2.6" % "test"

val excluded = "<empty>;public;resources;logs;target;router.Routes.*;controllers\\..*Reverse.*"

ScoverageSbtPlugin.ScoverageKeys.coverageMinimum := 70
ScoverageSbtPlugin.ScoverageKeys.coverageExcludedPackages := excluded
