
This document was made to lay out the Sim's architecture to expose coupling problems and help improve the program overall.

## Classes

# Match:
    Represents Individual Matches

    Methods:
        play()
        simPossession()
        switchPos()
        checkRebound()
        choosePlayer()
        getBestShooters()
        getBestIso()
        chooseGoal()
        getTeamPos()
        shootIt()
        getShotOutcome()
        checkTurnover()
        getTimeSpent()
        showstats()
    Attributes:
        teams
        lineups
        scores
        haspossession
        defending
        pwithball
        gametime
        totalpossessions
        quarter
        quartertime
        offthebats
        shots
        passes
        violations
# Team:
    Represents a team

    Methods:
        None
    Attributes:
        name
        players
        roster
        wins
        losses
        avgpts
        gamescores
# Player:
    Represents individual players

    Methods:
        logShot()
        flip()
    Attributes:
        team
        data
        index
        shotodds
        threeodds
        midodds
        layodds
        passodds
        threeshot
        midshot
        layshot
        stl
        perdef
        paintdef
        speed
        ballhandle
        loc
        points
        threes
        mids
        lays
        shottot
        shotsmade
    Properites:
        game_stats
        fgper

## How Games Are Run

# Play
Play sets up a loop that breaks when the timer is ran out, and keeps track of which quarter it is. It calls simPossession() on every loop

# simPossession
SimPossession does a lot. Here are it's ordered steps:
1. get current offensive and defensive lineups based on string of which team has the ball
2. Set shot clock
3. Initialize time_elapsed
4. Loop over shotclock:
    a. get team position (getTeamPos)
    b. choose team goal (chooseGoal)
    c. check if goal is give up, if so then dribble out
    d. choose shooter based on team goal and offensive lineup (getBestShooters)
    e. choose matchup based on corresponding index of shooter on other team
    f. run shot attempt
    g. subtract time elapsed and check for shotclock violations
    h. if shot made, log it, and assign scores 
    i. if shot missed, log it, and check for rebound
    j. if turnover, break out of loop
5. subtract time elapsed from quartertime
6. add to total gametime
7. switch which team has possession
8. add to total possessions

## Current Flaws
1. Lineups are static and predetermined (no substitutions)
2. Defensive matchups are chosen through a broken system