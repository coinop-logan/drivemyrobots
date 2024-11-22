module Types exposing (..)

import Browser
import Url exposing (Url)


type alias Flags =
    ()


type Msg
    = NoOp



-- | OnUrlRequest Browser.UrlRequest
-- | OnUrlChange Url


type Model
    = Loading LoadingModel
    | Loaded LoadedModel


type alias LoadingModel =
    ()


type alias LoadedModel =
    ()
