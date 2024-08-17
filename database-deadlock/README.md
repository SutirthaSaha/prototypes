# Deadlock creation

This prototype is try and replicate a deadlock in mysql and how to react when such a scenario happens.
To try this out we need to first deploy mysql and also provide some initial data.

## Setup MySQL

- `initialize.sql`: a script to create the database, table and populate with dummy data
- `docker-compose.yml`: easy way to set up your mysql locally

Command:
```sh
cd mysql
docker-compose up
```

## Lock Related Clauses:
- `FOR UPDATE`: 
  - This clause is used to lock the selected rows for the purpose of updating them
  - It prevents the selected rows from being modified or locked by other transactions until the current transaction ends
  -Other transactions trying to lock the same row with FOR UPDATE will be blocked until the lock is released
- `FOR UPDATE NOWAIT`:
  - When used with the above clauses (like FOR UPDATE NOWAIT), it specifies that if a requested row is locked by another transaction, the statement should not wait and instead fail immediately with an error
  - This is useful when you don't want a transaction to be held up waiting for locks to be released
- `FOR UPDATE SKIP LOCKED`:
  - This clause is used to modify FOR UPDATE or FOR SHARE so that instead of waiting for locked rows or failing, it skips over them
  - Useful in implementing job queues or similar patterns where you want to process only the rows that are not currently being processed by another transaction