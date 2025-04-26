I.**NoSQL wide-column datastore**
- organize data into flexible columns (called column families) that can vary across rows. It means, each row can have a different set of columns, and columns can be added dynamically without altering the entire schema
- each row is identified by a row key. No duplicates are allowed.
- use `denormalization` technique (keep related data together in one row) while designing
- is built for big data, so they lean on **disks** for storage but use **memory** to speed things up
- often choose availability and partition tolerance (AP) over consistency (CP)
- use `eventual consistency`. It means data might be different at some nodes for a short time, but eventually data will be synced and consistent at all nodes (over the world)
- Ex: Apache Cassandra, Apache HBase, Bigtable 
