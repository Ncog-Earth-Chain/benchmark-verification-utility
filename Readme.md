# Python blockchain log parser

This module will process the logs and extracting the information related
to the number of transactions in the blocks. This log contains the
information related to events, blocks, transactions etc. So, from all
that information, we need to find those log information which is talks
about the new block information.


## Extract the details from those lines, the information like block
time including miliseconds, number of transactions etc.

## suppose we need to tell the user for how many transactions on an
average are there in one second higest, extract the information from the
log for the new blocks information.

## Collect all the information in a list in python and then you are able
to give relevant results easily. Eg. there can be multiple blocks in a
second as we have sub-second finality.

## Search for every block and give result for the highest number of
transactions in a second in the specified time range. There will be two
options, first, to pass the time range from the command line as
parameters like we pass in linux commands. If no parameter is passed
then the whole log will be analysed.here are two kinds of transactions
per second, First is the absolute like we\'ll see the highest number of
transactions in a second in multiple blocks. The second way is the
average transactions per second, which is the standard process as
everyone talks about that. So, we\'ll show both results.

### Use Case! 
This module is independent from the blockchain. This module is
open source. People will use this module to verify the blockchain
transactions per second which we will be showing on the dashboard from
the network data. This module will use the logs which will be available
to download from the dashboard and/or people can also use the logs from
the live main net to verify the block data for TPS(Transaction Per
Second). User can input the things like the logs file path time/date
range etc. You\'ll verify from the starting and ending of the logs to
check for the time range. You\'ll then process the data from the logs
and will provide the processed information from the log data.
