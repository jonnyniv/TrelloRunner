# TrelloRunner

TrelloRunner aims to provide a unified interface for performing actions on Trello.
It aims to do this by separating the concept of config, action, and runner.
This should allow actions to be scripted generically, and applied to an arbitrary config, representing a specific account.#

v1.0 aims to have 3 main objects: Trello, TrelloRunner, and TrelloAction.

The Trello object represents a specific config, which wraps authentication into a tidy interface.

The TrelloAction object represent a series of actions used to produce an end result.
The actions may or may not be described Ansible style (in a YML), and the object may or may not be recursive (Defining multiple actions).

The TrelloRunner takes a TrelloAction and applies it to the Trello config. It will handle converting actions to API calls.
It may also validate correct application of actions using some expected state checking. 
It may ensure idempotence of actions, meaning the same action applied twice won't change the state of the Trello account.

Due to the inability to delete lists, it may be impossible to undo a failed action, but it can hide it and/or run some pre-state changing checks to ensure that the repo is in a known state.