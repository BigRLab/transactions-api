transactions-api
=====

This service acts as a proxy between the deed-api service and the transactions-adapter service.
It has been developed within a Docker container.

See: deed-api at

See: transactions-adapter at

### Contents

- [Usage](#usage)
- [Available routes](#available-routes)
- [Useful Curl commands](#useful-curl-commands)
- [Quick start](#quick-start)
- [tests](#tests)

# Usage

Accepts json and forwards it to an adapter service.

# Available routes

```bash
post    /insert-transaction/    # Forwards a payload to a database adapter
```

### Useful curl commands

Insert a new transaction into DB2

```bash
curl -X POST -d '{"appn_trans_code":"C","appn_trans_value":123,"fee_categ_code":"2","lr_appn_ref":"ABR1234","title_no":"TN11111","trans_proc_curr":"Y"}' -H "Content-Type: application/json" http://localhost:5014/insert-transaction
```

## Quick start

Export some environment variables

```shell

export APP_NAME='transactions-api'
export TRANSACTION_ADAPTER_URI='http://transactions-adapter:8080'

```

Then run with 

```bash
make run
```

or 

```bash
flask run
```

## tests
```bash
py.test integration_tests
```
or
```bash
py.test unit_tests
```