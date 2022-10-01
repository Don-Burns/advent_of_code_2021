val scala3Version = "3.2.0"

lazy val root = project
  .in(file("."))
  .settings(
    name := "scala",
    version := "0.1.0-SNAPSHOT",
    scalaVersion := scala3Version,
    libraryDependencies += "org.scalameta" % "munit_3" % "1.0.0-M6" % Test
  )
