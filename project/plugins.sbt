resolvers += "Typesafe repository" at "http://repo.typesafe.com/typesafe/releases/"
resolvers += "SonaType" at "https://oss.sonatype.org/content/groups/public"
resolvers += Resolver.url(
  "hmrc",
  url("http://dl.bintray.com/hmrc/releases/"))(
  Resolver.ivyStylePatterns)


// The Play plugin
addSbtPlugin("com.typesafe.play" % "sbt-plugin" % "2.4.3")
