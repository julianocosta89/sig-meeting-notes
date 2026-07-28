SIG: Network SIG
Date: 2026-07-27
Duration: 22 minutes
============================================================

## Zoom Recording Transcript

**RC Robert Cowart** 01:30 Hey everyone, how's it going?
**Giuseppe Ognibene | Coralogix** 01:41 Hi, everyone.
**RC Robert Cowart** 01:50 Sin won't be joining us today. I know he has, he's out for a few days.
he did give me a bit of an update on the conversation that happened, last week, just to… it sounded like it was just a lot around things we need to be reviewing from other SIGs.
Trying to evaluate what makes sense to… To pick up on what might make sense to coordinate around other… You know, potential changes and things like that.
So I know that was, is that… am I… for anyone that was maybe here last week, am I representing that correctly?
**antonjim** 02:39 Sorry for joining late.
I don't recall there was any blocker, honestly, for the…
**RC Robert Cowart** 02:46 It's not a blocker, necessarily, just saying that, like, these are things that were discussed, you know?
**antonjim** 02:51 Oh, yeah, yeah, yeah, for sure, for sure, yeah, they were.
**RC Robert Cowart** 02:55 Yeah.
**antonjim** 02:55 Newer.
**RC Robert Cowart** 03:08 All right, sorry. Okay. And the other thing is…
**antonjim** 03:16 Go anti-stable, if I… Yeah, the protocol was pretty stable that way. I don't think there was any blocker, but… I imagine he will just merge it when he's back from vacation.
Question.
**RC Robert Cowart** 03:34 So, what are the steps that are still required from here to have that, To be… for this to be merged and accepted.
**antonjim** 03:51 Okay, well, I don't think there is any blocker, any extra step. Braydon just wants to join, he might have more context about requirement, but I don't think there are any other.
**Braydon Kains (Google LLC)** 04:03 I'm checking the PR.
Oh, this is the project proposal one.
**antonjim** 04:24 Sounds right.
**Braydon Kains (Google LLC)** 04:25 did we get… so, did Mila agree to… UTC sponsor… I think if there are no open discussion threads, And it looks like we've got lots of approvals.
I think usually what happens is They leave it open for comments.
for… A week after it's received approval from technical committee in GC, and it looks like it has basically been a week, so… You could probably… ask, our GC liaison.
To merge it, most likely.
**RC Robert Cowart** 05:12 Would it… would it make sense if I… Let me double check my calendar. Oh yeah, I have it there. That after this one, I jump on the semantic convention SIG call and just, you know, ask for any required next steps or anything?
**Braydon Kains (Google LLC)** 05:30 Yeah, probably. They aren't the SIG responsible for merging this, but, Lyudmila does attend that meeting, and she's our TC sponsor, so she might… Be able to help, just in case.
**RC Robert Cowart** 05:43 Okay, understood. Alright.
**Braydon Kains (Google LLC)** 05:50 the, the SIG responsible for merging this is the… specification SIG, and they meet.
tomorrow at 11 Eastern, so, like.
The hour after this one, tomorrow.
**RC Robert Cowart** 06:06 Alright, yeah, let me, pull that up on… Oh, I see him there, yep.
Yeah, I probably actually, if I needed to, could attend that as well. Okay.
**Braydon Kains (Google LLC)** 06:23 I can probably attend it tomorrow, too.
**RC Robert Cowart** 06:26 Alright, sounds good. Maybe we can both be there.
**Braydon Kains (Google LLC)** 06:29 Sure.
**RC Robert Cowart** 06:31 Alright, cool. Antonio, you had something to… Discuss?
**antonjim** 06:39 I don't know if you recall, for the people that was here last week, we were discussing about having the others IPv4 and PB6 extra attributed for when it's available, both of them are PB4 and PB6 on the same time series metric. So, here I have the proposal. We agree that we are not going to commit into that and others related.
Until we agree if we are gonna keep using tier, route, or source and destination.
Which Svern was the one proposing on creating that ticket. I might ask him some PTO, he couldn't make it, so I can… I can create that.
that, GitHub issue about, replacing PR remote with something more clear for user, like source and destination, less confusion. So… and then we can address all those JIRA issues… sorry, GitHub issues after… after that, if… I agree.
**RC Robert Cowart** 07:36 I mean, I think that makes sense to me.
I'm not a huge fan of that, that wording of, like, Peer in particular.
Especially under network. My brain just immediately goes, like, to routing protocol, you know, like, BGP peering is a very specific type of terminology, you know.
And so, I just think it has a more specific connotation in various network contexts that are not, don't really seem to be the intended purpose of that use of the word peer, so…
**antonjim** 08:20 Should I do that? So it will create that, that, ticket, and I hope… We can add commenter, agree.
Somehow, and that would be a good start… starting point after. So here, that was just honestly mainly to what we discussed, putting… track it under a GitHub issue.
**RC Robert Cowart** 08:47 I probably need to put something on the list, I had something I wanted to just mention to the group, but I don't know if, since I didn't put on the list, if someone else has another item as well. I'm happy to see… That order, so… Yeah, if not… so, you know, I… just so y'all are aware of some of my efforts that I've committed to, You know, one of the sources we expect to get a lot of indication of, like, entities and, And different, metrics and things that we expect to have in the network is SNMP data.
And I had mentioned in one of the other tickets that, The approach we were taking ourselves was, like, we… We have a pretty large collection of, of MIBs from different vendors.
And, to help sort through it all in a more, efficient manner.
We wrote a mid-parser that, you know, to parse all the objects out of all the MIBs and things, we, And that even includes a whole bunch of, like, just weird stuff that's not really conforming to proper MIB spec, but, like, vendors do anyway.
Then put all of that stuff into a, I happen to be just using Elasticsearch, because I know it well, into, like, Lexical Search, Vector Store, to help, be able to find and, related information and stuff. So.
finish that… that particular process. For anyone that happens to be interested. It turned out to be… Approximately 27,000 unique MIB files.
Of which, we extracted, 5.2 million unique SNMP objects.
The, And… but now it's in a form that can be a bit more easily sorted, searched through, slices for particular technologies pulled out of it, etc. So… My first step I'm gonna take with that is… is pull out all the things that would be related to, essentially, various entities.
And, get that documented so we can start to work our way through that, because as we had identified, that was one of the first steps. Now, I'm not… I don't want to boil the ocean with this, so to me, it's more about trying to pick out maybe those top dozen things to start with that are most common for the environments that we've talked about. More specifically, like, enterprise data center WAN networking is kind of that first, step. I think there'll be plenty to get started there, but, I know for myself, it would be good to… then pick a subset that we start taking, through end-to-end, if we can, through the process. But, But that process, we did finally get, like I said, all that information, all that data in. It took about 8 weeks of work alongside other work to get that done. By the way, I did the math. If each MIB object would have taken 30 seconds to do manually by a human, it would have taken 26 years to do that. So, you know, LLMs to read mid-descriptions do have their value.
But, anyway, I'm also gonna look into seeing how we can maybe expose that data set for others here in the group to potentially, query and take a look at as well. I'll let you know.
We'll make a little progress on that. But I do expect next week to have a good bit more… For us to kind of look at as a group.
as far as, you know, the different entities and things that we could maybe get started with. So, I just wanted to give a little bit of update on the progress on that. So, took a little longer than expected.
But now it's ready to get going, so, yeah, so some progress there.
Any thoughts?
**antonjim** 13:24 That'd be a great tool.
**RC Robert Cowart** 13:25 What's that?
**antonjim** 13:26 identifying… it would be great to start identifying the entities for the… SNMP data, yeah.
**RC Robert Cowart** 13:34 Yep.
**antonjim** 13:39 What was the status of the entity proposal that we started with?
IP address, interface, access point, what was the other we were discussing?
**RC Robert Cowart** 13:54 Boo.
**antonjim** 13:54 be…
**RC Robert Cowart** 13:55 It's not been started yet, because I… we wanted to get this other part… internally, we wanted to get this other part finished, so we could start to put a little bit more meat behind it, because to me.
I mean, I… this is my personal preference, and if it's inefficient, I'm more than happy to someone to tell me that it is, but instead of just throwing something up, I prefer to be like, well, we think this should be an entity. Why? Well, these 27 vendors support that, and they do so in this way, and it has this relationship to… you know what I mean? Like… A little bit more to it than just… Hey, this is my opinion, you know?
So,
**antonjim** 14:37 Sure, sure.
The reason why I'm saying is because I think the other one was, like, more like the base, network base, rather than starting with SNMP directly, but yeah, I think both.
Could be discussed also.
**RC Robert Cowart** 14:49 Yeah, yeah, yeah, yeah.
Does anyone have any other topics that they need to bring up?
**Marc Netterfield** 15:00 I guess I was gonna go ahead and introduce myself, I'm Marc Netterfield, I'm at Grafana currently. I worked at New Relic when they launched their network monitoring product and built out most of the entity definitions over there for what they had for the idea of a network. And then, Previously, I did, like, a decade of work in, kind of, in the SolarWinds space, so, you know, monitoring and SNMP and all of these things, so… Super interested in, what you're talking about there. I… me and the team that I worked with, we spent, like, 3 years building out, like, MIB profiles and stuff. So, very excited to hear that you've got a tool that'll do it.
**RC Robert Cowart** 15:40 Yeah, you know, I had always said for years the problem with MIBs is they are not… the structure is not sufficient to make them 100% programmable, like, as far as what you can get out of them. A human always has to read them and figure out, what is this thing supposed to mean? And…
**Marc Netterfield** 16:01 Hmm.
**RC Robert Cowart** 16:02 But it's.
**Marc Netterfield** 16:02 And typos, and mistakes, and like, oh, it's a gauge, or a counter.
**RC Robert Cowart** 16:06 Yeah. What were we saying, sorry?
**Marc Netterfield** 16:09 I was saying, and the typos and mistakes, and oh, I'm not sure if it's an age or a counter, or…
**RC Robert Cowart** 16:14 Yeah, yeah, yeah. My favorite are the ones that say, like, I'm a gauge, and then you read the description, and you go, no, you're a counter.
**Marc Netterfield** 16:22 Yeah.
**RC Robert Cowart** 16:22 But yeah.
**Marc Netterfield** 16:23 when we were doing the ones at New Relic, we made people give us a walk from a device, because we're like, I can't trust the MIB file. Like, you gotta give me real hardware.
**RC Robert Cowart** 16:32 Yeah, absolutely, I mean, that's always the preferred way. You know, something else we could potentially share for different purposes is… We did actually write for our internal purposes, our own mid-walk tool.
With a MIM simulator tool that can… I mean, the output is very similar to, like, a NetSNMP MIBWalk.
But it has a little bit of extra stuff. So, like, you know, for example, all the strings are both the octet string representation of hex, as well as the printable string, you know, and different things like that. So… but it enables us to, again, just like you're saying, not only get actual MIB walks, but get a, You know, have something that you can, like, later when you're developing a collector or something, you actually have something that you can… Replay it, and it's going to answer exactly bit for bit the way the device did, you know.
No.
That's actually a really good point. I'm glad you brought that up, Mark. You know, we have our own one of those that… I had not posted, but… For our own collector, but it will… Obviously, some of this stuff will change once we get down this semantic convention path, but…
**Marc Netterfield** 18:12 Yeah, one of the things, too, in that catalog was that, we were curating it for, like, what will customers pay us to store, because that was the billing model at New Relic, and so it tends to be things that help to either define a boundary or provide, like, critical, important, like, performance state and things like that, so… Got it.
**RC Robert Cowart** 18:35 Sorry, I got distracted on something for a second. Because yes, I was just like, oh yeah, that's right, Kintec and New Relic had that relationship with each other.
Because… because before, when you said, like, at New Relic, you did this network stuff, I'm thinking, New Relic didn't really have network stuff, did they? But yeah, you had the Chem Tech partnership.
Got it. So you were, though, New Relic on that side of that, right?
**Marc Netterfield** 19:03 Yeah, there were 3 of us, but yeah.
**RC Robert Cowart** 19:06 Could you pause sharing just for a second?
**antonjim** 19:11 Oh, yes, sir? You're free to take it.
**RC Robert Cowart** 19:13 I'm not… there we go.
Oh, there we go.
Yeah, this is also public. These are the ones for our current collector that we would… Obviously adapt over time to, to be… More specific to whatever we end up doing on semantic conventions.
And while some of this is very, like, just more or less the vendors' names. There is some effort that we had already put into normalizing things.
like, all BGP-type stuff, so there are certain things that… I'm not saying these names would stay the same, or whatever, like, I'm… I'm definitely not attached to any of it, as far as that goes, but just as, like, you know, where there is opportunities that we know we can… that there's a really core set of attributes that… can be normalized across vendors and stuff that we can bring into it, so…
**Marc Netterfield** 20:25 And the same… I mean, obviously, SNEP's its own can of worms, but the same problem exists in the GNMI space as well, right? Is that every attribute has been renamed, but most of them could be consolidated down to, like, standard patterns.
**RC Robert Cowart** 20:40 Yeah, well, I even think that applies to things like Linux boxes and whatever. At the end of the day, most things about network still borrow a lot of the concepts and naming from what was the original S&MP 40 years ago, right? So… Yep. Okay.
Cool, that's good to know. I'm glad to… good to meet you, Mark, and look forward to, working with you on this.
Alright, did anyone else have anything they needed to bring up?
If not, we could probably cut it short this week. Like I said, I do expect next week to have a bit more to start going through.
I will… I know we don't have, like, a repo or anything yet, but I will create probably an issue in the, you know, the… the larger semantic convention repo.
Beforehand to try to get it so everyone has an opportunity to take a look and comment and what have you beforehand, so we can be productive next Monday, so… All right.
**antonjim** 21:44 Sounds familiar, yep.
**RC Robert Cowart** 21:47 Cool. Then, yeah, thanks, everyone. Take… enjoy… enjoy the time back, so…
**Braydon Kains (Google LLC)** 21:54 Thanks, everyone.
**Stephen Lang** 21:55 Thanks.
**antonjim** 21:56 with it.
