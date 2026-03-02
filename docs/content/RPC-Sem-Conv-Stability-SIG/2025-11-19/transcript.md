SIG: RPC Sem Conv Stability SIG
Date: 2025-11-19
Duration: 10 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 02:06 Hey, Steve!
**Steve Rao** 02:09 Hello?
**Trask Stalnaker** 02:10 How you doing?
**Steve Rao** 02:15 Hello? Hello, Traska.
**Trask Stalnaker** 02:18 How are you doing?
**Steve Rao** 02:19 Yeah, I'm good. Yeah, next week we have a vacation, team vacation.
**Trask Stalnaker** 02:25 Yes, we have Thanksgiving, U.S. holiday. It's not a… it's just two days, but it's…
**Steve Rao** 02:33 Okay.
**Trask Stalnaker** 02:33 Felt good.
**Steve Rao** 02:35 Okay, yeah. Yeah, how…
**Trask Stalnaker** 02:39 the CooperCan North America.
It was good. Yeah, a good number of… OpenTelemetry folks there.
**Steve Rao** 02:54 Okay.
**Trask Stalnaker** 02:56 I… Faa… A small handful of talks?
Looking forward to the, I've been on their YouTube page, refreshing, waiting for all the… waiting for them to post all the talks so I can watch all the ones that I wanted to see, but ended up chatting with people in the, OpenTelemetry booth instead.
**Steve Rao** 03:20 Okay, yeah, yeah, me too, yeah.
**Trask Stalnaker** 03:33 We'll get a… minute, if Lydmilla is able to make it.
**Steve Rao** 03:41 Okay.
**Trask Stalnaker** 04:22 Actually, I will put in our channel…
Oh, no, let's see, when's… no, that was…
**Steve Rao** 05:10 Yeah, I'm not sure whether they remember, yeah, this time we changed the time.
**Trask Stalnaker** 05:16 Yeah.
Daylight savings is confusing.
Yeah, I just pinged with Mila on… Slack, so… We got a minute.
**Steve Rao** 05:35 Okay.
**Trask Stalnaker** 05:36 But then… If we don't meet today, I won't be sad, because I've been in meetings…
So much today.
So many meetings today.
**Steve Rao** 05:49 Okay, okay.
Yeah, if we have time, today, yeah, maybe, we can also discard a problem about the semantic convention, yeah.
In, in, Java, instrumentation project, yeah, last week, we, I discussed with Laurie. It's about,
Once band, they, connect with several nodes. In that case, we don't know how to collect the server address.
**Trask Stalnaker** 06:35 Yeah, I remember this.
Okay.
Yes, so, my proposal was… If there's only one…
Serv- like, server in the list?
Then go ahead and use that.
If there's more than one server in the list?
Then… leave it empty.
**Steve Rao** 07:03 Oh, okay, yeah.
Okay, makes sense. Yeah.
**Trask Stalnaker** 07:09 And what you could do is…
you could open a semantic invention issue, this was for Redis?
**Steve Rao** 07:20 Yeah.
**Trask Stalnaker** 07:22 Or no, memcached.
**Steve Rao** 07:24 Yeah, memo cache.
**Trask Stalnaker** 07:26 Okay.
So, yeah, we don't… I don't think we have a…
I don't think it's come up before…
like, what to do. If we're capturing a logical span.
And that logical span…
Is… all we know is it might connect to, you know, it may connect… may make multiple calls and may…
Hmm.
Yeah, so with the bulk, and it's memcached, it's a bulk operation, so it's, like, multiple operations, yeah.
Can we capture it at the lower level when it's only sending to one each?
what is it doing? Oh, it's shard… you said it's sharding.
Yeah. So some… some of the stuff goes to one…
**Steve Rao** 08:25 Long span.
**Trask Stalnaker** 08:26 Yeah.
Yeah.
It… It's kind of like the connection string that we used to have for databases.
Which could have, sort of, multiple… and it's doing… you're doing client load balancing, essentially, right?
So… Yeah, but we could introduce a new, like, memcached attribute.
In fact, you could probably even do that in the PR if you want.
If it's important to you to capture all of the servers.
You could have an… and you could just hide it behind an ex… you know, experimental span attribute flag.
**Steve Rao** 09:21 Okay.
**Trask Stalnaker** 09:22 And then you could have… you could set server when it's only one.
And you could always set that experimental attribute to have… List.
And that could be a string array.
**Steve Rao** 09:37 Okay, okay, makes sense.
**Trask Stalnaker** 09:48 Cool. Well, let's… let's call it.
**Steve Rao** 09:53 Okay.
**Trask Stalnaker** 09:54 See you… see you next week.
**Steve Rao** 09:56 See you next week Okay.
**Trask Stalnaker** 09:59 Yay.
