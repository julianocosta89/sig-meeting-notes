SIG: Agent Management WG
Date: 2025-10-29
Duration: 9 minutes
Zoom Recording URL: https://zoom.us/rec/share/ZlelDztDgmbf8zMR5l76UI-_HuHJTU4YahiMI2DfOY2PQRLZTxfhyz5w7eRDT9tf.BLWww5Z09tMXR23w
============================================================

## Zoom Recording Transcript

**Jack Peterson** 00:16 I don't know.
**Tigran Najaryan** 00:18 Alrighty.
**Jack Peterson** 00:20 Good, how are you?
**Tigran Najaryan** 00:22 I'm good. Hi, Andy.
**Andy Keller** 00:31 Whoa.
See, were you back at KubeCon? Or Jack, for that matter?
Nope. Nope.
Kevin, will you be there?
**Evan Bradley** 01:01 Nope, I'm gonna be in San Francisco that week.
**Andy Keller** 01:05 Another conference, or…
**Evan Bradley** 01:07 No, just a buddy of mine wanted to use up some travel credit, so…
**Andy Keller** 01:11 Oh, nice.
**Evan Bradley** 01:11 you want to do.
**Andy Keller** 01:12 Yeah.
**Jack Peterson** 01:14 I think I was too late to, register, and I would have been over the, you know, conference budget or whatever, to go to Hotel Day, so I was like, well, I don't know, we'll go next year or whatever.
Maybe I can get out to Amsterdam or something in the spring.
**Andy Keller** 01:29 Yeah, I'm actually… I'm definitely going to Amsterdam as well, so…
**Evan Bradley** 01:33 Cool. I'm gonna try and make it out there as well.
**Andy Keller** 01:36 Cool.
Did you submit anything?
**Evan Bradley** 01:40 I will. I haven't yet.
**Andy Keller** 01:45 There's still time for… Observability Day, right?
**Evan Bradley** 01:49 Yep, and the Maintainer Summit.
**Andy Keller** 01:52 Alright, sure.
**Tigran Najaryan** 01:53 Did you guys submit a talk for… for OPAMP this… this year?
**Andy Keller** 01:58 I did.
Yeah.
Another…
It's… it's on OpAmp Gateway, which is in process, but hopefully you have more to share about soon. But it's the thing that you've talked about before, Deeren.
Hmm.
There's actually some kind of weird little things about it, like…
on connecting as a handler doesn't really make sense, because you'll have one connection from the gateway, but then you'll have a lot of agents connecting to the gateway, and how do you represent them?
Upstream, so I think we might need to introduce an unconnecting message, effectively, that would include headers and things for authentication.
To the extent that you're using headers, like client certificates, things like that, you'll want to send up to the…
back-end server, but you'll need to do that via another message, I think. So, I'm still sorting out the exact details on that. I'll start with a custom message, but…
Be happy to talk more about it as it gets closer.
**Tigran Najaryan** 03:05 Okay.
Yeah, we can discuss when you're ready.
Okay, we have nothing in the agenda for today.
So… I think I merged one PR.
And the other issue, Andy, you said you will… you will look into it, right? The one that Dakota.
**Andy Keller** 03:28 That's one, Dakota…
**Tigran Najaryan** 03:30 But it's just the issue about.
**Andy Keller** 03:34 No, I'm sorry.
**dpaasman** 03:35 the set capabilities?
**Andy Keller** 03:36 Yes.
**dpaasman** 03:37 Yeah, okay, I was gonna bring that up, I just didn't get a chance to add it to the agenda.
**Tigran Najaryan** 03:42 Yeah, yeah, I asked Andy to take a look at it, and a bit busy with some internal work right now.
I don't want to delay that. You guys can… And work on that together.
**dpaasman** 03:53 Cool.
**Tigran Najaryan** 03:56 Okay, and Jack, I saw you opened the issue…
With the, with the, Message signing your proposal.
So let's keep it open. If you want to direct people to comment on it.
advertise it, so it's all good, right? Let's keep it open for a while.
**Jack Peterson** 04:18 Absolutely. I'm gonna work on… I'm working on custom message, custom capability, as a demo,
That I should be able to share soon, but not… not ready for today, unfortunately.
**Tigran Najaryan** 04:31 Okay, cool.
What?
Anything else? Any other topics in the month?
**JM Juande Manjon** 04:40 So, Tigrant, thank you for merging my APR. So, in, in the chat, in the Slack chat, I'll be some…
A question about, open, open server.
Open source server.
so, I don't know what that expectation for everybody… so, for me, as a… as a…
user, what I had done, just copy and clone this example. I'm trying to do my server, my own server.
I am seeing that other people are doing the same thing.
So, we should find… try to find an area where we can provide
A server that actually has some kind of interface where they can plug in their stuff.
Instead of doing… everybody doing everything in their way.
I don't know if making sure this comes in.
**Tigran Najaryan** 05:29 What we have is really just a bare-bones example, right? It's not… it's not something you would use on production, obviously, but that's a… I'm with you. If we can improve it to make it more suitable, closer to something that you can then maybe fork and
and use, actually, as a production-grade Open server. Why not, right?
It's just that we never… Had the manpower to make the example
a more, I guess, more sophisticated example out of it, but yes, I think we should welcome…
**JM Juande Manjon** 06:02 Yeah, yeah. I have been working on that. Also, I see that there are some, like, if we have the way to have a…
A plugin for custom messages, where everybody can add their custom messages as a plugin, so we can run in that server and test it on
the client side.
For example, in the telemetry.
**Tigran Najaryan** 06:23 Through the example, do you mean?
**JM Juande Manjon** 06:25 Yes, or if we move the server to someone else, to somewhere, that way we… because now it's in the internal example, so it's not visible. So if we have, I don't know, another repo, or in the same repo where we can provide this structural server, a strong example where people can
At the start on top of that.
**Tigran Najaryan** 06:48 I think it's a possibility. We can do that, move it to a separate repo, if there is a significant momentum behind that, right? If there is, let's say, a few people who are
Committed to working on it and maintaining it.
We can make the case that, yes, it doesn't need to be an internal example anymore, we just make it a proper implementation. We could do that.
But for that, like I said, we need…
A proper commitment from a few people, at least, to be the maintainers of that repository, at least.
for now, I guess it's okay, we can keep working on that internal…
example, improve it. If at some point we see that there is really
Enough support to have a proper, like, a…
more of a reference implementation, rather than just an example. We could do that, yeah.
**JM Juande Manjon** 07:42 Right, but because the network is internal, you cannot import outside the repo.
**Tigran Najaryan** 07:47 Sure, yes. And that's on purpose, right? We didn't want to…
**JM Juande Manjon** 07:50 Right.
**Tigran Najaryan** 07:51 take the responsibility for maintaining it long-term, right? So we want it to be free to break it whenever we want to break it.
**JM Juande Manjon** 07:59 Right, but in my case, what I have done, I just copy-paste to another reposit are working on that.
So now I need to maintain both, and for me, it doesn't make sense.
**Tigran Najaryan** 08:08 I… yeah, I hear you, I understand what you're saying, but…
there's a significant step up in terms of how much time you have to contribute if it becomes a repository that now you have… you have to support the releases and stuff like that, you maintain it, documentation, all of that, right? You can see how much more work it is.
I don't think we are ready as a group to do that.
If there is people who are willing to do that, then that's a discussion we can have.
**JM Juande Manjon** 08:38 Okay.
**Tigran Najaryan** 08:44 And thanks for your PR, by the way.
**JM Juande Manjon** 08:46 Obviously, any improvements are very welcome.
**Tigran Najaryan** 08:56 Okay, anything else? Anyone?
Thank you all.
**Andy Keller** 09:09 Alright, have a good day.
