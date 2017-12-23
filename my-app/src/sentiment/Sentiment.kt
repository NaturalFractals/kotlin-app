package sentiment

import react.*;
import react.dom.*;
import kotlin.browser.*;

interface SentimentProps: RProps {
}

interface SentimentState: RState {
}

class Sentiment(props: SentimentProps) : RComponent<SentimentProps, SentimentState>(props){
    override fun SentimentState.init(props: SentimentProps) {
        
    }

    override fun componentWillUnmount() {

    }

    override fun componentDidMount() {

    }

    override fun RBuilder.render() {
        div("Test") {
            h2 {
                +"Test here for header."
            }
        }
    }
}

fun RBuilder.sentiment() = child(Sentiment::class) {
    
}