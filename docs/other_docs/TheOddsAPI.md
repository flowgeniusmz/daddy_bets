#The-Odds-API List of Values

## Betting Markets
The odds api covers the betting markets below

### Featured Betting Markets
These are the most common markets that are featured by bookmakers. Terminology for betting markets can vary by country, sport and even amongst bookmakers. We aim to simplify this by defining the following markets

| Market Key (use in the API) | Market Names                   | Description |
|-----------------------------|--------------------------------|-------------|
| h2h                         | Head to head, Moneyline        | Bet on the winning team or player of a game (includes the draw for soccer) |
| spreads                     | Points spread, Handicap        | The spreads market as featured by a bookmaker. Bet on the winning team after a points handicap has been applied to each team |
| totals                      | Total points/goals, Over/Under | The totals market as featured by a bookmaker. Bet on the total score of the game being above or below a threshold |
| outrights                   | Outrights, Futures             | Bet on a final outcome of a tournament or competition |
| h2h_lay                     | Same as h2h                    | Bet against a h2h outcome. This market is only applicable to betting exchanges |
| outrights_lay               | Same as outrights              | Bet against an outrights outcome. This market is only applicable to betting exchanges |


### Additional Betting Markets
Additional Markets BETA
Starting in 2023, more markets are becoming available in the API. Additional markets are currently limited to US sports and selected bookmakers, however coverage is expanding. Additional markets update at 5 minute intervals.

Due to the growing size of the API response, additional markets need to be accessed one event at a time using the new /events/{eventId}/odds endpoint.

| Market Key (use in the API) | Market Name                      | Description |
|-----------------------------|----------------------------------|-------------|
| alternate_spreads           | Alternate Spreads (handicap)     | All available point spread outcomes for each team |
| alternate_totals            | Alternate Totals (Over/Under)    | All available over/under outcomes |
| btts                        | Both Teams to Score              | Odds that both teams will score during the game. Outcomes are "Yes" or "No". Available for soccer. |
| draw_no_bet                 | Draw No Bet                      | Odds for the match winner, excluding the draw outcome. A draw will result in a returned bet. Available for soccer |
| h2h_3_way                   | Head to head / Moneyline 3 way   | Match winner including draw |
| team_totals                 | Team Totals                      | Currently only available for MLB & NFL |


### Game Period Markets
Game period markets depend on the sport, and can include quarter time odds, half time odds, period odds, and innings odds.

