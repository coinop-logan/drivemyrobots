module State exposing (..)

import Browser
import Browser.Navigation as Nav
import Types exposing (..)
import Url exposing (Url)


init : Flags -> Url -> Nav.Key -> ( Model, Cmd Msg )
init flags url key =
    ( Loaded (), Cmd.none )


update : Msg -> Model -> ( Model, Cmd Msg )
update msg model =
    case msg of
        NoOp ->
            ( model, Cmd.none )



-- OnUrlRequest urlRequest ->
--     case urlRequest of
--         Browser.Internal url ->
--             ( model
--             , Nav.pushUrl model.key (Url.toString url)
--             )
--         Browser.External url ->
--             ( model
--             , Nav.load url
--             )
-- OnUrlChange url ->
--     let
--         route =
--             Route.parseUrl url
--     in
--     ( { model
--         | route = route
--         , bodyViewport = Nothing
--       }
--     , case route of
--         Route.Projects (Just fragmentIdStr) ->
--             scrollToProjectId fragmentIdStr
--         _ ->
--             Cmd.none
--     )
-- case model of
--     Loading loadingModel ->
--         (case msg of
--             GotViewport viewport ->
--                 { loadingModel
--                     | viewport = Just viewport
--                 }
--             UpdateNow newNow ->
--                 { loadingModel
--                     | time_bySecond = Just newNow
--                 }
--             _ ->
--                 loadingModel
--         )
--             |> (\loadingModelModified ->
--                     -- test if loaded
--                     case ( loadingModelModified.viewport, loadingModelModified.time_bySecond ) of
--                         ( Just viewport, Just time_bySecond ) ->
--                             initLoadedModel viewport time_bySecond loadingModelModified.url loadingModelModified.key
--                         _ ->
--                             ( Loading loadingModelModified
--                             , Cmd.none
--                             )
--                )
--     Loaded loadedModel ->
--         updateLoadedModel msg loadedModel
--             |> Tuple.mapFirst Loaded


subscriptions : Model -> Sub Msg
subscriptions model =
    Sub.none
