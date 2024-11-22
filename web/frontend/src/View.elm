module View exposing (root)

import Browser
import Element exposing (Element)
import Types exposing (..)


root : Model -> Browser.Document Msg
root model =
    { title = "TEMPLATE"
    , body =
        case model of
            Loading _ ->
                [ Element.layout
                    []
                    viewLoadingMessage
                ]

            Loaded loadedModel ->
                [ Element.layoutWith
                    { options =
                        [ Element.focusStyle
                            { borderColor = Nothing
                            , backgroundColor = Nothing
                            , shadow = Nothing
                            }
                        ]
                    }
                    [ Element.width Element.fill
                    , Element.height Element.fill

                    -- , Element.inFront <| putModalsHere
                    ]
                  <|
                    view loadedModel
                ]
    }


viewLoadingMessage : Element Msg
viewLoadingMessage =
    Element.el
        [ Element.centerX
        , Element.padding 20
        ]
    <|
        Element.text "(loading)"


view : LoadedModel -> Element Msg
view model =
    Element.text "hello"
