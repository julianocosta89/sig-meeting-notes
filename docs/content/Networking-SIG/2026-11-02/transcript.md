SIG: Networking SIG
Date: 2026-11-02
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**RC Rob Cowart** 01:29 8.
**Sven Cowart (ElastiFlow Inc)** 01:30 Yeah, there.
**Antonio Martinez (Cisco Systems, Inc.)** 01:32 Hey, everyone.
**Sven Cowart (ElastiFlow Inc)** 01:36 How'd your talk go internally?
**Antonio Martinez (Cisco Systems, Inc.)** 01:41 Correct?
**Sven Cowart (ElastiFlow Inc)** 01:42 The presentation you're giving at KubeCon, didn't you say last time you were doing it internally?
**Antonio Martinez (Cisco Systems, Inc.)** 01:47 Yeah, it was fun. It was, it was good. People liked it, people wanted to extend it, a little more use cases, so yeah.
Are you nugget? Awesome Not about you. How are you doing with the preparation of the booth?
Or the conquering.
**Sven Cowart (ElastiFlow Inc)** 02:04 killing myself.
We'll be down there.
**Antonio Martinez (Cisco Systems, Inc.)** 02:13 Thank you, man.
**Sven Cowart (ElastiFlow Inc)** 02:13 I'll send that when we get there, so you can find me, but yeah, that's why you'll find out why I've been killing myself.
**Antonio Martinez (Cisco Systems, Inc.)** 02:20 Is it? Okay.
**Sven Cowart (ElastiFlow Inc)** 02:24 Hey, Braydon.
**Braydon Kains (Google LLC)** 02:25 Morning.
**Antonio Martinez (Cisco Systems, Inc.)** 02:27 Sir.
**Sven Cowart (ElastiFlow Inc)** 02:28 Completely unrelated to this SIG. Antonio, I read in TLDR this morning, Cisco.
Hired someone to give them unlimited AI tokens to rewrite 98% of their legacy code. It's like.
**Antonio Martinez (Cisco Systems, Inc.)** 02:41 Yep.
We're not the same, we're not the same. I will ask also my manager about that.
Oh, man. I don't know if those are rumors, or… If that's something happening, I don't have idea.
**RC Rob Cowart** 02:58 Good luck with that.
**Antonio Martinez (Cisco Systems, Inc.)** 03:01 Yeah, not ideal.
Okay… So it's good that we have prop today, we didn't have a few meetings, so yeah, maybe we can resume some of the SNMP meetings, I mean, discussions.
**RC Rob Cowart** 03:17 Yeah, y'all will have me more regularly again. I just had a ton of stuff, also personal life going on that was just killing me, so… But yeah.
Like, my background is all different, because I had to move and stuff, too, so, you know, that's always fun.
**Antonio Martinez (Cisco Systems, Inc.)** 03:34 Okay. Anyway. Good luck… good luck with the new place.
**RC Rob Cowart** 03:39 Yeah, honestly, I like the old place better, but our landlord sold it, so… or was selling it, so, you know, what can you do, you know?
**Antonio Martinez (Cisco Systems, Inc.)** 03:48 Hey, man, whoa.
Okay, I don't know if more people will join, but maybe we can get started. Quick note there, all those three metrics got merged, so we are doing some progress. Christopher and Lyudmila, who were on Trust were quite helpful there, merging it.
So, thank you for that.
coming back, some talk is from myself. Braydon said that document, I don't know if you had a chance, but those are, like, the available slots, and we agreed that Tuesday was a day with some talks, so maybe Wednesday would be a better timing, and then we created that.
pool, and those are the days, so should we go with the first… first one?
Maybe?
**Sven Cowart (ElastiFlow Inc)** 04:40 Works for me.
**Antonio Martinez (Cisco Systems, Inc.)** 04:42 How does it work, Braydon? Do you know if we can just put here Network SIG, or is it something because no one has done it, so…
**Braydon Kains (Google LLC)** 04:50 Pretty sure we can just… we can just put it in.
If we have to start negotiating times with people, we can, but I think, as far as I know, we can just kind of put our name in there. Just say, this is a networking slot, because no one else is claiming it. It's been open for a couple days, so… I think we can just do it.
**Antonio Martinez (Cisco Systems, Inc.)** 05:12 Thank you for that. And moving on… I don't know if you guys remember, but we got attention with that pull request that was about the DNS lookup time, and then we have the question name, if that was optional, if that was recommended, and so on and so forth. I mind that the owner of the pull request also got attention on something else, so I think you also have here a blocker, so I don't know if we want to resume that pull request and have I wanted to see that metric as recommended. What's… what was the latest, the latest.
**Sven Cowart (ElastiFlow Inc)** 05:45 If you go… If you go to the,
**Braydon Kains (Google LLC)** 05:47 Mostly happened on the issue attached.
**Sven Cowart (ElastiFlow Inc)** 05:49 Yeah.
**Antonio Martinez (Cisco Systems, Inc.)** 05:52 What was that, sorry?
**Braydon Kains (Google LLC)** 05:53 Like, philosophical things about semantic conventions in general.
So it's a long… it's a long one, but I think we did settle on basically what Sven's blocking comment said.
**Antonio Martinez (Cisco Systems, Inc.)** 06:07 That one, right?
**Sven Cowart (ElastiFlow Inc)** 06:08 Yep. Yep. I think there was… in the issue, there was still a little bit of an open-endedness to should the metric itself be opt-in or recommended, because the value of it is hard to… there's… It's difficult to get value from it.
**Antonio Martinez (Cisco Systems, Inc.)** 06:25 If you dismiss him, yeah.
**Braydon Kains (Google LLC)** 06:26 There's… there's something… something we didn't, like, talk about in that discussion for recommended versus not, is that, like, I think that between Sven and I, and Sven asking some… some other engineers at the company, as far as I remember, we determined that, like, there are times when the metric can be useful in this sort of, like.
question name opt-in type of scenario, like, there is a use for it, but something I didn't say is that, like, whether we call that recommended or not blanket is actually very difficult to say, because do we actually recommend this metric with the attribute opt-in all the time? Probably only in these specific scenarios where we've determined it's useful, so should we say it's recommended blanket because of that? I actually… I don't know where I land on that. I… I lean more… not, where I say opt in, and, like.
We recommend this in a scenario where… or, like, even explaining on the attribute, like, the attribute… like… we'll say… You can… you can leave this off, and metric is… the metric it's on is still useful in certain ways.
Yeah, this is… getting tricky. It's probably something we're gonna run into a lot, where the specific metrics have very different uses and levels of recommendation, depending on the environment, and they're being used.
So I don't know how to handle that going forward, necessarily.
**Sven Cowart (ElastiFlow Inc)** 07:53 I'm with you on that. The reason I think this actually ends up being opt-in is if you go to the issue, Rob's last comment, I think, on this particular one is really important, because it takes it a little bit out of the… Philosophical realm?
And into, go to the top, and the description has the…
**Braydon Kains (Google LLC)** 08:13 Topics could be a linked issue.
**Sven Cowart (ElastiFlow Inc)** 08:15 Yeah, fixes.
**Braydon Kains (Google LLC)** 08:16 Fixes 3839 up at the top of the description.
**Sven Cowart (ElastiFlow Inc)** 08:20 Yeah, they're…
**Antonio Martinez (Cisco Systems, Inc.)** 08:22 Based on the pull request, okay.
**Sven Cowart (ElastiFlow Inc)** 08:25 Well, Rob basically points out, and this is very valid on this particular one, is that because of DNS caching, what does this actually tell someone?
after the DNS record is cached, your responses get much quicker.
And consumer.
**Braydon Kains (Google LLC)** 08:43 I did not see this comment, sorry, I lost track.
**Sven Cowart (ElastiFlow Inc)** 08:46 Here go down.
**Braydon Kains (Google LLC)** 08:47 issue.
**Sven Cowart (ElastiFlow Inc)** 08:47 I did too, actually.
**Braydon Kains (Google LLC)** 08:50 Reading it now.
Okay, I… I think that actually does… Help a lot for me to lean more metric opt-in, too.
**Sven Cowart (ElastiFlow Inc)** 09:13 Yeah.
**Braydon Kains (Google LLC)** 09:14 I think if we have to put these many caveats on, like, here's how the metric is useful, but be careful not to misinterpret it in this way because of XYZ problem, like, I think already we're into, like.
We shouldn't recommend the metric blanket if we're already having these types of discussions.
**Sven Cowart (ElastiFlow Inc)** 09:31 Yeah.
And I do think this brings up a really good point. It's like, you're testing… this metric will report on… the speed of the DNS cache.
Chuck, does anyone care about that? I'm not sure. Maybe, but… Yeah.
**Braydon Kains (Google LLC)** 09:47 It's one of those ones where the metro this.
**RC Rob Cowart** 09:50 I think you still care about the latency of the lookup in general.
**Sven Cowart (ElastiFlow Inc)** 09:55 Yeah, yeah, yeah.
**RC Rob Cowart** 09:56 whether it comes from the cache or not, what I just want… to me, it's just like, some people go, well, my DNS server is fast or slow. Well, maybe not, maybe, maybe not.
**Sven Cowart (ElastiFlow Inc)** 10:06 Yeah, yeah.
**RC Rob Cowart** 10:07 Or, like…
**Sven Cowart (ElastiFlow Inc)** 10:08 This gets to the point exactly what Braydon, I think, was just getting at. It's like, this is recommended if you're doing synthetic testing and you can guarantee you're not hitting the cache.
then it's a good idea. But if you're hitting the cache, then, well, maybe, maybe you care, maybe you don't.
**RC Rob Cowart** 10:23 I think you still care, you just care about it differently.
**Sven Cowart (ElastiFlow Inc)** 10:27 Yeah.
**Antonio Martinez (Cisco Systems, Inc.)** 10:27 Correct.
**RC Rob Cowart** 10:28 It has to be heavily loaded, like, like under a heavy load, that still causes the problem, even though it is touched, right? So, you still kind of care, I just think, like, you're just not measuring the same thing anymore.
You know, the same entity is not being managed anymore.
Once it's cached.
**Sven Cowart (ElastiFlow Inc)** 10:48 Yep.
**Antonio Martinez (Cisco Systems, Inc.)** 10:57 Okay, so, how should we talk about?
**Sven Cowart (ElastiFlow Inc)** 10:59 I'll update my comment.
I think this…
**Antonio Martinez (Cisco Systems, Inc.)** 11:03 Anyone question?
**Sven Cowart (ElastiFlow Inc)** 11:04 Yeah, I'll update…
**Antonio Martinez (Cisco Systems, Inc.)** 11:05 uncommon.
**Sven Cowart (ElastiFlow Inc)** 11:05 and remove the… well, I guess I still need to do… opt-in, because the metric itself, I think, is what we're saying should change to opt-in.
**RC Rob Cowart** 11:14 I have another question real quick, because I had not… when I answered that other thing, I didn't look at this as much. Are these attribute or metric names already… already…
**Sven Cowart (ElastiFlow Inc)** 11:26 They're under development. They're already published as developmental.
**RC Rob Cowart** 11:30 Okay, I just don't like the name lookup.
I… you know, I would argue DNS is a request-response protocol, but in DNS terms, if anything, it's… it's an… it's an answer. So if I'm going to use question name, then I feel like it's… it's answer duration.
More so than lookup duration?
**Sven Cowart (ElastiFlow Inc)** 11:59 Hmm.
**RC Rob Cowart** 12:00 Like, and I guess there's probably a little bit of a question of, is this a, in which way do we want to have… is the goal to have similar terminology across multiple protocols? Like, request response is pretty generic, you know? But… or to which way is it proto… like, be true to the protocol? In which case.
if you look at all, like, the RFCs and stuff for DNS, and even what the fields are called that are… the correct word would be answer.
So it would be DNS answer duration, which matches, actually, the fact that, like, DNS question name. You know, so question answer as opposed to request response. So, like, I just feel it weird that one is called question, and then the other one's not called answer.
**Antonio Martinez (Cisco Systems, Inc.)** 12:56 I see totally your point, I like it too, yeah.
We're in a good timing for making that improvement, honestly.
**RC Rob Cowart** 13:01 Okay.
**Sven Cowart (ElastiFlow Inc)** 13:02 Doesn't DNS look up duration, though?
If you say… that's saying both sides of it. Like, starting with a request, how long does it take to get a response? DNS answer duration could be interpreted as just.
**RC Rob Cowart** 13:17 just inside the DNS server.
**Sven Cowart (ElastiFlow Inc)** 13:18 The response, yeah.
**RC Rob Cowart** 13:20 That's maybe fair, but, yeah.
Look, I'm not gonna die on the field either way, you know?
**Sven Cowart (ElastiFlow Inc)** 13:33 I'm not either, I was just thinking of…
**RC Rob Cowart** 13:35 I just… it just hit me when it's like, why do you say question and not then answer on the other one then? Because, you know… I haven't checked, Sven our old internal schema codecs, and we called it also answer. We actually called a query an answer, but that's a sort of question, but yeah.
**Antonio Martinez (Cisco Systems, Inc.)** 13:58 I don't have a quick comment here. You guys were mentioning that we should change it to opt. It's already opt, right? The metric might change. It's already.
**RC Rob Cowart** 14:07 Yep.
**Sven Cowart (ElastiFlow Inc)** 14:10 Okay, so it stays as opt-in.
**Antonio Martinez (Cisco Systems, Inc.)** 14:14 Correct.
**Sven Cowart (ElastiFlow Inc)** 14:15 I think that PR wanted to change it to recommended.
**Antonio Martinez (Cisco Systems, Inc.)** 14:19 Mmm.
**Braydon Kains (Google LLC)** 14:21 if it was that the PR wanted to, or if it was Lyudmila suggesting as such.
Bye.
I can't recall, but I do remember part of the discussion was… That this attribute is high cardinality, and as a result, we shouldn't… Have a recommended Recommended metric and recommended attribute that would result in high cardinality, scenarios… Yeah. And there's a lot of nuance to that discussion, where it's like, There… to some degree, we're… Protecting backends that can't handle this well, and like, isn't that the backend's fault?
But at the same time, there's some client-side, like, user-facing concerns for tracking high cardinality metrics sometimes, so… In the end, we still try and… Protect our default recommendation conventions against that, but… we note where necessary… like, we are fully allowed as a SIG to note, if you don't turn this on, the metric isn't nearly as useful, but it's opt-in because of the cardinality problem. Like, I think… we're allowed to say that. They can't… they can't tell us not to say that.
**Sven Cowart (ElastiFlow Inc)** 15:36 Yep.
**Antonio Martinez (Cisco Systems, Inc.)** 15:40 So I will pin the owner of the request to see if he can take a look at the latest comment, so we can progress there.
**Sven Cowart (ElastiFlow Inc)** 15:47 And I'll make a comment to Antonio right after this call, so that…
**Antonio Martinez (Cisco Systems, Inc.)** 15:51 Bet.
**Sven Cowart (ElastiFlow Inc)** 15:51 to do.
**Antonio Martinez (Cisco Systems, Inc.)** 15:51 liquid.
**Sven Cowart (ElastiFlow Inc)** 15:52 Yeah.
**Antonio Martinez (Cisco Systems, Inc.)** 15:54 That would be awesome. I mentioned in the chat we have to put requests for the support of SNMP traps logs in the OTL collector… on trip.
Please take a look whenever you find time. Actually, it's one, the other is more like a simulation, An example pull request, so this is the good one.
And those were my comments, but in the last meeting, we were talking about syncing with Drop to create the GitHub, so I don't know if you have a chance. I imagine you had a pretty busy week as well, so… Couldn't find the time, but… I am… I am seeing more and more often.
**RC Rob Cowart** 16:33 Oh, that… no, so I was actually about to say, like, that… I'm gonna get that out this week, if not in the next day or two.
Because now, as I'm circling.
Coming back to this stuff, and also has some internal projects associated with it, so,
**Antonio Martinez (Cisco Systems, Inc.)** 16:49 Awesome, awesome.
**RC Rob Cowart** 16:51 Yeah, and I still have the feedback that I got previously.
Even around, like, May.
Yeah, like, making…
**Antonio Martinez (Cisco Systems, Inc.)** 17:00 Peter, by the way.
**RC Rob Cowart** 17:01 ingress, egress, or in-out, an attribute, and what have you. So, the only thing I was still… I didn't really remember where we landed, and… and the more I think about it, I'm still not sure what to… How we handle is… We had the conversation about by bytes being… is the units, but it's also kind of the name of the metric as well.
**Antonio Martinez (Cisco Systems, Inc.)** 17:30 Correct, but all those things we can discuss once we create a GitHub issue on a pull request, the same that we are discussing the DNS one, I guess. Byte is usually the unit that we are using on HTTP metrics today, bytes, or bytes per second, so I think we should try to be… as close as possible, I would suggest.
**Braydon Kains (Google LLC)** 17:52 But the question.
**Antonio Martinez (Cisco Systems, Inc.)** 17:53 So, yeah, that was…
**Braydon Kains (Google LLC)** 17:53 whites should be in the name or not? Is that…
**Sven Cowart (ElastiFlow Inc)** 17:55 Yes.
**Antonio Martinez (Cisco Systems, Inc.)** 17:57 And in the unit.
**Braydon Kains (Google LLC)** 18:00 Yeah, I think typically, like, historically, there's a lot of metrics that have the word bites or something in them, and I think that's… Historical, since in the past the unit wasn't, like.
Fully conveyed as part of, like, the conventions or anything.
Now that it is, we try and lean Not that direction, so take the word bites out of.
**RC Rob Cowart** 18:24 Yeah.
**Braydon Kains (Google LLC)** 18:24 the name.
**RC Rob Cowart** 18:26 Understood. It was just kind of like, okay, then what do you call it?
**Sven Cowart (ElastiFlow Inc)** 18:30 Yeah, exactly, that's…
**Braydon Kains (Google LLC)** 18:31 Well, yeah, that does.
**RC Rob Cowart** 18:32 Absolutely, it bites in and bites out of the interface is the raw underlying value, right? So, like, so what do you call it?
**Antonio Martinez (Cisco Systems, Inc.)** 18:43 But I think we also initiate that conversation, we said that it's going to be something like Networking Interface I.O.
**RC Rob Cowart** 18:49 Yeah, I.O. was, I think, the one suggestion that was maybe in, you know…
**Braydon Kains (Google LLC)** 18:54 I think that's what… that's what DISC does, and in the system network metric, we call it system.network.io. I don't remember how that links up with the network.
**RC Rob Cowart** 19:04 We should probably try to be consistent, yeah.
**Antonio Martinez (Cisco Systems, Inc.)** 19:08 I mean, we don't. We don't have to be consistent there, because those things are kind of… not standardized, and not that word used, and have, like, legacy mistakes, let's call it, but honestly, network.interface.io, I mean, they use a good name in there, in my opinion, but for the other, like, putting counts, or the others might not be the best.
**Braydon Kains (Google LLC)** 19:31 This metric did sort of go through the, like, semantic conventionizing So to speak. You know, it started out as there used to be two metrics. It was system.network.bytes.in and bytes.out, I think?
And so we standardize it down to I.O. with the direction attribute.
So, at least this one's.
**RC Rob Cowart** 19:52 the feedback they gave me on my initial draft of that document, also, was the in and out To be a direction attribute, yeah.
**Braydon Kains (Google LLC)** 20:02 Now, to… to the devil's advocate a little bit, something I try and, like… the drum I'm always banging in system is that, like, sometimes the semantic convention's rules are taking us away from you know, actually, like, naming in a way that matches what we're measuring. Like, the… the… if the common verbiage and, like, the… the… what… what the kernel or what the interfaces are giving you, like, if it's called bytes.
And that's the name that everyone who's used to measuring these things always knows, then is it really so bad that we break a semantic conventions rule so that we can at least, like, properly reflect what we're measuring in a way that many people, like.
agree upon already. I think that we're in a kind of a weird state where network and system They kind of have this… This same problem where there's so many monitoring solutions, and there have been basically since the inception of you know.
network in OSes, like, they… it's built in, and people have come up with so many different ways of doing it that it's a very old practice, and for us to try and, like.
enforce all new rules that go, like, super against the grain just to match what semantic conventions wants doesn't make a lot of sense a lot of the time, so I think if we Feel like we should break one of those rules because we're… like… aligning with an established practice or understanding, I think… I think it should be fine.
Personally. We might have to fight a little bit with maintainers sometimes, though.
**RC Rob Cowart** 21:36 That, that's… that's fair. If we… So, just in this specific one, actually, the two counters in SNMP World, and other things named them similar to SNMP World, are… If in octets, and if out octets.
**Braydon Kains (Google LLC)** 21:56 Hmm.
**RC Rob Cowart** 21:57 see that a lot of places, it doesn't… bytes are called octets, so… but I wouldn't want to name this octets either, quite frankly, because I think that would confuse anyone who's not a… really in the weeds in network, you know?
For me, I actually… thinking broader industry here, I think there's another motivation for, you know, making sure we just have something that That works really well, first and foremost, whether it leans on legacy naming heavily or not, is that, not knowing how much you're aware of it, but… In the network world, for the last decade.
you know, actually, I've been hearing for the last 25 years, SNMPs did. It's gonna be this thing that replaces it, and it never does. But the first thing that, like, where you thought, like, okay, this could replace it, was streaming telemetry, and you'll hear this talked about streaming telemetry, and do you support streaming telemetry, and whatever.
But the problem is, is that freaking streaming telemetry has… the adoption has been very slow. And the reason its adoption, in my opinion, has been very slow is, unlike SNMP, There are no standards for it.
you know, like you see here, like, the GNMI stuff, some people just send a bunch of JSON. Like, F5, it's all JSON payloads pushing.
you… shoot, Cisco has 3 different versions of streaming telemetry across their… across just their, like, iOS-based products, you know, or XI… XE iOS, or whatever the iOS XE, whatever the different versions are.
And so… So there's literally been, like, no standardization whatsoever. There is a part of me… that hopes.
That once there's a really good standard for all of these different types of information network devices can push, that there will be, hopefully.
with any luck, I don't know, maybe like the Sonic project or something, hey, push streaming telemetry with OTEP! You know, and maybe we can start to have a bit of a standard around that streaming telemet… vendors implementing streaming telemetry can actually implement.
And be able to send this native. And that's kind of, you know, when I think, like, what's your big dream for this? Well, that would be one of the problems I'd love to solve in the industry, is streaming telemetry. When people say that in 10 years from now, they'll just mean, oh yeah, hotel semantic conventions, that's what they're talking about, you know.
**Antonio Martinez (Cisco Systems, Inc.)** 24:40 Good for being here.
Then, for sure, a good starting point will be to… to put some somatic convention over those, because from what you mentioned, the time that we were reviewing those, those were, like, the main SNMP metrics, isn't it?
They run down the earth right here.
**RC Rob Cowart** 25:00 I mean, a lot of people streaming telemetry data still leans on the same things, because as it is with SNMP, I don't know if y'all have ever been on any of these type of Things before, but, like, you know, implementing certain… some of these IETF standards and stuff, especially in networking, what ultimately ends up happening is some of them are not done in code. They're implemented in silicon.
And so, you know, just because now I magically have you know, I might have implemented these counters for network interfaces in silicon. Well, just because I now support streaming telemetry doesn't make that underlying data in the silicon any different than what it is, right? So, the… the limit… the streaming telemetry still leans heavily on the SNMP data, you know.
**Antonio Martinez (Cisco Systems, Inc.)** 25:50 Alright.
**RC Rob Cowart** 25:50 I mean, even if you look at, like, the Linux, what are the… not the prox… is it the prox file system? You know, where they… the kernel stores a lot of its stuff, right? Yeah. And it's also a name like the SNMP stuff is, like, you know, they didn't reinvent the wheel when they did network metrics, so…
**Antonio Martinez (Cisco Systems, Inc.)** 26:11 My favorite parts.
**Braydon Kains (Google LLC)** 26:13 Something that… It might be interesting for us to… to… I'm trying to find it. So, in… in… The system group.
I ended up writing a… Design doc, basically.
That explained how we consider different different types of conventions, and how strictly we adhere to certain rules in different ways, and I ended up separating them into, like, two classes of metrics, or instrumentation, whatever you want to call it.
class… the main class, Class A, would be, like, metrics that we recommend by default, that might generally be cross-platform, that need to be easily understood by anybody who might look at a dashboard.
And in those cases, we name things Generically, in a way that, like, via our expertise, we think makes sense and would… align with other semantic conventions. And then we have a sort of second bucket or class, which we call, like, specialist metrics, where we essentially introduce conventions for things that people who, like, really know what Linux is. Like, they're looking for these specific metrics, and they know the exact names and terminology that they're looking for, they just want the hotel version of that. We have that kind of second class of metrics, and for those, you know, we don't consider the semantic conventions rules For naming as closely as we just want to, like, give the specialists what they want.
So I think… we can sort of make the same distinction. Maybe Network Interface Bytes is a good one, where We… we think that the specialist ver… like, we think this is a generic metric that everyone wants to use, and as a result, we should name it in a way that we feel makes the most sense, not necessarily based on what it's named internally, but in, like, the information that we want to convey, what's the right way to name this, and so I.O. might be a good name for it. But if there was… something super specific that, like, the… only the specialists who really know what they're looking at would really care about, that we would call opt-in, like, if you know you want this, this is… you can enable this, and this is what the convention is. And in those cases, we… Veer more towards, like, what the established naming practice is.
**RC Rob Cowart** 28:39 That's kind of interesting, actually. And by the way, if you… if there was a link to that, I'd love to see that.
**Braydon Kains (Google LLC)** 28:46 Let me try and find it. It's in the semantic conventions repo, I wrote it out.
**RC Rob Cowart** 28:50 The… the way I discussed this similarly in the past, when I have done schema-type stuff in past companies I've worked for, I came up with this model of A core common custom.
cores, like… like, CPU utilization. 99.9% of things that tell you about CPU tell you CPU utilization. But then, like.
Context switches per second on a core.
Okay, like… It's common… But not, like… everybody has it, you know? So, we may still normalize… this was the back then, you know, like, we may still normalize that to some common naming, but, like, we didn't have a ton of out-of-the-box functionality around it, you know? Like, the core stuff. And then custom is, like.
Well, you know, Cisco has their… supports this one standard, and then they made their own special flavor of it that has these three other metrics, you know? And it's like… and so they're the only one in the world that has them.
What do you… we don't even worry about normalizing that, because… and that's what… we are going to get into this at some point, this'll happen, where it's like… Does it even make sense to make… a metric name beyond Cisco underscore whatever they call it, because They're the only one that has it, because it's their own special secret sauce version of it. But, if you're a customer, and you just paid for the Cisco Secret Sauce version, well, you certainly want to monitor the secret sauce, right? So… you still want the data, but… and you kind of have that stuff all over a network. So… and I kind of think of those as what you're talking about, like, these are maybe the guru values that not very many people care about, or maybe even not that many people implement, but we need to be able to handle them in some way, so…
**Braydon Kains (Google LLC)** 30:57 Yeah, that's a… that's a good way of putting it. I never… really thought of that way, but I quite like that, actually. And the… this… this document that I wrote was a year and a half, maybe two years old, so, you know, we've… I've been through the semantic conventions Process a little longer now, and it could be… rewritten in a way that makes more sense, and I like that, the core, common, custom framing of it. I would be… open to… like, reframing the way I initially wrote it to… to be more like that, because I think it is a… it's a bit easier to understand than what I had written originally, but… Take a look through the…
**RC Rob Cowart** 31:40 There's logic.
**Braydon Kains (Google LLC)** 31:41 Yeah. See… what makes sense. I'm… this one is specific to system, but I think other groups have, like, referenced this doc and wanted to, like.
kind of follow the same framing. I think the maintainers were a fan of it when I first wrote it. So, if we wanted to reframe this and then write it in a way that, like, could go generally into semantic conventions guidance for people to follow, I think that would be… A useful… a worthwhile endeavor, let's put it that way.
**RC Rob Cowart** 32:13 Okay, yeah, no, thanks, that's helpful.
**Antonio Martinez (Cisco Systems, Inc.)** 32:19 Boom.
So, is there any topic from… from you guys that you want to bring up today?
**Braydon Kains (Google LLC)** 32:31 I don't.
**RC Rob Cowart** 32:31 Hope you'll have a good time next week at KubeCon.
Does that mean there's.
**Antonio Martinez (Cisco Systems, Inc.)** 32:34 No.
**RC Rob Cowart** 32:35 Next week, because everyone's gonna be… at or traveling to KubeCon?
**Braydon Kains (Google LLC)** 32:39 Yeah, I guess all three of us are gonna be there, so…
**Antonio Martinez (Cisco Systems, Inc.)** 32:42 Yeah.
**Braydon Kains (Google LLC)** 32:44 Probably will skip the call, maybe we'll put something in the… in the network chat.
To say it.
**Antonio Martinez (Cisco Systems, Inc.)** 32:49 Don't do that.
**Braydon Kains (Google LLC)** 32:50 such.
**Antonio Martinez (Cisco Systems, Inc.)** 32:51 Yeah, formatting. And do we want to have, like, a… Would that be that Syncat that we are gonna do, like, that friendly, or do we want to have some sort of a… points to discuss, like, I was thinking maybe, Ben, you mentioned, like, discussing the SNMP receiver.
**Sven Cowart (ElastiFlow Inc)** 33:11 That's weird.
Jim.
**Antonio Martinez (Cisco Systems, Inc.)** 33:12 roadmap?
**Sven Cowart (ElastiFlow Inc)** 33:14 Yeah, you can try that, yeah. I like that idea. It might take more than 50 minutes, but…
**Braydon Kains (Google LLC)** 33:21 Well, yeah. But I think leveraging that in-person time for, like, broader directional discussions is a good use of time. Like, in my experience, those types of… of discussions happening in person at the convention is useful. So, any, like.
broader directional topics about the Networking SIG in general.
Would be a good thing to… to… Good discussion to have there in person.
**RC Rob Cowart** 33:47 Does it make sense?
to try to sync up in any way, also, with folks from the entity SIG?
And I say this because, So, one of our goals that we have, and we were actually discussing about whether this is another Something that we could contribute, like, into the collector or elsewhere is, a topology discovery process.
And… and you're gonna have there things like, you know, This VLAN is tagged on this inter… like, and so, is tagged, or something, is a type of relationship. I think they're looking, actually, to… for some good examples.
Or some good understanding of different domains of how entities and relationships, especially the relationships, like, what are the different types of relationships that should be kind of identified as, as, like, the official set. And the comments on some of the times I've joined those calls is they've… they've been very, I got the feeling they're really looking for some people, and we seem like a good candidate, to suggest a bunch of entities, relationships, types, and all that. We're working on something internally, just to… for some of our own feature sets, where our goal would be, like, the output is, here's a big graph of hotel entities and their relationships with each other, part of which of that is expressing topology, you know?
And I feel at some point we're just gonna end up having to work closely together with them, you know? And so I just find myself wondering how much it makes sense also to sync with those folks, on those type of things. Sven is maybe something I could… Brained up a bit more to you this week before you're gonna travel anyway, but…
**Antonio Martinez (Cisco Systems, Inc.)** 35:54 Corruptly.
Do you mind giving an example? That would be, like, the interface will be an entity, and then we have, like, a device, like a router or a switch might have several interfaces.
**RC Rob Cowart** 36:04 Yeah, yeah. So let's say, like, a system is a switch.
And the system has two interfaces, but it also has a link aggregation group, of which each of those interfaces is a member of the link aggregation group.
Right? And so the relationship type would be, like, is a member of… or is… is a member of this group, because you could probably use member of a group for other technologies as well, right? You know?
And… so yeah, so like that, you know, and this interface is… connected to this other interface on this other system, which maybe also is just one member of another link aggregation group, right? So, that kind of stuff.
Oh yeah, and by the way, that link aggregation group has… for VLAN.
that tags on it, which, you know, et cetera, et cetera, right? So you have, like, you could have just one interface that has, like, actually 5, 6 different inter… you know, like, relationship types.
To other entities, right?
**Antonio Martinez (Cisco Systems, Inc.)** 37:15 Braydon that you're more… experience with all of that. Do you know if we're already doing that in OpenTelemetry? Those, relations between two entities? Because I am not that familiar.
**Braydon Kains (Google LLC)** 37:26 It is…
**RC Rob Cowart** 37:27 That'd be nice.
**Braydon Kains (Google LLC)** 37:28 As far as I know, mostly conceptual. I don't know if it's made it Properly into conventions anywhere yet.
on…
**Sven Cowart (ElastiFlow Inc)** 37:37 I haven't seen it.
**RC Rob Cowart** 37:38 Yeah, the last call I was on, they were kind of saying, like, they were… they were trying to bring an end to what they were calling Phase 1, and then… which was more the conceptual things, as you just mentioned.
Braydon. And then Phase 2 would be, okay, let's, like, actually get some concrete entity types and relationship types defined.
And I spoke up on a couple calls on just what our effort is over here, and the response I had was basically like, oh, great, someone's actually going to try to use this, and has potentially a pretty complex array of entities and relationships. So I actually think they're looking more for us to, like.
Give them something that could… they could then think about, you know?
**Braydon Kains (Google LLC)** 38:23 Yeah, I think that would be good, because, like, I've tried to suggest some entity relationships in the system world, but they're generally pretty… like… easy, like, they're really not all that complicated. Things like this VM is a EC2 VM, and separating, like, basically one-way relationships in that manner.
So I think the more complicated Entity relationships would be… Good to see, As far as people at the conference.
The only person I know for sure from the entity SIG who's going to be there is Dimitri.
and… you know, I'm… I already… I have a good working relationship with him, just from Collector and from System Group, so I can ask him if he's available for coming to the network Meeting to talk a little bit about some of that stuff. And I should also check if entities are gonna have a meeting of some kind in person anyway.
I will say that I suspect this North America conference is going to be… the worst attended by OpenSelemetry project people In, maybe, of all time?
Probably because, Salt Lake City sucks, and also because the U.S. is not fun to travel to right now, and there are a lot of important OpenTelemetry project members who are not in the US.
**Sven Cowart (ElastiFlow Inc)** 39:48 Hmm.
**Braydon Kains (Google LLC)** 39:48 So, for… For broader discussions with more people there, we're gonna be better off hoping, like, gunning for Barcelona, in March.
I don't know if people are already thinking that far ahead. I've made lots of submissions to the Barcelona conference in hope of getting accepted so I can go, because it is going to be much better attended by hotel project people.
**Sven Cowart (ElastiFlow Inc)** 40:12 I've made a submission to that as well.
**Braydon Kains (Google LLC)** 40:16 But all this is to say, there might still be people there that we can talk to. Dimitri, at least, if there are enough people from the entity SIG, I might push them to have a meeting If only because… there are… other groups that want to talk about entities in a more general sense, because we're waiting on it. System and network are two specific ones that are really waiting on entities to expand a little bit, because there are some things we just can't properly represent without things like the relationships and some of the, like, the telescoping relationship ideas.
Like, there are things, especially with, like, process entities, that we can't really represent, and some people are… Overly upset about, and suggesting very bad ideas to get around.
like, certain ways of representing processes, that I, like, I keep saying, like, let's wait for entities to make this better, and they just won't. I don't know. I, like, that sort of thing makes me really want to talk about entities at this conference, too, so I hope enough people are going to be there that we can, like.
meet and talk about it. I think I'll message Dimitri and see if he knows. If there are enough entities people, if I can push them to do an in-person meeting, it might be a good idea.
Just for us to talk about entities in general.
**RC Rob Cowart** 41:31 Sin, I will try to get you at least a draft of some concepts and examples on the network side that you could Have with you, if necessary.
Okay.
**Sven Cowart (ElastiFlow Inc)** 41:45 Sounds good. I know… by the way, you were definitely misled, and there is… either you misheard, or they misled you, but there's definitely an entity type, and it's… Easily communicated by the spec end.
**RC Rob Cowart** 41:57 So, what are all the valid values for that type field?
**Sven Cowart (ElastiFlow Inc)** 42:02 In the schema.
That it's linked to in the payload itself.
**RC Rob Cowart** 42:07 How many are there?
**Sven Cowart (ElastiFlow Inc)** 42:09 How many… that's the… I don't know.
**RC Rob Cowart** 42:12 There was, like, 2 or 3, like, examples there. That's what I'm saying, like, and there probably needs to be 37.
**Sven Cowart (ElastiFlow Inc)** 42:19 Yeah, the problem I'm having right now with the entities… piece is that these relationships, it's a little bit of a chicken and egg problem. Like, we need to put up a draft of, this is how we think relationships should be expressed.
**RC Rob Cowart** 42:33 Yeah. In the spectrum.
**Sven Cowart (ElastiFlow Inc)** 42:34 itself, so we can start iterating on the actual relationships on an example-like network. Because right now, the only way to Express a relationship is by just adding more attributes.
And then maybe adding more schema links, and that's kind of it.
And that's not great, because then you leave the downstream system to have to infer from that, what entities did I receive? And it almost needs to be, like, a… draft PR, I don't know, but something of the sort of, this is how I think we could… Express the entity relationships inside the spec.
**RC Rob Cowart** 43:17 I think another issue, and this is… this… this was based.
**Sven Cowart (ElastiFlow Inc)** 43:21 Stop.
**RC Rob Cowart** 43:23 one of the first calls I joined, they had a long discussion around just, like, what… which… Attribute uniquely identifies a host or a system.
Ghetto.
IP address? Well, it could have multiple IP addresses. Which one is in any given form of a piece? Like, a log might have a hostname. This one has a fully qualified domain name. The other one has, an IP address. Oh, it was a router, so it sent from the IP address to the loopback address, but maybe it just sent with the IP address source, you know, of… of the interface that happened to exit. You know, like, which one is it?
And I've been thinking about this a lot, because I think we're gonna end up in this scenario in some places on network, too, is like… I don't see how at some point, you don't have some type of Entity ID Resolution Service.
**Braydon Kains (Google LLC)** 44:21 That is essentially where we've landed on Host, too, by the way.
**RC Rob Cowart** 44:24 Oh, is it? Yeah. Like, where it's like, basically, I have these two pieces of information. Tell me the ID of that of that host or that thing, you know? Like, so that I can add it as an attribute to… we've talked about internally for something we're working on, like, maybe we're gonna need some… Some type of similar thing.
So that's interesting, y'all landed on the same spot, so yeah.
**Braydon Kains (Google LLC)** 44:48 Yeah. We've essentially had to, write out in text.
what we think the host ID should be based on the information you have available, and, like, expect them in priority. So, like, we say.
if you're within a known virtual machine providing service, like EC2, like VMware, like one of these, then… you use the ID that they give you in that scope. And, like, it essentially all boiled down to the fact that no matter how hard we tried, fundamentally, there is no way to uniquely identify something in the entire world… uniquely identify a host in the context of the entire world.
And so, we narrow down the context based on where you are, and we expect… we're actually working on coding the resource detection processor to do the thing that we laid out in text, essentially, like, try to resolve all of these host ID values, and then pick them in priority based on the top priority one that you found.
**RC Rob Cowart** 45:47 That might be something to… because we'll get the same thing, like, on a network interface. Depending on where you're getting the information from, it might be a MAC address, it might be a SNMP index value, it might be the IP address assigned to that network interface, it might be its name. It, you know… If it's Cisco, it might be the abbreviated name or the long name, you know? Like, so… You don't know, you know?
**Antonio Martinez (Cisco Systems, Inc.)** 46:14 The main issue that I see there right now is, like, you always need to go through that processor that identifies that research ID.
Because that's something that is done after.
Always, right?
**Braydon Kains (Google LLC)** 46:28 So yeah, this is… this is kind of a tricky, tricky thing that's coming up, too, and I think… Grafana was the first people to really bring this up as a problem with the collector specifically, but, like, receivers themselves are often not producing useful enough information to work. Like, the host metrics processor… so, sorry, the host metrics receiver relies on the fact that someone is configuring a resource detection processor right after to add the right resource detection stuff.
And they weren't a big fan of that necessity, but that's, like, built into the collector right now. We basically just… By default, expect that everybody is… is configuring resource detection.
And that's probably not the healthiest… the healthiest.
**Antonio Martinez (Cisco Systems, Inc.)** 47:13 answer.
**Braydon Kains (Google LLC)** 47:13 It's a bit of a foot gun.
I don't know how we're gonna… handle this going forward, like… on one hand… honestly, I think the best way to do it would be for resource detection processor to work in a way where, like, if the receiver has provided some specific attribute already, don't try and resource detect and overwrite with your own. Like, just accept what the upstream receiver gave to you first.
so that certain… if something like SNMP really wants to give its own resource detection stuff, or its own entities, it makes sense that it would give the entities that it wants, rather than expecting that something downstream is gonna add it on later. I think that's… when entities become… more prevalent in the collector, that's probably what's gonna happen. I think the host metrics receiver is probably going to start detecting the entities itself, rather than expecting the resource detection processor to be there, and, like, if the entity or specific resource attribute or whatever already exists on the signal, when the resource detection gets it, it will just, like, not try and overwrite it itself. I think that's what's gonna end up happening, but I don't know that for sure, because no one's… No one's said it yet, so I guess maybe take this with a grain of salt that this is my opinion, but I think it's shared by other collector people.
**Sven Cowart (ElastiFlow Inc)** 48:34 That makes sense to me. I, I… Ideally, it would almost land up in the SDKs itself.
like a… in each one of them, and then well-defined so that people, if they're not using the SDK for various instrumentation reasons, can also implement the same process themselves.
**Braydon Kains (Google LLC)** 48:53 I think that that's also kind of what the spec is expecting, in a way, too, because resource detection is also, like, an SDK element. SDKs have resource detectors, too.
separate from what the collector did. It's another one of those things where the collector came up with something because it needed to come up with something at the time, but it wasn't specified yet, so we have our own resource detectors, and so does the SDK, and they're not merged, so there's a little bit of… And by the time…
**Sven Cowart (ElastiFlow Inc)** 49:20 Yeah, and I think by the time the data actually hits the collector in… Probably a lot of scenarios, you'll have lost… The raw.
access to the raw, obviously, which might actually be the thing you'd require to do proper… Identity resolution.
**Antonio Martinez (Cisco Systems, Inc.)** 49:40 Yeah. And it can also be, like…
**Braydon Kains (Google LLC)** 49:43 There's… there's also some conflict between, like.
what if the collector is a gateway on a separate host? Like.
Does it matter that the collector… like, that you collect the resource… that the collector's running on. What you care about is the resource of the original telemetry that was produced, not necessarily the resource of the… collector that aggregated it as a gateway. So that's a bit of a… conflict, too. I feel like sometimes the resource detection processor Exists under an assumption that the collector's always running same host or sidecar style, not necessarily as a gateway.
**Sven Cowart (ElastiFlow Inc)** 50:20 Yeah, yeah, that's actually been biting me in the butt over the last couple weeks. I haven't had to fix a bunch of things, because that assumption was made, and it leads to problems like service name is now the collector. I'm like, what? No, that's…
**Braydon Kains (Google LLC)** 50:32 Yeah.
**Sven Cowart (ElastiFlow Inc)** 50:33 Yeah.
**Antonio Martinez (Cisco Systems, Inc.)** 50:36 But if I'm not mistaken, on the network ecosystem, that will never be the… scenario, we will always use a collector as a gateway, because we are not gonna run, never, a collector in one of those switches, or routers, or those things.
So we will always pull, or… I mean, if we have Gemini, as we were mentioning before, it would be pushed to us, but we will not have access to do any detection.
**Sven Cowart (ElastiFlow Inc)** 50:57 Yeah.
**Antonio Martinez (Cisco Systems, Inc.)** 50:59 It will be all in the receiver side, I guess.
**Braydon Kains (Google LLC)** 51:03 I think this is a good use case to… bring up… Resource detection right now doesn't have, like, Any really strong owner?
in the collector, the primary owners are not super active at the moment, so it's kind of just, like, owned by the collective collector group, generally. Because, like, we all care about resource detection, we just don't specifically own the processor, but I think if… as stuff like this comes up… I mean, it's coming up in host ID resolution right now, where we're talking about changing how the resource detection processor works to work with this new, like, priority resolution mode of host ID detection. I think that this is gonna come up again, where SNMP receiver wants to handle its detection itself.
Rather than expecting that a detector has to be configured right after it, and I think the detection processor should support that properly, if it doesn't already. I don't… I don't really know if anybody's considered The use case quite that way yet.
So, I think that will be… Useful to… useful to know On the collector side of things, and if it… it might come down to, like.
we make an RFC on the core collector about how the resource detection processor should handle this in the future, informed by what the SNMP receiver wants, or informed by the new changes that System group wants.
I, I think we're, we're pretty open to that stuff. A lot of… a lot of the collector that I notice, it basically just, like.
Falls into a habit of… we just hope that everybody is configuring it in the smart way, and if you're not, why aren't you? And then that… that kind of leads to a lot of, like.
Oh, this is the way we've always done it, type of… type of… Like, shoving problems under the rug.
So I… I think, I think we will be open to making changes like that. I know I will be, for sure. I want… I want resource detection to be less of a foot gun than it is right now.
**Antonio Martinez (Cisco Systems, Inc.)** 53:07 Perfect, sir.
Okay, so I… just to give some ownership, I will try to investigate a little bit about the SNMT receiver roadmap. I will do some proposal and investigation there, exploration, with the amount of time that they had.
And Rob or Sven if you can think about some examples of identity relations, so we can present to them if we have the chance, that would be great. And feel free to propose here any other topic, like, I don't know, like.
Interface, semantic, convention… Also, you were talking, I think, BEP has been one of the meetings that we have not that long ago, or also the Flows one. I mean, feel free to bring in person any of those.
won't… And then we can discuss it, I guess.
**Sven Cowart (ElastiFlow Inc)** 53:55 Sounds good.
**Antonio Martinez (Cisco Systems, Inc.)** 53:58 Okay.
Matthie, do you have something that you want to say, or something that you want to add today?
**Matthieu Noirbusson (Sensor Factory)** 54:04 Oh, no, I just tried to understand what you said.
**Antonio Martinez (Cisco Systems, Inc.)** 54:12 Awesome. Welcome to the meeting, by the way.
Okay.
So… I guess there is no other topic.
Happy to see you back, Rob. See you all next week.
**Sven Cowart (ElastiFlow Inc)** 54:23 Take care, bye.
**Matthieu Noirbusson (Sensor Factory)** 54:25 Bye.
