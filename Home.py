# 📚 Libraries
import streamlit as st
import PIL
from PIL import Image

Near = PIL.Image.open('Near.png')

# Title
st.set_page_config(page_title='Activity of NEAR Developers', page_icon=Near, layout='wide')
st.title('Activity of NEAR Developers')

# Content
c1, c2 = st.columns(2)

c1.image(Image.open('Images/COVER.JPG'))

st.subheader('📃 Introduction')


st.write(
    """
Today, if someone wants to use a simple application or game launched on the blockchain platform, he has to go through many steps; Therefore, the Near network has put its main focus on the usability and user-friendliness of its platform; Developers and programmers and end users of products launched on the Near platform should feel better and more comfortable when using it. This network is very similar to Ethereum in terms of idea and is a platform for launching decentralized applications. The Near protocol is similar to the Ethereum network; With the difference that this chain tries to provide higher usability, scalability, and ease, and finally be a completely decentralized network. The NEAR protocol provides a platform where programmers can freely present their programs. With such programs, we will have a better world where people are fully in control of their assets, be it money, personal information, etc.

🤔 **What is the purpose of creating the Near protocol?**

The main goal of the NEAR network is to create an infrastructure for creating a new Internet. In the new internet, it will be harder for big companies to access people's personal information. Countries cannot ban some programs and destroy people's business in this system. A world of freedom where everyone can act freely. Of course, this goal of the Near network is not a new concept; In fact, Satoshi Nakamoto also pursued the same goal by introducing Bitcoin in 2008. But Bitcoin has created this freedom only in the financial sphere. But like many other networks, Near seeks to expand this freedom to other aspects of human life.

👌  **Near protocol features**

1️⃣ The speed of transactions in Near network is high and the transaction fees are low. The reason for this is that Near protocol uses sharding technology.

2️⃣ Scalability is an important concept in the blockchain world. Near protocol uses sharding technology to solve the scalability problem. In this model, a transaction does not need to be checked by all network nodes. With sharding, a network is transformed into several parallel networks that check transactions simultaneously, so t hat each transaction is checked in a shard. As a result, only nodes present in a shard will check and confirm this transaction, and other nodes present in other shards of the network will not check this transaction. This idea makes the capacity of the network increase significantly.

3️⃣ Sharding technology is also used by other protocols and for this reason Near protocol is not the first network. In many networks that use sharding, relatively complex hardware equipment is needed to set up a node; Therefore, fewer people are able to set up nodes in these networks; But the Near protocol uses the cloud space of the host to launch the node.

4️⃣ Unlike other layer 1 networks such as Avalanche, which adopted Solidity to make it easier to integrate with Ethereum, NEAR became a developer-first network with support for WebAssembly (WASM).

5️⃣ The NEAR protocol does not follow Polkadot, BSC, or Solana networks that use 64-character public keys; Rather, by abandoning the use of public keys for wallets, the wallets of this network are the first wallets in which people's addresses are the same as their profile names. Therefore, the Near network not only aims to make the process of developing and creating various programs easy for developers, but also users can easily benefit from its services.
    """
)

st.subheader('🎯 Purposes of Dashboard')
st.write(
    """
We Produced a rich analysis of NEAR developer activity, using metrics and definitions to answer the questions:

- **How many developers are active on NEAR?**
- **How active are they?**
- **How this has changed over time?**
    """
)

st.subheader('📖 Vocabulary')
st.write(
    """
⚫ **GitHub**

GitHub is a code hosting platform for version control and collaboration. It lets users work together on projects from anywhere.

⚫ **Repository**

A repository contains all of users project's files and each file's revision history. users can discuss and manage their project's work within the repository.

⚫ **Pull requests**

Pull requests let users tell others about changes they've pushed to a branch in a repository on GitHub. Once a pull request is opened, users can discuss and review the
potential changes with collaborators and add follow-up commits before their changes are merged into the base branch.
    """
)


c1, c2, c3 = st.columns(3)
with c1:
    st.info('**Analyst: [Emanoel](https://twitter.com/Astiran91)**', icon="📌")

with c2:
    st.info('**Database: [Flipside Crypto](https://flipsidecrypto.xyz/)**', icon="📚")

with c3:
    st.info('**Provided for: [MetricsDao](https://metricsdao.xyz/)**', icon="💡")






