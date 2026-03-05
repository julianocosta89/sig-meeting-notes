SIG: RPC Sem Conv Stability SIG
Date: 2026-03-04
Duration: 44 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 01:49 Hey, you made it! Just to keep all the, noteetakers, note-taker bots company.
**Liudmila Molkova** 01:56 Yeah, I just joined him.
Means 3 bucks.
**Trask Stalnaker** 02:01 worse.
**Liudmila Molkova** 02:03 Yeah, I'm going to keep my camera off, I'm at the airport.
**Trask Stalnaker** 02:07 Sure, sure.
**Steve Rao** 02:30 Hello?
**Trask Stalnaker** 02:32 Hey, Steve.
You prepared an agenda.
**Steve Rao** 02:59 Yeah.
**Trask Stalnaker** 03:01 Alright… Remove client address port.
Yes.
Why was I… hesitating on this. Let me…
**Liudmila Molkova** 03:17 Maybe because of the… the GenA stuff?
**Trask Stalnaker** 03:23 Maybe.
**Liudmila Molkova** 03:25 So my motivation here is because it's just not part of RPC?
It's like, for HTTP, we use X4, Reddit for, right?
And for our PC, it's just, we don't even have… It's normally… we have network, peer address.
That's fine. We keep it. It's just not duplication.
**Trask Stalnaker** 03:51 Right.
Yeah, I think that's fine, and I think that…
It can always be an opt-in thing… Later…
like, I think of, like, again, kind of the gRPC example where maybe you don't capture
an HTTP span, but you do look at the forwarded by, I don't know if you have a
Maybe gRPC is not… The best example, but…
Something working in a unary mode.
We're over HTTP.
one.
**Liudmila Molkova** 04:40 I mean… What I was thinking that, let's say if we connect our PC, we could…
just keep it because… or for double, because they support HTTP as an input.
But for general keys, We remove it. It's the… the convention system. That's a good point.
**Trask Stalnaker** 05:03 Yeah.
Yeah, because, that's a good point, since RPC is not…
general RPC doesn't have to be over HTTP. Yes, okay.
You've convinced me. Thank you.
**Steve Rao** 05:20 Yeah, I have a small question. Yeah, I found that, yeah, the client address, the client, the point, they are stable.
they are stable attributes. We can, delete them directly.
**Liudmila Molkova** 05:37 Well, we can delete them from our PCOS bench.
**Steve Rao** 05:43 Okay, yeah. You mean, for stable attributes, if they are not in metrics, we can, delete them directly?
**Liudmila Molkova** 05:52 But we can… stop referencing them on RPCs, plans, or metrics until
We reached stability for our PC.
**Trask Stalnaker** 06:06 Yeah, so this whole… so this document here…
I mean, I can kind of see the confusion, like, it's release candidate, unless otherwise specified, but this…
Stability… this stability level… I think we've discussed this, Lyudmila, that in the table, it can be confusing.
**Liudmila Molkova** 06:33 Oh, it's not clear the… what it applies to?
**Trask Stalnaker** 06:36 Yeah, that it's attribute level, that the attribute itself is stable when… the… Yeah.
Like, it should almost be a max of…
The attribute stability and the semantic… the span stability.
**Liudmila Molkova** 06:57 Or it makes no sense to show
Attribute stability on spends, because they already have stability, and nothing there should be traded.
higher than… Oh, it's still useful to see if it has lower stability rates.
**Trask Stalnaker** 07:13 Yeah, yeah.
**Liudmila Molkova** 07:15 Yeah.
**Steve Rao** 07:16 Yep.
**Trask Stalnaker** 07:24 But yes, so Steve, we can. It's just not so clear in the… Document.
**Steve Rao** 07:29 Yeah, it's confused for me at the first.
**Liudmila Molkova** 07:32 Thanks for… for noticing.
**Trask Stalnaker** 07:39 Do we want to record RPC status code when an operation has failed?
**Liudmila Molkova** 07:45 It's inspired by the bug, you…
Or the discussion we had somewhere about something else, maybe databases?
**Trask Stalnaker** 07:53 Databases, yeah.
**Liudmila Molkova** 07:55 Yeah, and I thought we have a chance to change it for our PC. I really don't know if we should, but we have a chance.
So the problem… is that we require status quo to show up when it's available, I think?
And… It's… the same as airtight.
So let's say for gRPC, it's required, because it's always available.
So… And if we do, and we also set our type based on it.
So then, as a result, we have… if error happens, we have it twice.
It's granted.
**Trask Stalnaker** 08:53 So, I think the question for me is, are there interesting status codes…
on non-errors. They're interesting non-error status codes.
Because I think that was the problem that I was running into with database.
Semantic conventions, is that…
all that I could capture in the instrumentations, and all that seemed really available or even interesting was there was, like, success.
And then there's… All these different failure error codes.
I… Was having a hard time…
thinking of why I would want to capture these non-error…
status codes, as well as I didn't even have access to them. There were, in the Java drivers, generally, it was, like, in an exception, the status code was conveyed to us.
**Liudmila Molkova** 10:06 Yeah, for gRPC Server, there are plenty of status quoads that are not errors.
I think we'll list only those that are.
But… Yeah, there should be at least a link to the… the gRPC status codes there.
**Trask Stalnaker** 10:27 Yeah, and would that be… Similar to… I'm wondering if there's a server-client situation, like, on a…
**Liudmila Molkova** 10:36 It is, yeah.
But imagine we don't.
It's like… The… imagine we only capture success cases.
We… we can do this. We can say, okay, the… we don't populate if it's the same as error type.
than… I think it's good for… To our application, but…
It means that if I need to, say, let's, group by the status quoad, I need to take two attributes into account.
And all my queries and dashboards become harder.
Or we say, oh, we do it on metrics, we don't do it on metrics, but only on spans, we avoid duplication.
No, they're working.
Come on.
**Trask Stalnaker** 11:37 So let's see, so you've outlined, okay, success case… Status code…
**Liudmila Molkova** 11:44 What's you know?
**Trask Stalnaker** 11:45 Failure key. Okay, success case.
Not an error.
Right, or a type…
Let's see, where can I see the list of all GRPC status codes?
**Liudmila Molkova** 12:23 I think there should be a link in brief, but yeah, if you Google it, we'll find it.
**Trask Stalnaker** 12:35 And so, on the… on the client side, as, like, everything except okay is an error, is that right?
Okay.
And on the server side, it's just that… Smaller list.
Right, not found.
And what about, Steve, remind me again, does…
If Dubbo is not doing gRPC, does it still use, sort of, these same gRPC status codes?
**Steve Rao** 13:40 No.
Yeah, in double, 2… 2-0, yeah. Zhao, it's,
there is a… you can, you can, jump to the semantic convention of double, yeah, with list related…
Status quo.
**Trask Stalnaker** 14:07 Oh, okay, yeah.
**Steve Rao** 14:09 Yeah, yeah, we… yeah, we briefly introduced the case.
Yeah, the, the page, it may be each note,
It's not very clear. You can, you can, you can see in this page, it's okay.
**Trask Stalnaker** 14:31 And the triple protocol error codes are based on gRPC.
**Steve Rao** 14:36 Yeah.
under 4… For Servo, yeah, we,
Elaborate the case when we think there are error.
in 002.
You can… Yeah, GC is a client, client spec.
Yeah, here.
**Trask Stalnaker** 15:07 Right.
**Steve Rao** 15:18 Yeah, I have a small question, yeah, I found, yesterday. I'm not sure in, current Java, instrumentation implementation, in double instrumentation, I can get the, the error like, show in this,
page.
Yeah, maybe sometime I just can get the,
Yeah, maybe runtime exception, and they don't have…
It's a very, specific, error type.
But I'm not very… I don't spend too much time to, to figure out it. Maybe I can do it later, but, I just, yeah.
Point out this point.
**Trask Stalnaker** 16:10 Okay.
And… but presumably, if we… if you ever natively instrumented the double library You could capture it.
So, my… Lyudmila, my initial reaction is it seems confusing to me to split them… split it across the two attributes.
**Liudmila Molkova** 16:55 What do you mean?
**Trask Stalnaker** 16:58 To have… The… some status codes reported here, and some status codes reported… on error type.
So, the success error codes would be on…
the status code.
and error… codes would be on the error type, is that…
Maybe I'm not following…
**Liudmila Molkova** 17:30 Yeah, so this, this is what we could have done.
So… You would find it confusing, and… Is it…
Like, the downside of the current story is… Duplication.
And it sounds like you're… You're fine with it, at least here. It's not in the databases.
Because in databases, nobody cares about the flavor of success, ever.
**Trask Stalnaker** 18:11 Yeah, and we don't… and because we don't have server… I mean, maybe… getting back to it, we don't have server-side instrumentation, so…
We don't… Care about… we don't have that.
aspect, also.
I'm trying to make some parallel, like, that RPC is, like, the status code is a bigger…
deal and baked more in, but I do know that, I mean, status codes are a big deal in databases. I remember when you were doing all that research, and, like, they're… have pages and pages of status codes.
**Liudmila Molkova** 18:55 Yeah, but they are less formalized. I, I kinda…
I, I, I agree with,
Not changing what we have today.
So we can just take this issue of the RPC
And follow up in some other places.
Cool.
**Trask Stalnaker** 19:23 Alright, let's talk prototypes.
Python?
**Liudmila Molkova** 19:31 Yeah, it's still, not… Complete, it's probably 90% complete.
a couple of observations. They didn't have metrics, and I didn't add them yet.
But people were asking for this.
They didn't have message events.
And nobody ever asked for them.
Which is a good signal.
I didn't find any problems.
implementing this. There might be some shenanigans with how… how it's monkey patched.
that, the trickiest part is to find Means to detect, unregistered methods.
Like, when I'm calling something, that doesn't exist.
It's possible… Yeah, but it's…
**Trask Stalnaker** 20:33 to pull in Java, also.
**Liudmila Molkova** 20:35 Right, it seems they fixed it when they've done native instrumentation, but they didn't fix it in Python.
**Trask Stalnaker** 20:41 Okay, yes, yes.
**Liudmila Molkova** 20:45 But yeah, so the only feedback I had is this client address and port that looked redundant and not clear how to get it.
And other than that, it's true, though.
**Trask Stalnaker** 20:59 Alright, alright.
Speaking of the unknown that,
method original stuff, Steve, and the unknown, basically capturing unknown server side spans…
Did you see my comment?
Okay, before I merged here. Yeah, thanks for the double PR.
And then, yeah, if you can look at those two, basically the two… GRPC PRs that I have.
In draft, still.
**Steve Rao** 21:43 yeah, yeah, yeah. I also, list the, agenda today to discard the.
Server address in double…
**Trask Stalnaker** 21:54 Oh, yeah.
**Steve Rao** 21:55 Find a loader balance.
Yeah, so I want to… yeah, when we finish the discussion, and I implement According to the… a solution?
**Trask Stalnaker** 22:15 Sorry, I missed it.
Yeah, can you say that again, Steve?
**Steve Rao** 22:20 Okay, yeah, in, registry, scenarios in Dabo, yeah, maybe,
We will use the interface name, version, and group.
to get the, server address, the IP address from registry.
So, yeah, I think, yeah, maybe in, client side, when, it used the, registry, yeah, maybe we can set the, server the…
Just to the identified name in registry.
**Trask Stalnaker** 23:06 Oh, right, we had started talking about this last week.
So, server address…
**Steve Rao** 23:19 Yeah, this is an identified name in registry.
to map the IP address.
**Trask Stalnaker** 23:28 I see, so you give it, basically, your service name…
And a version of your service.
**Steve Rao** 23:36 Hmm.
I grew up. Group.
**Liudmila Molkova** 23:40 Well, there's nothing we have to do.
**Steve Rao** 23:46 And, yeah, I also get the…
get the, feedback for, for some users, they think the version and group information, they are, they are very necessary for them.
Because if they have a lot of different versions of the same interface name, they want to get a null .
Which version, which group they actually, invoke.
**Liudmila Molkova** 24:17 Do this… are this, like, part of…
The service discovery? Is it, all of this are parameters to the service discovery?
I guess…
**Steve Rao** 24:28 Yeah.
**Liudmila Molkova** 24:28 Could the…
It's like, depending on this survey things…
I would get back a list of IP addresses or something.
**Steve Rao** 24:43 Yeah.
Yeah, maybe, we define the service like ISO in the code snippet.
they can get the IP address from registry.
**Liudmila Molkova** 25:02 is this… this is the client or the server? Because we actually…
**Steve Rao** 25:07 Okay.
**Liudmila Molkova** 25:07 Care about the server address on the client.
**Steve Rao** 25:10 Klein, yeah.
**Liudmila Molkova** 25:11 Okay.
**Matthew Hensley / Grafana Labs** 25:14 Yeah, from what I could, read out of this when I looked earlier, Kind of what was…
proposed here for server address made sense, based on what I saw here. It's like, what the client
In this ecosystem would use to actually identify where it was connecting.
So, I think at least it was internally consistent for Dubbo.
Which… With some of the stuff I've been doing, looking through at WCF, and it's… Incre…
kind of idiosyncrasies, it definitely made sense. Like, this is internally consistent if you're gonna write queries against it.
I think it would…
Yeah, at least what was written here made sense as far as what a client in this ecosystem would need.
And what you would expect is, some of these uses things.
**Liudmila Molkova** 26:08 Nice, and I remember we've seen some things like registry name?
**Steve Rao** 26:13 Is it? Yeah.
**Liudmila Molkova** 26:15 Something else?
**Steve Rao** 26:16 So…
Yeah, go hand.
**Liudmila Molkova** 26:23 Now, I'm just, I'm just curious, I remember we talked, we've seen some examples with registry name.
And maybe some address there. Is it something… Different?
We're…
**Steve Rao** 26:36 I also, yeah, least the advantage of this blind for double. You can scroll down.
Yeah, here.
**Trask Stalnaker** 26:53 Is there some… the one thing that I'm kind of missing here is, like, if there is any…
Official documentation that we can… point to that describe… this…
**Steve Rao** 27:14 Hmm… Oh, okay, yeah, I need to, yeah, source the official documentation.
But, I, I, I list the example.
**Trask Stalnaker** 27:30 Okay, so how do I… what should I look at in this example?
**Steve Rao** 27:34 You can, consumer, you can go to the consumer and,
You can go to the source code.
Yeah, so it's called direct to me.
Yeah.
Oh, Task, Tasker.
Yeah, this is, yeah, use case of, double incline site, yeah.
Value to me.
**Trask Stalnaker** 28:03 Where do I see the, I see… where do I see the registry configuration here?
**Steve Rao** 28:11 In… in, in resource.
In res- in resources.
Yeah, yeah.
**Trask Stalnaker** 28:22 Source, main resources, got it.
**Steve Rao** 28:24 Yeah.
**Trask Stalnaker** 28:27 Okay, so… We've got the… registry address…
And then… internally… Double… Calculates the… that…
server.address key that it sends to the Zookeeper registry based on this.
these pieces. Yeah.
**Steve Rao** 28:55 Yes.
**Liudmila Molkova** 28:58 So this is the code-based abstraction to discover a register address that's used to discover actual IP addresses. Another meta layer.
**Trask Stalnaker** 29:13 And then this NACOS Encodes version group direct intellological service name.
Is this what goes over the wire to… oh, I see, ZooKeeper uses a path based only on the interface, so Zookeeper…
is gonna be, what's the encoded full URL?
**Steve Rao** 29:45 You, you can see the, yeah, description below.
The version and the group are embedded in, Yeah.
**Trask Stalnaker** 29:58 Oh, that's fine.
**Liudmila Molkova** 30:00 I think I understand, so… for…
gRPC, we have, like, the… let's say it's a zookeeper or some other place where the registry leaves, and we record that, plus the path.
Like, every record everything.
And here, if I understand correctly, Steve, we record just the pass within
The registry, but not the registry address.
**Steve Rao** 30:31 Yes.
**Liudmila Molkova** 30:32 Could we record all of it?
**Steve Rao** 30:36 I think in double, I mean, we can do it.
Because, yeah, we can use some instrumentation to get the information. I think it's okay.
**Liudmila Molkova** 30:52 Yeah, it just helps us be consistent, that we record
Like, the same thing everywhere, and it contains all the information that's necessary to discover services.
**Steve Rao** 31:06 Yes.
Yeah, before you.
**Trask Stalnaker** 31:09 Because then it includes the actual registry service server address.
**Steve Rao** 31:14 Right, yes.
Yeah, this way, like, just like a host name in HTTP's memory convention. And, we use the registry to, translate the server address to actual
IP address. So I think this way is an, is a more natural way, compared to, compared to the, other solution.
And, another disappoint of, if we record the registry address in double, they support multiple,
register, So, it's very hard to, distinct with,
With the registry, address.
It's, it's, Cracked for this, invocation.
**Trask Stalnaker** 32:10 So let's take this one…
Would the… so this is the zookeeper… URL… Would it be… This… slash…
this… And then the query string…
Would it be something like this?
Is this what is actually, like, Is this the URL?
That you send to Zookeeper, and Zookeeper sends you back.
an IP address?
**Steve Rao** 33:01 But in double case, yeah, I can share a link.
The, the scenarios, is, complicated.
Sometime, we don't easy to get the, correct, registry address.
**Liudmila Molkova** 33:30 Is it, like, the… the… sometimes it's not configured, or…
Is it…
**Steve Rao** 33:38 Because, user will, config, multiple, registry address, because, double supports multiple, registry.
**Liudmila Molkova** 33:50 how would, then, it decide which one to pick? It still picks one, right? Or is it round-robin?
**Steve Rao** 33:59 No, yeah, sometime, yeah, maybe it will combat, different IP address from, to a registry.
**Trask Stalnaker** 34:14 So is it, like, a comma-separated list of… Zookeeper addresses…
**Steve Rao** 34:22 Mmm…
**Trask Stalnaker** 34:40 Let me see what we did on the,
gRPC… I wanted to look at that gRPC Zookeeper example.
Okay, right, we have target string, sometimes that's comma delimited, which is fine, we just use the comma delimited.
**Steve Rao** 35:09 Yeah, I, I, yeah, I sent a link.
Being over top.
**Trask Stalnaker** 35:26 So, in this case, is it gonna ping both of these and just aggregate them?
**Steve Rao** 35:36 Yeah.
And for some time, there are some configuration, they can control which registry we record, we get the IP address. You can scroll down.
It's awesome.
Yeah, so if we, yeah, add the register…
**Trask Stalnaker** 35:56 quality.
**Steve Rao** 35:56 I think it will make the things become more complicated.
**Trask Stalnaker** 36:05 Sort of, but this also makes… brings it back to just the single case, which would…
**Steve Rao** 36:18 You can scroll down, and…
And,
There are a lot of different use cases.
**Trask Stalnaker** 36:38 Yeah, so like this, right, an option is just to store this whole thing…
I guess the problem is that this isn't all of it, this is just the registry address, and then…
Beyond that, you also have… A pass that you hit on… at that registry?
**Steve Rao** 37:10 Hmm…
Yeah, I, I want to, yeah, I have a, another opinion. If we, being HTTP client.
If we, record the host name in server address, we don't, get the DNS address.
Yeah, maybe we can,
compare with the HTTP scenario, semantic convention. In HTTP semantic convention, we just captured the host name.
**Liudmila Molkova** 37:50 It's different because there, there's just one host name, right? There is no service discovery.
And no… no complexity that we have here.
**Steve Rao** 38:02 I think the registry, just like the DNAs, to translate the host name to the IP address.
**Liudmila Molkova** 38:16 To a certain extent, yes, but… Like, imagine you…
Or connect your… your services are talking, and you want to break down
Who… you want to know who your client talks to.
Yeah. And which… Which registry was chosen, which… How it was resolved.
And maybe the answer is… for…
For double, we record, I don't know, a thing called registry.
dot address would… I don't know. Or maybe we record double.group.
independently.
Maybe server address.
not super applicable, I don't know.
**Steve Rao** 39:14 Yeah, you mean that the registry, information is necessary in RPC scenarios?
**Liudmila Molkova** 39:24 Oh, sorry, I'm in the airport. Can you repeat, please? Sorry.
**Steve Rao** 39:28 You mean the registry information, is, is important in RPC scenarios?
**Liudmila Molkova** 39:38 It's just generally important to know who you called, where they live.
Race.
**Steve Rao** 39:48 Mmm…
**Liudmila Molkova** 39:49 And that's the only way we know.
like, we record IP address, but it's…
**Steve Rao** 39:58 Stu criteria.
**Liudmila Molkova** 39:58 Originology and not useful.
**Steve Rao** 40:00 Yeah, I also have, yeah, in bubble case, sometimes, yeah, when the client, records the server, they don't, record
the… address from registry. They get the registry, informed by registry.
And, in Babel client-side, there is a cache.
that is a cache. They can, store, the IP address from registry. Yeah, maybe, if I remember right, maybe, 30 seconds per time.
And, when the client side recalled the,
server side, they can get the IP address from the cache. So, when, the invocation happened, they don't have communicate with the registry.
**Liudmila Molkova** 41:03 Oh yeah, absolutely. But, like… The goal… Even it would be cached.
But…
it would still appear unspan so that you know who you called. You can say, okay, show me the latency per this group of
Things.
**Trask Stalnaker** 41:30 Yeah, so the thing that I like about where GRPC landed is that…
Because server address is the… we've defined it in semantic conventions as the logical address of the server, so if you have, like, a cluster of a bunch of things, that's…
Just, you just have one, you know, server.address, and that represents the whole cluster.
and… So, in gRPC now, with this, this is basically one… string that… Tells you, unequivocally.
Who… what the… what server you talked to.
what logical server? It's like a… it is DNS. It's basically, essentially, you know, this is DNS, this is the name.
And this is the DNF server that got looked up into an IP address.
And so, I think… What would help for next time, Steve, is if you could… you know.
Work… try to go through, you know, all these complicated examples.
And… Share, you know, what… What would it look like if we tried to coalesce?
All that complexity into one string?
And… So that at least we can see what that would look like if we did
You know, try to push You know, force it into that, path.
And, you know, maybe we look at it, and it's just super horrendous, and, you know, it's gonna be more confusing than it's worth. And then, you know, maybe we think more about splitting out… splitting things out into double-specific, double registry-specific.
attributes, and… Not capturing server address at all.
In that case.
**Steve Rao** 43:46 Yeah, maybe I can do more research next week.
And maybe we can discard next week.
**Trask Stalnaker** 43:55 Cool.
**Liudmila Molkova** 44:01 Awesome.
**Trask Stalnaker** 44:01 Alright.
**Liudmila Molkova** 44:02 Thank y'all.
**Trask Stalnaker** 44:03 Yeah, thank you.
See you next time.
**Liudmila Molkova** 44:08 See you, bye.
