package app

import react.*
import react.dom.*
import logo.*
import ticker.*
import sentiment.*

class App : RComponent<RProps, RState>() {
    override fun RBuilder.render() {
        div("App-header") {
            logo()
            h2 {
                +"Welcome to React with Kotlin"
            }
        }
        p("App-intro") {
            +"To get started, edit "
            code { +"app/App.kt" }
            +" and save to reload."
        }
        p("App-ticker") {
            ticker()
        }
        p("App-sentiment") {
            sentiment()
        }
    }
}

fun RBuilder.app() = child(App::class) {}