| Market Key (use in the API)           | Market Name                          | Note                 |
|---------------------------------------|--------------------------------------|----------------------|
| h2h_q1                                | Moneyline 1st Quarter                |                      |
| h2h_q2                                | Moneyline 2nd Quarter                |                      |
| h2h_q3                                | Moneyline 3rd Quarter                |                      |
| h2h_q4                                | Moneyline 4th Quarter                |                      |
| h2h_h1                                | Moneyline 1st Half                   |                      |
| h2h_h2                                | Moneyline 2nd Half                   |                      |
| h2h_p1                                | Moneyline 1st Period                 | Valid for ice hockey |
| h2h_p2                                | Moneyline 2nd Period                 | Valid for ice hockey |
| h2h_p3                                | Moneyline 3rd Period                 | Valid for ice hockey |
| h2h_1st_1_innings                     | Moneyline 1st inning                 | Valid for baseball   |
| h2h_1st_3_innings                     | Moneyline 1st 3 innings              | Valid for baseball   |
| h2h_1st_5_innings                     | Moneyline 1st 5 innings              | Valid for baseball   |
| h2h_1st_7_innings                     | Moneyline 1st 7 innings              | Valid for baseball   |
| h2h_3_way_1st_1_innings               | 3-way moneyline 1st inning           | Valid for baseball   |
| h2h_3_way_1st_3_innings               | 3-way moneyline 1st 3 innings        | Valid for baseball   |
| h2h_3_way_1st_5_innings               | 3-way moneyline 1st 5 innings        | Valid for baseball   |
| h2h_3_way_1st_7_innings               | 3-way moneyline 1st 7 innings        | Valid for baseball   |
| spreads_q1                            | Spreads 1st Quarter                  |                      |
| spreads_q2                            | Spreads 2nd Quarter                  |                      |
| spreads_q3                            | Spreads 3rd Quarter                  |                      |
| spreads_q4                            | Spreads 4th Quarter                  |                      |
| spreads_h1                            | Spreads 1st Half                     |                      |
| spreads_h2                            | Spreads 2nd Half                     |                      |
| spreads_p1                            | Spreads 1st Period                   | Valid for ice hockey |
| spreads_p2                            | Spreads 2nd Period                   | Valid for ice hockey |
| spreads_p3                            | Spreads 3rd Period                   | Valid for ice hockey |
| spreads_1st_1_innings                 | Spreads 1st inning                   | Valid for baseball   |
| spreads_1st_3_innings                 | Spreads 1st 3 innings                | Valid for baseball   |
| spreads_1st_5_innings                 | Spreads 1st 5 innings                | Valid for baseball   |
| spreads_1st_7_innings                 | Spreads 1st 7 innings                | Valid for baseball   |
| alternate_spreads_1st_1_innings       | Alternate spreads 1st inning         | Valid for baseball   |
| alternate_spreads_1st_5_innings       | Alternate spreads 1st 5 innings      | Valid for baseball   |
| totals_q1                             | Over/under 1st Quarter               |                      |
| totals_q2                             | Over/under 2nd Quarter               |                      |
| totals_q3                             | Over/under 3rd Quarter               |                      |
| totals_q4                             | Over/under 4th Quarter               |                      |
| totals_h1                             | Over/under 1st Half                  |                      |
| totals_h2                             | Over/under 2nd Half                  |                      |
| totals_p1                             | Over/under 1st Period                | Valid for ice hockey |
| totals_p2                             | Over/under 2nd Period                | Valid for ice hockey |
| totals_p3                             | Over/under 3rd Period                | Valid for ice hockey |
| totals_1st_1_innings                  | Over/under 1st inning                | Valid for baseball   |
| totals_1st_3_innings                  | Over/under 1st 3 innings             | Valid for baseball   |
| totals_1st_5_innings                  | Over/under


### Player Prop Markets
#### NFL NCAAF Player Props
| Market Key (use in the API)      | Market Name                           |
|----------------------------------|---------------------------------------|
| player_pass_tds                  | Pass Touchdowns (Over/Under)          |
| player_pass_yds                  | Pass Yards (Over/Under)               |
| player_pass_completions          | Pass Completions (Over/Under)         |
| player_pass_attempts             | Pass Attempts (Over/Under)            |
| player_pass_interceptions        | Pass Intercepts (Over/Under)          |
| player_pass_longest_completion   | Pass Longest Completion (Over/Under)  |
| player_rush_yds                  | Rush Yards (Over/Under)               |
| player_rush_attempts             | Rush Attempts (Over/Under)            |
| player_rush_longest              | Longest Rush (Over/Under)             |
| player_receptions                | Receptions (Over/Under)               |
| player_reception_yds             | Reception Yards (Over/Under)          |
| player_reception_longest         | Longest Reception (Over/Under)        |
| player_kicking_points            | Kicking Points (Over/Under)           |
| player_field_goals               | Field Goals (Over/Under)              |
| player_tackles_assists           | Tackles + Assists (Over/Under)        |
| player_1st_td                    | 1st Touchdown Scorer (Yes/No)         |
| player_last_td                   | Last Touchdown Scorer (Yes/No)        |
| player_anytime_td                | Anytime Touchdown Scorer (Yes/No)     |

#### NBA, NCAAB, WNBA Player Props
| Market Key (use in the API)                  | Market Name                               |
|----------------------------------------------|-------------------------------------------|
| player_points                                | Points (Over/Under)                       |
| player_rebounds                              | Rebounds (Over/Under)                     |
| player_assists                               | Assists (Over/Under)                      |
| player_threes                                | Threes (Over/Under)                       |
| player_double_double                         | Double Double (Yes/No)                    |
| player_blocks                                | Blocks (Over/Under)                       |
| player_steals                                | Steals (Over/Under)                       |
| player_turnovers                             | Turnovers (Over/Under)                    |
| player_points_rebounds_assists               | Points + Rebounds + Assists (Over/Under)  |
| player_points_rebounds                       | Points + Rebounds (Over/Under)            |
| player_points_assists                        | Points + Assists (Over/Under)             |
| player_rebounds_assists                      | Rebounds + Assists (Over/Under)           |

