## 1. What is blockchain technology?
- **Blockchain** is a **decentralized, distributed digital ledger** that records transactions across many computers (nodes) in a way that ensures the data is secure, transparent, immutable, and tamper-resistant
  - **Decentralization**: no single authority (like a bank) controls it. Copied of the ledger exist on thousands of nodes
  - **Immutability**: once data is added, it cannot be altered without consensus from the network
  - **Transparency**: anyone can view transaction (in public blockchains)
  - **Security**: uses digital signatures and hashing to secure data
  - **Consensus Mechanism**: rules (like Proof of Work or Proof of Stake) ensure all nodes agree on the ledger's state

## 2. Transaction
### How a transaction is created?
- each person has a [digital wallet]() that contains public key & private key.
  - the wallet address is a shorten version of the public key.
  - private key is used to sign the transaction to prove that the transaction is made by the owner of the wallet
  - digital signature: private-key-sign(hash-of-transaction)

### 2.1 How a transaction is verified?
- then the transaction is broadcasted to the peer-to-peer network of nodes
- nodes receive the transaction, and verify
  - verify if the wallet's balance is sufficient to make this transaction
  - verify if the digital signature is valid (use the public key to decrypt and compare the hashed values)
  - verify if no double-spending (@Todo)
- Valid transactions go into the mempool (a waiting area)

### 2.2 How a block is created?
- a **miner** (the owner of a node) selects transactions from the mempool
- the miners bundle them into a candidate block (e.g., up to ~1MB in Bitcoin)
- the block includes:
  - a list of transactions
  - **previous block's hash** (links the chain)
  - timestamp
  - **Nonce** (number used in **mining**)
  - **current block's hash** (hash of all transactions in this block)

### 2.3 Consensus (Proof of Work)
- the miners competes each other to solve a cryptographic puzzle (to find a **nonce**)
- this requires massive computation
- first miner who solves it will broadcast the block

### 2.4 How a block is added (or chained)?
- other nodes verify the new block
  - all transactions are valid
  - previous hash matches
  - nonce meets difficulty
- if valid, add the block to their copy of the blockchain

## 3. Security
 
### 3.1 How the blockchain is secured?
 - to successfully attack or rewrite the blockchain, an attacker must control more than 50% (**majority rule**) of the network's nodes.
   - blockchain relies on consensus - all nodes agree on one version of history (a block)
     
### 3.2 Who is the winner?
- who is the winner if many miners solved the puzzles?
  - miner A solves and broadcast -> create a chainA
  - miner B solves and broadcast -> create a chainB
  - the longest chain will win

## 4. Broadcast, how it works behind the scene?
- @Todo (via Peer-To-Peer Goship protocol)

## References

- [Blockchain 101 - A Visual Demo](https://www.youtube.com/watch?v=_160oMzblY8)
- [Blockchain 101 - Part 2 - Public / Private Keys and Signing](https://www.youtube.com/watch?v=xIDL_akeras&t=315s)



