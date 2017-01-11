#!/bin/bash

DATASET=/DoubleEG/Run2015A-v1/RAW
INSTANCE=global

if [ ! -z "${2}" ]; then
    DATASET=${2}
fi
if [ ! -z "${3}" ]; then
    INSTANCE=${3}
fi

RUNLIST=`./das_client.py --query "lumi run dataset=${DATASET} instance=prod/${INSTANCE}" --limit 0 --secondary-key lumi.number`

echo -ne '{\n '$RUNLIST'\n}' | sed 's:]] :]],\n :g' | sed 's:\[\[:\: \[\[:g' | sed 's: \::" \::g' | sed 's:^[^{}]: ":g' > ${1}

exit 0