#### MLB Player Props
| Market Key (use in the API)              | Market Name                           |
|------------------------------------------|---------------------------------------|
| batter_home_runs                         | Batter home runs (Over/Under)         |
| batter_hits                              | Batter hits (Over/Under)              |
| batter_total_bases                       | Batter total bases (Over/Under)       |
| batter_rbis                              | Batter RBIs (Over/Under)              |
| batter_runs_scored                       | Batter runs scored (Over/Under)       |
| batter_hits_runs_rbis                    | Batter hits + runs + RBIs (Over/Under)|
| batter_singles                           | Batter singles (Over/Under)           |
| batter_doubles                           | Batter doubles (Over/Under)           |
| batter_triples                           | Batter triples (Over/Under)           |
| batter_walks                             | Batter walks (Over/Under)             |
| batter_strikeouts                        | Batter strikeouts (Over/Under)        |
| batter_stolen_bases                      | Batter stolen bases (Over/Under)      |
| pitcher_strikeouts                       | Pitcher strikeouts (Over/Under)       |
| pitcher_record_a_win                     | Pitcher to record a win (Yes/No)      |
| pitcher_hits_allowed                     | Pitcher hits allowed (Over/Under)     |
| pitcher_walks                            | Pitcher walks (Over/Under)            |
| pitcher_earned_runs                      | Pitcher earned runs (Over/Under)      |
| pitcher_outs                             | Pitcher outs (Over/Under)             |

#### NHL Player Props
| Market Key (use in the API)              | Market Name                           |
|------------------------------------------|---------------------------------------|
| player_points                            | Points (Over/Under)                   |
| player_power_play_points                 | Power play points (Over/Under)        |
| player_assists                           | Assists (Over/Under)                  |
| player_blocked_shots                     | Blocked shots 

## Bookmakers
### US Bookmakers
| Region key | Bookmaker key  | Bookmaker                        |
|------------|----------------|----------------------------------|
| us         | betonlineag    | BetOnline.ag (opens new window)  |
| us         | betmgm         | BetMGM (opens new window)        |
| us         | betrivers      | BetRivers (opens new window)     |
| us         | betus          | BetUS (opens new window)         |
| us         | bovada         | Bovada (opens new window)        |
| us         | draftkings     | DraftKings (opens new window)    |
| us         | fanduel        | FanDuel (opens new window)       |
| us         | lowvig         | LowVig.ag (opens new window)     |
| us         | mybookieag     | MyBookie.ag (opens new window)   |
| us         | pointsbetus    | PointsBet (US) (opens new window)|
| us         | superbook      | SuperBook (opens new window)     |
| us         | twinspires     | TwinSpires (opens new window)    |
| us         | unibet_us      | Unibet (opens new window)        |
| us         | williamhill_us | William Hill (Caesars) (opens new window) |
| us         | wynnbet        | WynnBET (opens new window)       |
| us2        | betparx        | betPARX (opens new window)       |
| us2        | espnbet        | ESPN BET (opens new window)      |
| us2        | fliff          | Fliff (opens new window)         |
| us2        | sisportsbook   | SI Sportsbook (opens new window) |
| us2        | tipico_us      | Tipico (opens new window)        |
| us2        | windcreek      | Wind Creek (Betfred PA)          |


