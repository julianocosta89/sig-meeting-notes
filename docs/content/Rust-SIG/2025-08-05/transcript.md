SIG: Rust SIG
Date: 2025-08-05
Duration: 17 minutes
============================================================

## Zoom Recording Transcript

**Cijo Thomas (Microsoft)** 05:15 Hello!
**Nikhil Bhatia** 05:17 Hello!
**Cijo Thomas (Microsoft)** 05:18 Hey? Can you hear me?
**Nikhil Bhatia** 05:20 Yeah, I can hear you.
**Cijo Thomas (Microsoft)** 05:23 Yeah, thanks. Let's see if anyone else is joining. I missed the last one, so I'm not sure if there was anything anyone mentioned about skipping this one. So let's wait.
**Nikhil Bhatia** 05:34 Sure.
**Cijo Thomas (Microsoft)** 07:37 Okay, I think we can start. It's 3 min past 9. Hey?
Hey, Nicole, I do see that you are here last week. But I was not here. Just want to say Hello! Do you mind giving a quick intro? I know that you probably have done it last week, but just for the sake of it.
**Nikhil Bhatia** 07:56 Yeah, sure.
So I'm just getting started in the rest. SDK, so I'm looking for issues
so that I can contribute. And
actually, I am. I was an open source contributor as gitlab for Gitlab query language, which is a compiler written in rust.
I'm looking forward to do more contributions in Western secrets.
So I found open telemetry, and
I was. I read about it, and I'm interested now to contribute in it, so.
**Cijo Thomas (Microsoft)** 08:36 Yeah. Okay. Glad to have you here. Yeah. And welcome.
**Nikhil Bhatia** 08:39 Thanks.
**Cijo Thomas (Microsoft)** 08:40 Yeah, feel free to like, look at the open issues and see if anything interests you. We have like quite a large number of open issues, so like depending on your bandwidth and interest, there should be like one issue for every levels, like simple, easy ones to like quite hard ones. So please feel free to take a look around.
**Nikhil Bhatia** 09:04 Sure. Thank you.
**Cijo Thomas (Microsoft)** 09:07 I don't have anything in the agenda from anyone so hopefully, this should be pretty. Q. Guy, more like an faa thing. We now have completely enabled copilot in both
the main repo and the contribut repo
If anyone has concerns with that like, please raise it in the community issue which I believe was shared in.
Okay, maybe in the maintenance channel, because only maintenance and approvers have access to.
I say, any issues to a
can already see, like things are like
working well now, with copilot like it's reviewing, it's able to create. Pr, it's responding reasonably, well, like, if the issues like
straightforward, very small one. Yeah, it does work.
Yeah, it's more like fia, it's only for approvals and maintainers to like, assign it for now. So yeah.
another cube update is on Otlp exporter. So
Scott and I'm working to stabilize Otlp exporter. Scott is doing most of the work. I'm just helping
it's more like a update. We don't have a date in mind, but we have, captured almost all the issues pending which is required to make the
create as a stable one. There are maybe a dozen of them.
Some of them are like very small, some of them like media. Nothing like Major, like everything is like small to medium sized work.
He was not able to access. Yeah, this Pr, later. This, I believe there is no progress beyond is on vacation. And I don't see any updates
since last month. So this is concerning because we, a lot of public api changes in open elementary. Basically, we are trying to remove a lot of public Aps that will break tracing open telemetry this bridge unless this Pr is accepted. So
yeah, I mean, I don't have much control in this one.
so we'll wait for like beyond to come back. And
then we put like more aggressive timelines. It's almost 3 months without progress. So
we might put, like some firm timeline, that
open elementary will clean up the public Api, and
whether tracing works or not, that's completely up to tracing maintenance to accept the Pr.
Because we cannot delay the
progress like forever. It's been delayed for quite a while so on that same topic. We if we discussed like few weeks ago, like having some guidelines on what would be the
end story looks like after.
Like once the distributor tracing is declared stable in open telemetry.
It's I created as an issue. Not a Pr. But I'll convert it later to a pr, so people can actually comment. Ask clarification. And we can like once, everyone is happy. Then we can put it. Maybe like we can keep it under the Docs page itself.
It's very short, like, we are basically recommending what every other language in open elementary is doing. It's a no surprises. Use motel Api, for tracers use the tracing Api
for logs and events, and we we have the grid. So this is pretty much what every other language in point elementary is doing nothing special there.
This is like somewhat special, because there is no concept of in proc entrancement for logs in any language.
I mean, there is some in like.net, but there is no universal way.
and this has been requested a few times in the past, so we'll recommend people to use tracing span macros
to add like contextual metadata.
But it won't work today because the open elementary appender it does not look at span attributes at all. So it has to be enriched with that ability. So these 3 would be still like
like, quite unsurprising to most the last 2 parties where things are like bit messy. Because we know that people are already using tracing span macros, not for 3, but for creating like actual spans.
And this is where we are.
We don't have any support in open telemetry, except we did like some
special casing to make tracing work, but it's completely offered by this bridge tracing open elementary bridge.
But it does have like significant limitations. You cannot do remote parent, no ability to specify links or span kinds which are very crucial for server spans and client spans, even queuing scenarios. So there is no such ability in the tracing grade itself. So the bridge
started offering some extension Apis on top of this. But I don't think like we, as in open elementary, can make any recommendations about that.
So we can probably list them. That list. That tracing open elementary has some extensions, but whether they use it or not that's totally up to the users. In fact, I think maybe we should
recommend against using it. Because it's neither tracing. It's neither open, elementary, nor tracing. It's a
it's a bridge which is offering instrumentation Apis, which doesn't sound quite right to me. But anyway, like I'll write it into an Pr, so people can actively comment on it.
And this may be an issue for some people, because they're already quite used to.
or they are already instrumenting with the bridge. Apis. So asking them to reinstrument with hotel. Pure hotel might be a challenge
So point number 5 is all about like how to mitigate that to a certain extent.
because most of the time.
The need for remote parent and span kind are only for edge spans, and the those are like usually covered by instrumentation library. So if you're using actics or
tower, then there could be an instrumentation library which does it automatically. So users, excuse me, doesn't have to manually create
spans using any aps, it just exists by default for them, not by default, like by installing Instrumentation library. This kind of like mitigates a lot of pain. But again, it's not perfect like. It won't work with
any scenarios. It only it won't work. In all scenarios. It only works in specific scenarios where there is an Instrumentation library.
So I'll convert this into a Pr for people to review.
There are quite a lot of work to actually materialize this thing like it's
I have done some prs to show benchmarks last week week before. It looks like the cost of creating span is like significantly higher than what it should be so we need to solve all those problems. But this is mostly to
get everyone to see if we agree on the long term direction, issues like performance and other things. Yeah, they are more like implementation details. This is mostly setting the direction. Only.
Yeah, any comments on that. Otherwise I'll create it into a Pr, so people can comment.
Alright. So nothing else. Any other topics which we should cover anything from previous weeks.
Yeah, I don't see anything from previous. So we can end early.
Thank you. Everyone. If there is anything we need discussion we can use Prs to cover it. Oh, by the way, that remains me like good question, like, if you get some free time like, just look at open Prs. I have like some very small Prs. Open. Nothing big like quite small.
**lalit** 17:28 Sure, sure.
**Cijo Thomas (Microsoft)** 17:30 Thank you. Thanks everyone. Bye-bye.
**lalit** 17:34 Thank you. Bye.
**Nikhil Bhatia** 17:35 Thank you. Bye.
