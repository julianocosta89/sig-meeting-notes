SIG: Semantic Convention SIG
Date: 2025-08-18
Duration: 123 minutes
Zoom Recording URL: https://zoom.us/rec/share/3eL6BNHT3aTPGuAIW0zjMN8jXBu6cYUhqSDsXZxC39neSLtINUTZjAIMzUkvSZey.8QV23wMCdDRTIOu2
============================================================

## Zoom Recording Transcript

Christophe Kamphaus 00:00:47 Hi, Trask, how are you?
Trask Stalnaker 00:00:51 Hey, Christoph! Doing good.
How about you?
Christophe Kamphaus 00:00:57 Oh, and fine.
Trask Stalnaker 00:00:59 Right.
Liudmila Molkova 00:01:05 Hi, folks.
Christophe Kamphaus 00:01:07 Bye, everyone.
Trask Stalnaker 00:01:09 A….
Josh Suereth 00:01:20 Hey, everybody.
How are we all doing?
Christophe Kamphaus 00:01:30 But, until….
Trask Stalnaker 00:01:31 You are so good. Two minutes into my week.
Liudmila Molkova 00:01:40 I don't remember seeing the lights in the aquarium behind you, Josh.
Josh Suereth 00:01:45 Oh, it's… it's a new one, sort of.
I used to have clownfish back there, and what I'm doing is I'm tearing down
the bigger aquarium I had in my living room, and moving all the fish here, so it's set up with plants to get ready.
And then the clownfish are out temporarily, and I'm gonna set up a, a bigger saltwater setup out there.
Nice.
Yeah, it's exciting.
I like it.
Anyway, you'll see the light on from now on, because I'm growing plants.
Alright, sorry, it's taking me a bit to get started. Had a… I had an exciting morning. Not as exciting as Trask's 2 minutes, but…
Alright, let's get going.
Cool.
Please add your, agenda items here.
We have some general topics so far, and then we have the triage board to get through, and the, pull request board.
So, alright, …
With that, I want to actually jump into the triage board a little bit and make sure we're making progress on stuff.
… Cool. So, good, we have…
Ready to be merged. This one, I wanted to check on… I looked at this this morning.
And I think that this one has enough approvals to make it through.
The only thing was, and it was in the merge queue.
So, there's one open comment, or no, two open comments from Ludmilla that I think are answered, but I wanted to check quick to make sure this one can make progress. So, is… is Alexandra on the call?
Liudmila Molkova 00:03:37 No.
Josh Suereth 00:03:40 Alright, ….
Liudmila Molkova 00:03:41 We can take a quick look and resolve the discussions.
Josh Suereth 00:03:45 Yeah, if you can make sure that they actually are resolved. I think she answered your questions, but I don't know if there was something to change. Anyway, this one looks like this should just be resolved, so I can do that now, but the other one….
Liudmila Molkova 00:03:57 Solve it, because I approved it before, so it wasn't important.
Josh Suereth 00:04:01 Okay.
Cool. Alright, so that is that one.
And then, there were a few here…
There's a bunch under Needs More Approval, …
I'm gonna take a quick, quick sec from that to go through…
the awaiting code owner's approval. I just want to make sure folks know that this exists, and this means that we're waiting for code owners.
Meaning, like.
HTTP Semcov, messaging Semcov, browser, to approve things before we move it into needs more approval. And a few of these that I was looking at, there were a few that came in for HTTP and messaging.
that I don't know…
For the messaging SIG, is that one active? Just, just wanted to make sure that it's… no?
Trask Stalnaker 00:04:53 Messaging SIG is not active.
Josh Suereth 00:04:55 Okay.
So just… I guess this is a broad, quick triage. Maybe… I'll add this as a topic for later.
Of, … We'll do maybe a 10-minute topic here.
What do we do with issues?
for owners that are not active. Okay.
Just to make sure we're making progress there. Alright, let's go through… I think…
We'll go through some of these needs more approvals, just to check. Update actions check out. This one is actually just a GitHub Actions PR. There's a second one in here for updating to Actions version 4.3, and one to update to version 5.
just ignore the 4.3, and let's all approve the 5-1. I don't think we…
I don't think we have to step…
That should be addressed in the work.
on project management issues. Right, right. Yeah, I think you're doing… that's one of the things I want to discuss. Okay. Cool, if you didn't see the chat from Jeff. …
Let's do not render deprecated enum members and examples. This one, I think, is, ready to go. This is a good cleanup from Jow. It is basically previously
Previously, we would actually render all of the… all enumerations…
Values that were stable and deprecated.
And there's a change coming in Weaver where actually the deprecated ones don't show up by default. Oh, Ludmill, you just approved this. Actually, this is probably ready to go.
Joao G. (Dynatrace) 00:06:40 Yeah, just, a neat, we rendered the three, the first three, examples.
And if… one of the first three were deprecated, and it was being rendered, rendered areas.
Josh Suereth 00:06:56 Yep, so I think this was a good fix. Alright, I'm just gonna… I'm gonna throw that in the merge queue now.
Cause I think we have….
Joao G. (Dynatrace) 00:07:03 Cool, yeah.
Josh Suereth 00:07:03 But it's not….
Joao G. (Dynatrace) 00:07:04 Let's go back to… what else do we have here?
Josh Suereth 00:07:08 Oh yeah, client-side jank event. This one, I think, was just waiting for one comment to be resolved.
So, I don't know if Jason's here, or if someone can reach out to them to make sure, but it was, … this knit, I think, actually, I'm treating as a somewhat blocking comment, which is…
Should we be measuring
the jank period seconds and doubles are in ints, so it's just a matter of, since it's a boundary.
And a window? Should it be a double window, so you have more flexibility? Or if it's int, you know, you have…
you have less, so I think I'd like to see that one resolved, and that's why I didn't throw that in the merge queue. But I think this does have enough approvals.
Liudmila Molkova 00:07:50 One more comment on this one. I don't believe I saw a prototype.
But I think they exist, so I would like us to be… …
pedantic, and add links to prototypes in the PR description.
Josh Suereth 00:08:09 Yeah, it says that there's a link.
here, but I don't see the link. Alright. Yeah.
Yeah, I think we can ask for it. I'll add that here.
Okay.
Beautiful.
What else do we have?
add SQL commenter, adds context propagation for database was ones. This one, I think…
I didn't have a chance to actually prove this one yet. Was there any open questions on this one that we needed to resolve? One from yesterday, yeah.
Liudmila Molkova 00:09:00 Is Sam here?
No, Sam is not here. We have a lengthy discussion on that specific wording.
And I… It seems how we need to continue it.
Josh Suereth 00:09:18 Take care.
We'll let that one progress, then, with that discussion.
… Cool.
I think… Is that Enum… oh yeah, this one, this one's interesting. …
So this one, I think there's not a lot that's done here.
it seems pretty relatively simple, I just wanted to check. So this is actually setting, and this is something…
The reason I say this is interesting is because I feel like we should get to a point where this isn't needed.
But basically, all members have a brief, and the brief is the capital version of the ID and the value.
So there… I think there's nothing contentious about this PR.
It's just adding a brief so that things render better. When there's an underscore, it just makes it actually a word.
So, again, I don't think there's anything contentious here. I think this one's fine to go. I personally think that tooling should automatically do this for us, if that's what we want.
Like, if you don't have a brief, you just synthesize one that is the capital version of the thing. But that's a different story.
… Yeah. Anyone have any concerns with this? Just wanted to check.
Liudmila Molkova 00:10:27 So, I think the… the reason I didn't approve it yet is I don't understand the point, right? So, we have tons of enums, around semantic conventions that are… they don't have briefs.
And we were fine with it. We are requiring brief on, let's say, metrics, or spans, or attributes.
Because it makes sense, right? The Inum members are mostly self-explanatory.
And if we are introducing briefs everywhere, does it mean we're going to require them? No.
So, this seems like a lot of busy work, but it doesn't… Help us achieve anything.
Josh Suereth 00:11:15 Yeah.
That's fair. My… the thing that I kept wondering is, if this isn't… if there's nothing interesting about it.
It should be synthesized.
But, but also… It's not really describing
what the Inum means, if you didn't know.
From the left-hand side, right?
Liudmila Molkova 00:11:36 Right.
Josh Suereth 00:11:37 Okay.
Alright, … So, are you… are you… do you want to block this, then?
Or… We need to make decisions about whether or not brief will be needed for e-news.
Liudmila Molkova 00:11:54 I don't want to block this, because I don't think there is any grounds for blocking, it's…
But I don't want it to approve it either. I can leave a comment with my… opinion on this.
Josh Suereth 00:12:07 Yeah, I think that that would help. …
I personally also felt a little bit weird with this one, with the… just the fact that, you know.
the core meat of this work is basically you have idle, and then you have capital idle, right? And you have eventual, and you have eventual without the strain.
And that felt weird to me, like there's some tool missing to make this easier and nicer, if we needed it.
Okay.
Matthew Hensley 00:12:33 Cool. I'd agree with both, perspectives on that one. If it's important, it should be automated, since it's
just… You know, changing the casing.
I'm not sure… If it's needed, because enums make sense, but say both those perspectives.
Kind of fit together. It's like…
Either, is it needed, and then if it is, it should probably be automated, since it's so clear how to do that.
Josh Suereth 00:13:01 Yeah, yeah
Alright, let's, so I look forward to your comment there, Lyudmela, and I think, we're almost out of our time box time quota. I wanted to do the first 15 minutes, so we have one more minute. Let's look at blocked. We have…
One Sun RPC model and NFS system metrics is now blocked.
Liudmila Molkova 00:13:24 Yeah, I blocked it because, … There are…
the approach taken on the SPR Is that we…
represent each time series as a metric. So, for example, we'll say
operations with something bad status, it's actually part of the metrics, or the TCP count, …
And it sounds like we could, …
A more detailed way would be to collapse them into one metric with multiple dimensions.
Josh Suereth 00:13:59 And I wonder, Braden, you're here, I wonder what you think about it.
Fraggle Rock (ca-wat-brt3) 00:14:07 Yeah, I, …
I went through and plus-woned the comments that I think we can just kind of do without thinking. I already told John about it this morning.
And…
the… I commented on a few that I think we might need to think about first, but for the most part, yeah, I agree with…
the… the suggestions.
Liudmila Molkova 00:14:29 Yeah, thanks. I… I had a general question, not sure if I asked it.
So, it seems like we are reporting something that's reported in Linux, in, …
the same, essentially the same way as it's reported on Linux. How much…
wiggle room do we have to report it in the hotel way? Like, how far we would be from
Like, this highly dimensional, Collapse the toll.
metrics.
Fraggle Rock (ca-wat-brt3) 00:15:04 I don't think any of your suggestions will specifically, like… I think… well, other than one, but most of them won't, like, re-directly transform the information as it's reported here, it's just sort of in a different format. The only other one is that, like, the… there's a few that are, like.
the… there's one counter for the full sum of everything, and then a breakdown of all the others, like, for TCP, UDP, and, like, general packet count.
And so we might need to circumvent a couple of them, like.
We don't want to track the general net count counter if we're…
Gonna produce UDP and TCP under one dimension, then the sum of those two would actually be what we want to report?
Liudmila Molkova 00:15:49 So there's a… Yeah, that's.
Fraggle Rock (ca-wat-brt3) 00:15:51 Couple things like that we have to decide on, but….
Liudmila Molkova 00:15:53 Yeah, let's work through this. Would it be possible to augment it with more details? Like, when we talk about connections, having…
server address would be useful. I assume it's not part of the metric that…
Is reported, so we don't have a breakdown per destination.
Fraggle Rock (ca-wat-brt3) 00:16:13 So that's a weird one. I did respond to that comment on the PR.
NFS being a kernel-level service means that, like, you won't have, like, multiple servers. I mean, maybe there's some weird edge case I'm not aware of, but you wouldn't have, like, multiple servers on one host, so the association to the entity sort of…
Is that answer, and the entity should probably contain that information, rather than it being on each time series.
Liudmila Molkova 00:16:39 And if you're reporting client-side, then you can have fewer consumers.
Fraggle Rock (ca-wat-brt3) 00:16:47 the client statistics are still one-to-one with the host, I don't… I think.
I think.
I might… I might need to….
Liudmila Molkova 00:16:59 to ask….
Josh Suereth 00:17:00 Yeah, if I recall correctly, the NFS daemon runs locally on the host, and that's what actually calls into the remote.
Like, so, so, you have, you have a weird…
what, client daemon thing going on, right? Where NFSD runs and gets you all your data?
and it's making all of your remote calls from your host. So, your client is, like, the process… and again.
I could be wrong here, so, like, take this with a grain of salt, because it's been, I think, 15 years since I used NFS in Anger.
But the client was, like, all your processes grabbing NFS things in the kernel, and the daemon server's the thing responsible for, like, serving up all of the NFS things locally in the host.
Right? Like, when you run an NFSD, you check to see if that thing's overloaded because it's, like, your local cache.
Fraggle Rock (ca-wat-brt3) 00:17:48 Yeah.
Liudmila Molkova 00:17:50 Okay.
But….
Josh Suereth 00:17:54 Again, I might be misremembering, because I haven't had to use those metrics in a modern metric system ever, personally.
So, it's been, like, 15 years. So it'd be good if we got someone who actually knows this, but I will say that some of the things I saw in this discussion about client-server are awkward as hell when it comes to NFS, and I think it's because it's baked into the kernel.
So, I…
I'm fine if we want to go with that vernacular the way it's written now, but it's not…
What is it? …
you know, if we look at the spirit of how we're trying to do client-server in SunConf, NFS, if we want to match that, we might have to rethink some things.
Fraggle Rock (ca-wat-brt3) 00:18:42 A lot of these stats, for reference, they all come directly from
from DockFS, like, the kernel is managing all these counters for, like, TCP and UDP datagram, whatever counts, and stuff like that.
And it's just from one…
From one spot. So, spiritually, when we are… like, the implementation that we have of this schema as it exists right now, it's just reading from…
the one file that the kernel manages, so there isn't really, like.
Like, we… if we were to get the server address or something and try and make it any more…
Any more dimensional than being attached to some host resource.
I don't know, I don't think there would… in the current implementation, there wouldn't be.
any difference. It would be one-to-one.
this all assumes that there isn't some weird NFS usage edge case that I'm not… aware of.
Josh Suereth 00:19:39 Sorry, I was wrong, by the way. There is an NFS server. NFSD is the server. I just, in my implementation of it, it ran on the same frickin' machine as the NFS client, so everything was local. But it doesn't have to be. And an NFS client could be remote, it could be in the same thing as
Right? So they could be together. It's just you pick one machine in your cluster to be the NFS server.
That's where the server metrics come from. Everything else is a client. And you get… you get file stats, like, when you talk to files in Linux, the NFS file stats are the ones that are important.
If you want to see how the server's doing, you check the server stats.
Fraggle Rock (ca-wat-brt3) 00:20:26 I'll see if I can…
meet with John today and try and answer some of those questions and come back on the PR.
With some more information.
Liudmila Molkova 00:20:34 Oh, thank you, I appreciate it.
Josh Suereth 00:20:42 Cool! We're over time, Box, so hopefully we can get some good discussion here.
Particularly about whether NFS RPC should be modeled in the RPC group or not. I think that's… that's kind of the main open, like, big question, right, Lydnolin, or no?
Liudmila Molkova 00:20:59 I don't think so. So, like, with the new, system-specific naming.
We would use, ONC underscore RPC as the prefix for the
ONC-specific things, and actually, I didn't… I don't think I commented on this, but RPC NFC would probably become just NFC.
So, to a large extent, it becomes irrelevant whether it's RPC or not.
Right.
Josh Suereth 00:21:29 I….
Liudmila Molkova 00:21:29 Oh, it's already….
Josh Suereth 00:21:30 Personally, I'd prefer that myself, knowing how NFS… knowing how people observe NFS, I think it makes sense to detangle it, because people aren't…
people who are dealing with NFS are dealing with NFS, people who are dealing with RPCs are generally thinking about RPCs between, you know, like, distributed microservice-type systems.
Liudmila Molkova 00:21:49 Alright, so NFS Infra RPC application.
Josh Suereth 00:21:53 Yep.
Yep.
Cool. That's where maybe if we had a, what's the use case and who are the users, as a question for somebody that would help us guide… guide the discussion, because I think that could have…
Avoided a lot of tangled… things on this PR.
Okay, … Awesome. So, Braden, you're gonna follow up on that?
Fraggle Rock (ca-wat-brt3) 00:22:19 Yes, ma'am.
Josh Suereth 00:22:20 Thank you. Alright, let's move on. Because I think the next one's related, Ludmela, RPC stabilization.
Liudmila Molkova 00:22:27 Yeah, we've been, trying to start this project for a while, but we are trust, I hope you're still with me on this one. We are starting RPC some quant stabilization.
And there is a doodles truffle, sorry, this timing. If you want to join, come join us. It shows date for this week.
We might not be able to start this week, but ignore the dates, pick the time that works for you, and we'll be happy to see you there.
Trask Stalnaker 00:23:06 Lyudmila, can you bump it out a couple weeks, just because if we… I think the, doodle may prevent us from, selecting things once they're passed, times once they're passed?
Liudmila Molkova 00:23:24 Okay, I'll do this. I think Doodle does it, but Stropwall doesn't, that's why I….
Trask Stalnaker 00:23:29 Oh, okay.
Liudmila Molkova 00:23:30 but I.
Trask Stalnaker 00:23:31 Awesome. Then, no need.
Liudmila Molkova 00:23:33 Trust.
Okay, I'll check. I'll make sure. Yeah, thank you.
Josh Suereth 00:23:43 I'm currently showing them in Eastern Texas.
Liudmila Molkova 00:23:45 But, yeah.
Josh Suereth 00:23:46 Just in case folks want to see what the available time slots are, and then go click your side.
Liudmila Molkova 00:23:52 Cool.
Josh Suereth 00:23:53 That's exciting.
Alright, next one is also Ludweller.
Liudmila Molkova 00:23:58 Yeah, so, can I present?
Josh Suereth 00:24:02 Yep.
Liudmila Molkova 00:24:03 Thank you.
Josh Suereth 00:24:07 Once, as it loads.
Okay.
Liudmila Molkova 00:24:11 I, … Cry.
So, I wanted to, socialize what we've done with complex attributes and gen AI.
I think we're still finding how to work with them across solid telemetry and starting with semantic conventions.
We actually have enough approvals. Thank you, everyone who reviewed, so we will be merging it, soon.
But, …
as I mentioned, I wanted to socialize and see how much appetite we have for doing things like this. So, the big question with defining complex attributes is actually how you define the structure.
what we've done in the past with event buddy, we had YAML events, YAML body definition.
It was… Reasonably good, and we can still probably use it, but …
It's kinda difficult, right? So ideally, how we wanted to define… … things as cold.
So we are actually including the models. They are non-normative. They're just for your information, but what's helpful is to define your models in the code.
and generate JSON schema, or the YAML body, or whatever we want to do with it, but generate it from the code. Because we, as developers, have much better
Experience reading the code and understanding this code.
So, we had similar things defined in the YAML in the past, and they took, like, hundreds of lines. Like, the code, it's actually way more compact, and it's easier to read, review, and everything.
So, this is non-normative, but the JSON schema we generate from it is kind of normative.
the benefit of JSON schema is that, okay, you…
sometimes you can even generate code from it. Like, if I want to take this JSON schema.
and throw it into some open-source Java.
code generator, I can get some terrible, but a good starting point for me to actually implement these models. Maybe it can be improved further.
And it's not the direction that we kind of want to go. We don't want to express everything as JSON schema, but we also don't have a good long-term story on how to do arbitrary code generation. So, like, this JSON schema is some spot in the middle where we can
created from the code. We can translate it into the code, but it's a manual step, and it still needs some refinement from human being to
… towards the instrumentation code. …
So, what we do on the… YAML, aside.
It's very… … Sorry, I'm looking for the motto.
It's not formal, so we were just saying that.
I'm okay.
It should be somewhere here.
… I'm sorry.
Okay, so we're just saying that… For this attribute.
Here is the JSON schema.
And ideally, there would be a formal way, but this is what we do.
today. There is a huge room for improvements. This is not the final story, but it… it kind of gives us
The middle term story to actually express
Structure for these complex attribute types.
Any thoughts, questions, concerns, ideas?
Aaron Abbott 00:28:48 I could ask something, Lyudmila, …
So, you mentioned at the beginning, like, there was a way to represent the schemas in the YAML.
what does that look like? Like, I think there was… it was pretty much just scalars or a list of scalars, right?
Liudmila Molkova 00:29:04 So it's currently, you can find it in Maine, if you go to Gen AI.
So here is the… Way we define the body today.
it's very verbose. You cannot reference types across each other. So, for example, if we use assistant message, assistant, like, the text part in one place, we would need to express it over and over again in every payload.
And… I found it extremely hard to read.
In the past. …
we can try and do exercise of expressing the same things as we do in Jason's schema in this structure.
… But… Yeah, I mean….
Josh Suereth 00:30:17 So, I think the big thing I'd say, I'm a fan of moving in this direction as a workaround temporarily, but I think what we want to define in SEMCOM, and possibly part of SEMCOM v2,
Is the notion of a custom type.
for which an attribute abides by. And that custom type can be referenced, it has a registry, you know, where you could say, like, here's a tool call, a tool call has these fields in it, this… and then when you define an attribute type, you can say, it is a tool call, right?
And I can reuse it in other places.
If we want to support… where I start to get a little bit nervous, or, like, one-ofs and any-ofs get really, really awkward, we're starting to build a full type system.
I love type systems, so I would just do this naturally.
But I don't want to inflict that pain on everyone else, if we don't need it. But if we need it, that's fine. So my only concern with this is that JSON schema is very rich, and it's possible we define things that we don't want to model in the future.
So, we want to, like, limit ourselves, of like, okay, try to keep these messages simple, don't do complicated things of, like, hey, if this field is false, then these other 5 fields show up, and if it's true, these 10 fields show up, right? That kind of crap is really…
where I think JSON schema annoys me, and gets really confusing.
So that's my only fear with this, is like, I think this is, …
You point out the good set of limitations with the current YAML thing, and I get it. And using JSON schema, I think, is better.
it right now.
But, I think we need to find a way to get this into the YAML, and I think having the ability to define types that attributes would use is exactly what we need to do.
Liudmila Molkova 00:32:07 Yeah, that's a great point.
And I think we are slowly moving into this direction.
Josh Suereth 00:32:15 I look forward to adding it to the, V2 proposal that you had, that we implemented in the current Weaver, yeah.
Liudmila Molkova 00:32:27 Cool! So then, if you wanna take a look, please go ahead. If you have some last-minute concerns, please, by all means, comment on the pull request.
And, … We're looking forward to evolving it for the semantic conventions use cases.
Cool, that's all I had, ….
Josh Suereth 00:32:51 Sweet.
Alright, let's get back to our agenda.
Next off is Kristoff on InfoMetrics.
Christophe Kamphaus 00:33:06 Yeah, can you open this issue?
Josh Suereth 00:33:09 Yeah, sorry, it's… I, … I wait for it to actually load before I click share tab. Okay.
Christophe Kamphaus 00:33:14 Yeah, we discussed it a few weeks previously, and I created this issue. I don't know if you had the time to take a look.
Josh Suereth 00:33:27 I did not, I apologize, yeah.
Liudmila Molkova 00:33:32 I took a brief look, like, Christoph, could you… would you mind guiding, as to how would someone use it? Like, I understand it's used extensively in Permedia as, like, a system.
I'm kind of curious what you would do with it, and how would you join Metrix? How… what would you extract from this?
Christophe Kamphaus 00:33:55 So… Here, what I noted down is not…
Not just for, joining metrics, It's for adding information, To other time series.
Of course, you can still then, perform…
A joint queries where you enhance, existing time series with this information.
Liudmila Molkova 00:34:25 Okay, so you're writing, information to other metrics, and then how would you use this information?
What for? Can you give an example?
Christophe Kamphaus 00:34:36 … Yeah, in the articles I linked, what they gave as an example is, for example, …
If you want to know if one metric changed.
Liudmila Molkova 00:34:49 When you did the deployment.
Christophe Kamphaus 00:34:52 Or to know… When one of the values in the infometric changed.
If this influenced your other metrics.
That's the main points they gave.
For example, if you're… Built info, if your build version changed.
That's, for example, USMC GoInfo, Or, … yeah.
… You might see that your risk request times go up.
After your deployment.
Yes, Trusk?
Trask Stalnaker 00:35:34 The only question that I had, I mean, it seems like this is, as Daniel, mentioned, I think, previously, it seems like this is very much the same as the future entity signal.
And so I… I think, you know, if it's something important to have, you know, sooner than the entity signal, or for systems, back-end systems that don't support the entity signal.
I think it's… I personally think it's…
okay to do that, but I was kind of hoping that the entity, SIG maybe could weigh in officially on the topic as far as… since it feels like it would be…
Like, long-term, it's sort of like a bridge.
…
And if there's, like, a recommendation from that group on, yes, we are going to be modeling this in this way, but for systems that don't support the entity signal.
This is the equivalent.
mapping.
Josh Suereth 00:36:48 Yeah, I think Daniel's also on the call. I can jump in for the entity SIG. So basically.
I do think that this info metric would be how we support Prometheus from entity signal. And I think, Daniel, you just added this in chat, of, like, you could take the entity signal and convert it directly into these info metrics, and that's how you consume it.
in Prometheus. And so, the question that we've had is basically, is it a trivial mapping?
Or does it have user engagement? We'd like it to be super trivial to do so.
And, for context, we have… we actually have this in one of our documents. I'm gonna try to pull it up. Give me a sec….
Christophe Kamphaus 00:37:28 In my last comment, I also mentioned this. In the spec, we have this, compatibility page.
And basically all resources, including entities, would be encoded in the target info metric.
But that's only one way, and we cannot, … Takes the existing info metrics, And make, entity.
Singing out of it.
Josh Suereth 00:38:00 Yeah, so, so from the original proposal,
we had a metrics and entity signal, where we kind of talk about cube state metrics, where in practice, like, cube state metrics are generally cube, entity name, and then a relationship, or state, of the entity, and there are gauges, and the value is always 1 with a set of attributes from the entity on it. And so.
You know, the naive thing we're thinking of is basically some kind of namespace, or entity name, or entity type, and then relationship or state gets put here, so this would be a particular descriptive attribute.
Possibly.
Gets turned into a gauge, and then the set of attributes here would be the identifying attributes for that entity.
It doesn't quite fit fully, so when we walked through this and looked at, like, what this could look like for, say.
hotel service info with service instance ID and service namespace and service name, and you want to, like, report service version as a gauge, right? We'd have an info metric where the version would be a label, and so would all these things.
…
the entity itself, and that would kind of meet what you're seeing Christopher show with this infometric. So that was kind of our thinking, and God, I think this was a year ago? Is that right, Daniel, when we wrote this proposal? Is that, like, or longer?
Daniel Dyla (Dynatrace) 00:39:28 Do you think a year sounded about right? I was gonna say less, so if you're thinking longer, then we'll meet in the middle and say it's been about a year.
Josh Suereth 00:39:35 Okay, okay. Yeah, so this is kind of what we were thinking about a year ago.
But we've kind of deviated hard to get entities and resource working, and the entity association bit. So, like, we've been solely focused. So I don't see the entity SIG addressing this problem directly for at least another 6 months while we finish the, …
the resource entity association work, before we, like, formally say, okay, here's how Hotel's gonna do it. But this is absolutely in line with how we're thinking about things. …
What do you… what do you think, Daniel? Do you think we should…
Take a quick detour and try to at least come up with this kind of a mapping, or have this discussion on the side while we do the other work.
Daniel Dyla (Dynatrace) 00:40:21 I mean, I don't see any reason why we couldn't do a basic mapping in parallel with what we're doing. I think that the core data model is pretty well established at this point, and it's not likely to change.
And it's all about, you know, how do we map that data model to something like Prometheus? I don't think it's affected by the other work we're doing, which is primarily, like.
Resource compatibility and that kind of thing.
I don't know how you're thinking about that. I know that Christoph said, you can't map the other way. I don't know if that's a blocker, like, if we receive…
You know, if you're using a Kubernetes, or not Kubernetes, I'm sorry, …
Prometheus receiver, and you get a bunch of intro… info metrics, is it okay to just propagate those as metrics?
then you end up with them potentially in OTLP and not represented as entities. You could end up in a weird state.
But… That might just be… part of what happens. We may need a way…
to convert entities into infometrics even without Prometheus, though, in order to…
make that consistent, right? Because if you… if you receive a bunch of info metrics and generate a bunch of entities.
You don't want it to look, all, like, mishmashed, on your backend, so maybe…
Maybe that's something that a collector processor, can solve and say, like, we just want all of this to be infometrics. Or, the other way, like, if you have this, this, this, and this infometric, that's all one entity, although then you're introducing a state, so that's…
probably a bigger topic for collector folks. But in general, I think in entities to info metric
mapping is not something that I think we need to put off for any specific reason.
Josh Suereth 00:42:15 Okay. I'm more worried about the inverse. Yeah, I think… I think you're right that we could totally take entities and turn them into info. This is more… this was the… the… the bit that was more exciting, was, like, should we have the ability to get,
Kubernetes entities from CubeState Metrics, and kind of reverse engineer the entities from CubeState Metrics.
As opposed to writing, like, instrumentation from scratch. That's a problem we can sort out later, but from the… yeah, I agree with you that… that we… the first one's a priority, and we can probably do that in parallel.
Especially if you're interested in this, Kristoff, feel free to join us.
Christophe Kamphaus 00:42:53 Yeah, I don't think I will have the time, I just wrote up this issue.
I don't think I will have the time to look into it.
Josh Suereth 00:43:02 I can… I can add a link to this from the, in your issue. By the way, this is linked, if you look at the entity SIG meeting notes, there's a bunch of, like, background reading at the top of all the proposals we put together. This is the one called, Resources and Entities.
from that.
So, if you wanted to find it, and it's under the metric and entity signal, almost at the very bottom.
So, I'm guessing a lot of people didn't make it down that far. Anyway.
Cool.
That was a great discussion. I think we'll follow up… oh man, I have the entity's notes up. Here we go.
Here's our notes. …
We'll follow up with Entity SIGS on this. Christoph, for your needs, what do you need for infometrics right now? Like, what would you consider a blocker for your CICD work?
Christophe Kamphaus 00:43:57 … So, in my pull request, I split it off to have just general guidance on per…
pipeline run….
Josh Suereth 00:44:07 Metrics.
Christophe Kamphaus 00:44:09 And, as we discussed previously, I defined the infometrics just as a gauge.
And that's where we, … But we came to this discussion.
Liudmila Molkova 00:44:23 I'm kind of curious what drives your ERPR to introduce it? Like, is there some specific scenario that you care about?
Christophe Kamphaus 00:44:34 … it was… Basically, to mix the link between different entities.
Liudmila Molkova 00:44:45 And so I think the key part that the entity, group will not address is that you are introducing metric that has,
Josh Suereth 00:44:54 Duh.
Liudmila Molkova 00:44:55 pipeline, run ID entity, right? You're not adding this entity on other metrics, but you're adding it on this one.
Christophe Kamphaus 00:45:05 Yes, I have this infometric just to link two different entities.
Liudmila Molkova 00:45:15 And this would help you.
Somebody using this matrix understand?
If, let's say, pipeline runs got longer because…
Actually, can you help me here? I'm a bit mad.
Christophe Kamphaus 00:45:34 Basically, we could query our metrics, for example, container metrics, load metrics, memory, CPU, whatever.
For a given pipeline run.
And determine if failures in our pipeline run are due to those metrics.
Was the other way around?
Or given pipeline runs, what are our metrics?
We could even aggregate some on a pipeline.
Do we see changes in our metrics?
And why do we need this link?
It's because… Sometimes, in some environments, we are limited. We cannot just add
All resource attributes to the metric series.
roles and metrics.
For example, on Kubernetes, if we have kubestate metrics for the container.
in which the pipeline runs. We cannot just add additional, Attributes to those metrics.
That's why I added this infometric to make the link separately.
Josh Suereth 00:46:58 You know.
Liudmila Molkova 00:46:58 You beat… go ahead.
Josh Suereth 00:47:00 this is the general, kind of, entity relationship use case of basically, the identity that you have access to when you're running. Like, the self-identity of me knowing who I am and where I'm running.
doesn't necessarily match the model that you want to show to users, and someone else has that mapping. And you need a way to join all this data, and you can't just force it to happen at the signal
time, right? It's… it's… somebody else understands the relationships from A to B, of, like, this pipeline is actually this Kubernetes task. So the way that this is solved today
is two ways that we see, right? One is this Prometheus way of you have an info metric, and people literally just join the two metrics together. You can actually expressly do a join, or you just render them at the same time to see what the hell's going on.
For some cases. And the other option is people have metadata servers, or systems that actually store this data, and allow you to interact, like, with the shape of everything at the same time, right? And Entities is trying to give OpenTelemetry that
metadata capability as a signal. So, if you want to have it be external, again, if you want to have it all be shoved into resource.
You'll have that capability in the future.
So I think what you're saying, Christoph, is you're solidly, like, you need this relationship somewhere to do these joins, so you need that reported somehow.
Christophe Kamphaus 00:48:33 Yep.
Liudmila Molkova 00:48:38 And going forward, the infometric. Let's say entities will be translated into the infometrics.
… Going forward, well, you still need to report
Some specific metric, or some specific signal that would be associated with that unique entity you are adding on that signal.
So it's not that you are just reporting the entity and it will translate into the infometric.
Christophe Kamphaus 00:49:13 I would….
Josh Suereth 00:49:14 Oh, I can talk from the entity side of what we're trying to build. In the future, we want to have an entity signal that has relationships, and so you would… you could decide, like, from an instrumentation standpoint, from a semantic convention standpoint, we will want people to define the entities and the relationships, and then metrics separately.
And then if somebody needs these infometrics, they will be inferred from whatever signal they need for their backend storage. So, like, longer term, these infometrics, like, I'm comfortable having them in SEMConv under this assumption that
All relationships that we define an entity.
We can say, here's what it looks like in metric form, generically. And that that will still be a useful thing we'll want to provide for systems that, you know.
are pure metric systems like Prometheus, right? But the definition, the, like, ownership of the infometric, becomes the entity relationship signal, or the entity signal.
Liudmila Molkova 00:50:14 Yeah, I appreciate the education. We are, I think, out of time on this topic. The one thing I want to mention,
I still feel that this defining us… defining this infometric today will not work with the entity region you just explained, because this
This would not… … it's not just the entity that will be added.
it needs… A signal to be reported with it, otherwise it will never be reported.
Josh Suereth 00:50:49 The entity is the signal that will be reported.
Liudmila Molkova 00:50:52 It won't because it's associated with just one metric.
this metric.
Josh Suereth 00:50:58 What I'm saying is, entities will be written as a signal.
And you could get a single metric for every entity.
Liudmila Molkova 00:51:08 Okay, so then, maybe, Christoph, we can keep discussing it offline and see if it aligns with…
Your proposal of having special metric with special entity.
Christophe Kamphaus 00:51:24 Yeah, I think C… infometrics that I defined will have to wait until some more generalized discussion
Both entity relationships is done.
I think it doesn't block me, I can still…
implemented in Jenkins, plugin, whatever.
And use it, until then, plus node in some conf.
Josh Suereth 00:51:53 Yeah, I'd recommend that as your path forward. So basically, have the metrics available for people to use, but don't put them in SEMCOM yet. I would still document in the collector, of course.
So….
Christophe Kamphaus 00:52:03 Sure.
Liudmila Molkova 00:52:05 Yeah, thank you.
Josh Suereth 00:52:08 Alright, let's move on to, what should we do with issues for owners that are not active? So, Yao, I don't know if you want to take over here to talk through this, but you have a,
a bunch of proposals to clean up things, and I think it's time for us to start talking to folks about this. …
Introduce my idea about SIGs and Markdown Generation. Do you want to talk through this at all?
Joao G. (Dynatrace) 00:52:36 Yes, I just, yeah, I just opened this. This was, I think, one of the things, or the main thing that we discussed in our, private meeting that we had about project manage and stuff.
And the idea was that we would have something similar as we have in the community repo, where there is a SIGCMO file, and we defined
We define all the six that are there, and the hope that we have is based on, you know, what we put in this file, like, if you open, there is, like, …
I came up with a JSO schema, but basically, if you go to the YAML, 6 YAML file.
Yes, I put it up, for example, labels to encode the status of the SIG, for example, when the SIG is accepting contribution, or if it needs prototyping or something. So the idea is that we would encode these things there, and
based on the areas label that is also there, and the… or the directory path, we would be able to flag things like PRs and such. If, for example, the SIG is inactive or is not accepting contribution, we would hopefully use Copilot or some automation to comment on this and
properly tag and triage and maybe close, or something like that. So that's the idea.
Josh Suereth 00:53:58 Yeah, I think for the sake of everyone, Jow has been looking at how to fix our triage process. If you looked at the triage process today, it's, we have, I think 122 pull requests open today.
120, sorry, we got through 2. We have 624 open issues, right? And we have a highly distributed ownership. So, like, in defining what success looks like, what we want to make sure of is when a pull request needs to be reviewed by a code owner, the code owner knows it.
And the maintainers know it.
when a pull request is done with code owner review, we want to make sure maintainers know it, so we know when to merge and approve things. But right now, the triage process we're going through, you've seen it in the beginning of the meeting, it often involves us as, like, the general approvers.
re-reading through all sorts of comments to figure out, okay, are the code owners done with this yet? You know? And it's kind of an unclear handoff, so we want to make that more explicit.
And we want to make sure that things kind of don't linger in a hiatus of nobody knows what to do with them.
That's the other failure mode we have for PRs, if someone makes an aggressive PR,
The code owners are not accepting changes right now, and it's not communicated,
across the board. It's, like, known by a few people, but it's not, like, well communicated. So, I'm a big fan of this, Yao. Like, I think that's, …
this, this is a big improvement. If, if we can start to…
Start to get someone to comment, like, yeah, this is not accepting contributions.
Liudmila Molkova 00:55:38 One….
Joao G. (Dynatrace) 00:55:39 Yeah.
Liudmila Molkova 00:55:40 Oh, God.
So one thing I hope we can decide is that if we're not accepting contributions from this area.
And effectively, there is an automation that closes the PR.
Josh Suereth 00:55:57 Yes, we should absolutely close the PR. The other concern I have, though, is if we say not accepting contributions, does everything turn into a bug?
Instead of a feature request.
Joao G. (Dynatrace) 00:56:13 I guess it… I guess it can depend.
it's really, like, a bug or something's wrong. It's, like, what we discussed as well about, like, if this doesn't apply to, simple things, like, would the thread change or something, like, because the idea is also, like, if…
…
for example, the SIG is inactive, like, messaging, and then somebody opens a PR, then if this automation works, we would comment, like, hey, this is the… we're not accepting changes on this because the SIG is inactive. Please, if you want to
to kickstart the group again, to do X or something. But if… I assume that if something is really about them, it would still, as a general approvals.
Go through it and get it done. Get it, get it, get it merged.
Unless it's, yeah, something… something too big, but….
Trask Stalnaker 00:57:02 We can have the automation.
Yeah, I was gonna say this, we could have the automation on the PR not close it, boom, but instead add a tag and say, you know, and then it will follow up
You know, a few days later, or a week later, and close it, which would give us time, or people time to appeal, or us time to….
Joao G. (Dynatrace) 00:57:26 Yeah, that's a good idea. It should go to some workflow, yes, exactly, yes.
that we can… filter out those particular cases, yeah.
Yeah, it's really draft, I just put it together, like, I don't know, 2 hours before the meeting, so there's a lot of things to iron out. But the other thing that I forgot to mention in the beginning is that, apart from the automation, what this also aims to help is
to make it more transparent, like, what SIGs exist today, and which SIGs are active, and…
If you want to collaborate or do something, like, who should you talk to, and, like, what's your point of contact, and so on.
because we have most of the information in the community repo, in the project section, but I'm not sure everybody knows about it, so I think having it here and a link there, that's what I also have a link there, helps, because then you can see
all the people that volunteer to work in the SIG, and… and yeah. There's also, like, often there's this, like, channel also as part of the thing, so you can reach out to the…
Slack channel and so on, so it just adds more transparency.
Yeah, and then there is a very rudimentary table rendered.
…
Can you refresh my mind that we shouldn't use HTML inside the Markdown table, right? That caused problems with the website.
Liudmila Molkova 00:58:49 The AREF, right? Not just the ACM.
Josh Suereth 00:58:54 Yeah, here's the thing, though, I think… I think that this is not pulled into the website.
So, if Sigs is top level.
You might be okay, because I think… I think the website is mostly driven from docs, but we.
Joao G. (Dynatrace) 00:59:11 Did you convert that?
Josh Suereth 00:59:12 So, like.
Joao G. (Dynatrace) 00:59:12 Okay.
Josh Suereth 00:59:13 Yeah, docs that we use for ourselves, if we want them on the website, we can put them on the website, too. And then please don't mess with Ahref, but last I checked, like, our mainline README, I don't think was used. I think it was… it was everything under docs.
Joao G. (Dynatrace) 00:59:30 That's good, because I want to do some more nice rendering of these things, and it's good. But I guess also, if it's there, we can also somehow exclude this, I would hope, from the indexing on the website. Okay, then I'll just use HTML.
Check with them.
Josh Suereth 00:59:50 Yeah, Mike, I would… I would still check with the docsIG,
Joao G. (Dynatrace) 00:59:54 Yeah, yeah, no, I'll do first, I'll do first, yes.
Josh Suereth 00:59:57 Cool.
Nice, and look, we're, like, all in on JSON schema, look at this.
Another good one.
Joao G. (Dynatrace) 01:00:09 Yeah, I wanted to do because, especially what we discussed about, like, to seek statuses.
I didn't want it to be free text, because I think that might… having it a well-known list of values might help with the co-pilot things.
Josh Suereth 01:00:24 Oh, yeah, yeah, for sure, for sure, especially since there's a manual description of what it means, yeah.
Okay, I think the only thing to do… well, we're out of time, so we're gonna call it, but the only thing I want to discuss at some point is, like, what labels we'd want for SIGs, and what kind of status they have, and just to make sure, even when a SIG is complete, we still have code owners who can review
Code requests, and then get them through.
Cool.
Thanks, man.
Alright, I'll see y'all next week. Have a great week.
Liudmila Molkova 01:00:55 Thank you.
Joao G. (Dynatrace) 01:00:55 Hi.