## Sports
| Key                                        | Group             | Title                         | Description                                 | Active | Has Outrights |
|--------------------------------------------|-------------------|-------------------------------|---------------------------------------------|--------|---------------|
| americanfootball_ncaaf                     | American Football | NCAAF                         | US College Football                         | true   | false         |
| americanfootball_ncaaf_championship_winner | American Football | NCAAF Championship Winner     | US College Football Championship Winner     | true   | true          |
| americanfootball_nfl                       | American Football | NFL                           | US Football                                 | true   | false         |
| americanfootball_nfl_super_bowl_winner     | American Football | NFL Super Bowl Winner         | Super Bowl Winner 2023/2024                 | true   | true          |
| aussierules_afl                            | Aussie Rules      | AFL                           | Aussie Football                             | true   | false         |
| basketball_euroleague                      | Basketball        | Basketball Euroleague         | Basketball Euroleague                       | true   | false         |
| basketball_nba                             | Basketball        | NBA                           | US Basketball                               | true   | false         |
| basketball_nba_championship_winner         | Basketball        | NBA Championship Winner       | Championship Winner 2023/2024               | true   | true          |
| basketball_ncaab                           | Basketball        | NCAAB                         | US College Basketball                       | true   | false         |
| basketball_ncaab_championship_winner       | Basketball        | NCAAB Championship Winner     | US College Basketball Championship Winner   | true   | true          |
| boxing_boxing                              | Boxing            | Boxing                        | Boxing Bouts                                | true   | false         |
| cricket_big_bash                           | Cricket           | Big Bash                      | Big Bash League                             | true   | false         |
| cricket_international_t20                  | Cricket           | International Twenty20        | International Twenty20                      | true   | false         |
| cricket_odi                                | Cricket           | One Day Internationals        | One Day Internationals                      | true   | false         |
| cricket_test_match                         | Cricket           | Test Matches                  | International Test Matches                  | true   | false         |
| golf_masters_tournament_winner             | Golf              | Masters Tournament Winner     | 2024 Winner                                 | true   | true          |
| golf_pga_championship_winner               | Golf              | PGA Championship Winner       | 2024 Winner                                 | true   | true          |
| golf_the_open_championship_winner          | Golf              | The Open Winner               | 2024 Winner                                 | true   | true          |
| golf_us_open_winner                        | Golf              | US Open Winner                | 2024 Winner                                 | true   | true          |
| icehockey_nhl                              | Ice Hockey        | NHL                           | US Ice Hockey                               | true   | false         |
| icehockey_nhl_championship_winner          | Ice Hockey        | NHL Championship Winner       | Stanley Cup Winner 2022/2023                | true   | true          |
| icehockey_sweden_allsvenskan               | Ice Hockey        | HockeyAllsvenskan             | Swedish Hockey Allsvenskan                  | true   | false         |
| icehockey_sweden_hockey_league             | Ice Hockey        | SHL                           | Swedish Hockey League                       | true   | false         |
| mma_mixed_martial_arts                     | Mixed Martial Arts| MMA                           | Mixed Martial Arts                          | true   | false         |
| politics_us_presidential_election_winner   | Politics          | US Presidential Elections Winner | 2024 US Presidential Election Winner      | true   | true          |
| rugbyleague_nrl                            | Rugby League      | NRL                           | Aussie Rugby League                         | true   | false         |
| soccer_australia_aleague                   | Soccer            | A-League                      | Aussie Soccer                               | true   | false         |
| soccer_austria_bundesliga                  | Soccer            | Austrian Football Bundesliga  | Austrian Soccer                             | true   | false         |
| soccer_belgium_first_div                   | Soccer            | Belgium First Div             | Belgian First Division A                    | true   | false         |
| soccer_brazil_campeonato                   | Soccer            | Brazil Série A                | Brasileirão Série A                         | true   | false         |
| soccer_chile_campeonato                    | Soccer            | Primera División - Chile      | Campeonato Chileno                          | true   | false         |
| soccer_efl_champ                           | Soccer            | Championship                  | EFL Championship                            | true   | false         |
| soccer_england_league1                     | Soccer            | League 1                      | EFL League 1                                | true   | false         |
| soccer_england_league2                     | Soccer            | League 2                      | EFL League 2                                | true   | false         |
| soccer_epl                                 | Soccer            | EPL                           | English Premier League                      | true   | false         |
| soccer_fa_cup                              | Soccer            | FA Cup                        | Football Association Challenge Cup          | true   | false         |
| soccer_fifa_world_cup_winner               | Soccer            | FIFA World Cup Winner         | FIFA World Cup Winner 2026                  | true   | true          |
| soccer_france_ligue_one                    | Soccer            | Ligue 1 - France              | French Soccer                               | true   | false         |
| soccer_france_ligue_two                    | Soccer            | Ligue 2 - France              | French Soccer                               | true   | false         |
| soccer_germany_bundesliga                  | Soccer            | Bundesliga - Germany          | German Soccer                               | true   | false         |
| soccer_germany_bundesliga2                 | Soccer            | Bundesliga 2 - Germany        | German Soccer                               | true   | false         |
| soccer_germany_liga3                       | Soccer            | 3. Liga - Germany             | German Soccer                               | true   | false         |
| soccer_greece_super_league                 | Soccer            | Super League - Greece         | Greek Soccer                                | true   | false         |
| soccer_italy_serie_a                       | Soccer            | Serie A - Italy               | Italian Soccer                              | true   | false         |
| soccer_italy_serie_b                       | Soccer            | Serie B - Italy               | Italian Soccer                              | true   | false         |
| soccer_mexico_ligamx                       | Soccer            | Liga MX                       | Mexican Soccer                              | true   | false         |
| soccer_netherlands_eredivisie              | Soccer            | Dutch Eredivisie              | Dutch Soccer                                | true   | false         |
| soccer_poland_ekstraklasa                  | Soccer            | Ekstraklasa - Poland          | Polish Soccer                               | true   | false         |
| soccer_spain_la_liga                       | Soccer            | La Liga - Spain               | Spanish Soccer                              | true   | false         |
| soccer_spain_segunda_division              | Soccer            | La Liga 2 - Spain             | Spanish Soccer                              | true   | false         |
| soccer_spl                                 | Soccer            | Premiership - Scotland        | Scottish Premiership                        | true   | false         |
| soccer_switzerland_superleague             | Soccer            | Swiss Superleague             | Swiss Soccer                                | true   | false         |
| soccer_turkey_super_league                 | Soccer            | Turkey Super League           | Turkish Soccer                              | true   | false         |
| soccer_uefa_champs_league                  | Soccer            | UEFA Champions League         | European Champions League                   | true   | false         |
| soccer_uefa_euro_qualification             | Soccer            | UEFA Euro Qualification       | European Championship Qualification         | true   | false         |
| soccer_uefa_europa_league                  | Soccer            | UEFA Europa League            | European Europa League                      | true   | false         |
| soccer_usa_mls                             | Soccer            | MLS                           | Major League Soccer                         | true   | false         |


## Requests Template and Examples
### Get Historical Odds
#### Endpoint
GET /v4/sports/{sport}/odds-history/?apiKey={apiKey}&regions={regions}&markets={markets}&date={date}
#### Example
GET https://api.the-odds-api.com/v4/sports/americanfootball_nfl/odds-history/?apiKey=YOUR_API_KEY&regions=us&markets=h2h&oddsFormat=american&date=2021-10-18T12:00:00Z

### Get Scores
#### Endpoint
GET /v4/sports/{sport}/scores/?apiKey={apiKey}&daysFrom={daysFrom}&dateFormat={dateFormat}
#### Example
GET https://api.the-odds-api.com/v4/sports/basketball_nba/scores/?daysFrom=1&apiKey=YOUR_API_KEY

### Get Odds
#### Endpoint
GET /v4/sports/{sport}/odds/?apiKey={apiKey}&regions={regions}&markets={markets}
#### Example
GET https://api.the-odds-api.com/v4/sports/americanfootball_nfl/odds/?apiKey=YOUR_API_KEY&regions=us&markets=h2h,spreads&oddsFormat=american

### Get Sports
#### Endpoint
GET /v4/sports/?apiKey={apiKey}
#### Example
GET https://api.the-odds-api.com/v4/sports/?apiKey=YOUR_API_KEY

### Get Event Odss
#### Endpoint
GET /v4/sports/{sport}/events/{eventId}/odds?apiKey={apiKey}&regions={regions}&markets={markets}&dateFormat={dateFormat}&oddsFormat={oddsFormat}
#### Example
GET https://api.the-odds-api.com/v4/sports/americanfootball_nfl/events/a512a48a58c4329048174217b2cc7ce0/odds?apiKey=YOUR_API_KEY&regions=us&markets=player_pass_tds&oddsFormat=american




https://the-odds-api.com/account/