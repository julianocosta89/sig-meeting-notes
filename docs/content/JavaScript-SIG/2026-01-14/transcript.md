SIG: JavaScript SIG
Date: 2026-01-14
Duration: 60 minutes
Zoom Recording URL: https://zoom.us/rec/share/KjaoSVrhzeCBOEUACX9waJqFA-KhKzysjVHiMigfCgkz3IuBsTt903DGKnCYyyZB.aoOF1mAoqxj7NJGE
============================================================

## Zoom Recording Transcript

Trent Mick 00:00:38 Rules.
Marc Pichler (Dynatrace) 00:01:19 Nope.
Marylia Gutierrez 00:01:21 Hello.
Marc Pichler (Dynatrace) 00:01:52 Alright.
So let's get started. Welcome, everybody.
The first topic here is… Marie dear.
Asking for a release.
Marylia Gutierrez 00:02:05 Yeah, I just saw that it got merged, so yeah, it looks like you're already on it.
Marc Pichler (Dynatrace) 00:02:10 Yes, I'm still waiting for workflow, approval, but then… New version should be out.
It's tune-ish.
Marylia Gutierrez 00:02:20 Great, thanks.
Yeah, that was pretty much it. The next one, yeah, it's just an FYI, I don't know if everybody saw this, but there is this old tab because
It's part of, like, the graduation, for hotel, that we want to differentiate things, make it, like, stable, so we have this new hotel that is, like, stable by default, and
Only… you have to, like, opt-in to have things, so, just…
put in there in case people want to check it out or have opinions on it. There's a lot of comments on it already.
Marc Pichler (Dynatrace) 00:03:01 Yes, thank you. I would definitely have a look. This is,
For, people who have seen the, community…
post, and also the… I think there was some announcement as well.
So I guess this is just a continuation of that as an old tab, right?
Marylia Gutierrez 00:03:24 Yeah, correct. So yeah, we are trying to break it out. We were actually just on the call with, like, GCNTC, discussing if we should break this up, this one even more, in more OTAPs to have this, but at least is the initial idea.
And we just want to get feedback, because it will affect all, like, SDKs and things like that, so in case anyone has any concerns as well.
Marc Pichler (Dynatrace) 00:03:47 Yeah, thank you for bringing that up.
I guess there's a lot to read anyway.
Marylia Gutierrez 00:03:53 Yeah.
Marc Pichler (Dynatrace) 00:03:54 And a bunch of comments already, so,
Yeah, I encourage everybody to have a look at this, and
Hopefully, we'll be able to get on with, stabilizing things before it causes us too much trouble. But… yeah.
I guess that… Kinda leads us into the next topic, anyway, already.
Marylia Gutierrez 00:04:22 Yeah, I put it there because, like, last week, I think the topic was there, but it was, like, a TBD, and we didn't got actually time to talk about it, so I just put it back here again.
Marc Pichler (Dynatrace) 00:04:35 Yes, so for… the focus topics that are currently defined, I think both of them are…
done at the moment,
Mostly thanks to, Trent and Jamie working on it, chipping away on that one.
So… I guess there's a few other ones, that we can…
pick up now. I think one of the most obvious ones is stabilizing logs API and SDK.
Since that is what's required for a bunch of other packages to become stable, too.
You know.
There's, the exporter…
what's it called? OTP transformer, which depends on the logs SDK, unfortunately. So, if we want to get the exporter stabers, then, the logs SDK is something that has to be…
Tackled first.
So we probably wouldn't be able to do exporters and logs at the same time.
It's just my view on the, things right now.
in terms of priority, I think logs would be…
The next thing on the list…
And I think traditionally we've done two, two focus topics at once, so… Yeah.
Does anybody have any?
Preferences on what to pick up next.
Marylia Gutierrez 00:06:16 I was gonna say, like, remember the last time we talked about it? I don't know if you can click and expand? There was not a lot of things missing for this one.
Marc Pichler (Dynatrace) 00:06:27 Yeah, so…
Marylia Gutierrez 00:06:28 Is that still the case? Because I'm saying, like, if it is… well, looks like still a couple, but yeah, because I was thinking, like, if there is very few things missing, we can already discussing adding, like, three topics, 4 topics, I don't know, because as soon as it ends, we don't need to have this talk again, and just pick up the.
Marc Pichler (Dynatrace) 00:06:47 Thanks.
Yeah, that would go a bit more into road mapping, but I think that makes sense, yeah. Having, like, a chain of stuff to work on, and then also having some information for people what's going to come up next is a really good idea.
Yeah, so for… for this here, there is a bunch of stuff here. Not everything is, really…
that much work. There's a few things in there that just need one PR and are fairly straightforward.
I think the biggest chunk that we would be looking at is a review from the TC.
At some point.
Once we're ready with…
like, getting the milestone done, we've, in the past done a review with the TC, where they would go in and have a look if we're actually SPAC compliant.
And then we would tackle a bunch of other concerns as well, as they come up.
Oh, hmm.
Carlos, you have your hand raised.
Carlos Alberto Cortez 00:07:59 Yeah, this is the complete set of issues that you need to resolve before trying to go GA.
Just to be safe.
Marc Pichler (Dynatrace) 00:08:07 Yes. New York.
Carlos Alberto Cortez 00:08:08 Perfect.
Marc Pichler (Dynatrace) 00:08:09 This is,
I think this is everything that we thought of as of now, but once we have that ready, we would be ready for a review from the TC.
Carlos Alberto Cortez 00:08:24 Sweet. Thank you. Sounds great.
Marc Pichler (Dynatrace) 00:08:34 Yeah, as for the other focus topics,
We have a few defined here in the backlog. One is the instrumentation packages.
Which… Probably is also fairly high priority, but also a lot of work.
Trent seems to have an opinion.
Trent Mick 00:09:05 I think that'll take a while.
Yep.
Marc Pichler (Dynatrace) 00:09:12 Yeah, then ESM packages, declarative config,
browser and bundler support, I guess this is essentially what the browser sig is working on, so I'm not sure if that needs a separate focus topic here.
And then there's, dynamic plugin loading, which I would say is lower priority at the moment.
Yep, that's in it.
Does anybody have any topics that, you would like to see here on the backlog that aren't there?
Trent Mick 00:09:56 I don't know if it needs a focus topic, or maybe it would help to have one, but I think come June, July, whenever the Node.js drop date is, we're… I…
whom we're planning to do a JS SDK 3.
That's dropping node 18 and 20.
And we'll have, I would assume.
It would be useful to have a bucket to be able to throw other…
changes that we want to do in there. So, for example, the…
StableStempCon for HTTP and DB will change over their defaults at that point.
I don't know if there's other stuff that we'll have…
Queued up for wanting to do,
Breaking changes, removing stuff that we've already deprecated or something.
Jamie Danielson 00:10:39 To your point, by having… if we add that topic, then we'll see things, come across them, and be able to add them in there, versus right now, it's just sort of out of sight, out of mind.
So I think that's a good idea.
Sorry, Mark, you were gonna say something.
Marc Pichler (Dynatrace) 00:10:54 I was just about to say that we have a few things that we've deprecated right now, but I think 3.0 won't be as big of a change as 2.0 was.
So,
I still think it would make sense to have something in the backlog here, so that we can move that up, because I think in any case, we would want to have another
stretch of time where we won't release, and just keep working on 3.0, and then do one, big push at the end where, we release 3.0, similar to what we did with 2.0 in the end.
I'd say we'd probably not want to have it be as…
Long of a period as last time.
One month should be… Enough for this time around.
And then we also don't need to do the different branches and stuff, which was kind of a headache the last time around.
Jamie Danielson 00:12:04 Yeah.
One thing that's on our backlog that I think
could come back up to priority as the declarative config. One of the reasons, too, is the…
They're pushing to put out, like, a stable, spec.
But they're waiting for more…
like, prototypes in other languages, especially because, you know, how JavaScript does things is very different from how Java does things, is very different from Go, so if we're able to get, like, the base stuff, not the instrumentation, not the more complex setup, but if we can finish doing some of the core pieces,
then I think that would help that SIG move forward, and we can still pause and revisit for instrumentations later when we're ready.
Marylia Gutierrez 00:12:54 Yeah, because that is something that I can… because, for example, I have a PR app that updates for the release candidate tree, because
That PR mostly changes a few things from location, like naming of, like, the model itself doesn't change for the actual usage, so I have that one up. So my goal was to at least finish the logger, meter, and trace provider.
And can I stop at that, because all the other stuff are things that we don't necessarily have the implementation that exists today, or things like that, so I… I have the PR up for the logger, so if we can, like, have review for those two open, then I can open one for the meter, the tracer, and then we can put, like.
a break on the declaracy config for the other stuff.
Jamie Danielson 00:13:41 Yeah, yeah, I'm kind of thinking of, like, we…
Right, we have a project board.
Right? I'm wondering if we have something more specific where we say, like, you know.
core, like, declarative config core things, and then declarative config everything else. Like, almost like two separate buckets, if that's useful. But…
Marylia Gutierrez 00:14:00 Yeah, I can't… yeah, right now I have the columns for, like, things that are, like, don't pick up, I have the columns, like, to pick up. I can kind of, like, rename and reorganize a little, just to say, like, these are the things we want to do, and then have everything else on the backlog until we get other things tables first.
Jamie Danielson 00:14:17 Yeah.
That works.
Marc Pichler (Dynatrace) 00:14:20 Yeah, I think that's a good idea. One thing that I…
I was just thinking of where you were talking about the PR that's already open. I wonder if we should start with, just traces and metrics at first, because these are the ones that we actually have as stable packages.
And then… I guess as a follow-up to the log SDK stabilization, we would continue with
Also adding the declarative config part for logs.
Marylia Gutierrez 00:14:57 Okay, yeah, I can open one for… because then I can already open base on the RC3.
That, like.
Marc Pichler (Dynatrace) 00:15:04 Clear.
Marylia Gutierrez 00:15:04 like, the next two based on that, because right now it probably would have a conflict on the logger, because that was created, like, two months ago, and the RC3 was… I opened just this week. But yeah, I can create the other two and share on the channel when I have those two ready.
Marc Pichler (Dynatrace) 00:15:21 Yeah, that sounds, sounds great.
So…
Jamie Danielson 00:15:25 I feel like…
somewhere for the tracer provider. I don't know if that's useful to pick up from there, or if you already have something separate.
Marylia Gutierrez 00:15:34 It's because I… I think, like, because it changes a few locations of things on the, like, some models change for, like.
Oh, true. Small things, like, on Tracer, like, meter, so you will have to, like, do, like, refactor anyway, so I might as well start from scratch there.
Jamie Danielson 00:15:49 Okay, sounds good.
Marc Pichler (Dynatrace) 00:15:55 Oh, what I'm hearing, kind of from this conversation is that we would likely look into picking up a subset of the declarative config as one of the focus topics that are coming up.
Jamie Danielson 00:16:11 I think there's not much… like…
in terms of, like, total PRs that are gonna go in, before we're like, okay, let's set it back down again, there's really not a ton of stuff, so hopefully that's just sort of a…
a quick one that we can get through, as we focus on it again. I think, Marlia, and maybe Trent, like, we could probably get through it pretty quickly.
If we focus on it again.
Plus, I got a talk accepted at KubeCon for declarative config, and it would be really nice to be able to say that JavaScript has implemented some of the core features, so…
Trent Mick 00:16:49 Is that the March deadline, then?
Jamie Danielson 00:16:51 Yeah.
Yeah, so if not, obviously, that's fine. There's still plenty to talk about, but it would be nice to be able to point that out, that we have some of the core implementation in there, too.
That's awful.
Marylia Gutierrez 00:17:10 Yeah, I can put, like, yeah, I can organize the boards, and yeah, there's already the board, but I can give you, like, a sentence or two if you want to put here, about, like, focusing on the core stuff, and what is the core stuff.
Jamie Danielson 00:17:23 Yeah. Let's connect on Slack after this, and… See if we can…
get aligned to make sure, because I can update this too, Mark, unless you wanted to, the…
This… is she happening?
Marc Pichler (Dynatrace) 00:17:34 feel free to go ahead and update it. It was always intended as a, like, everybody of the maintainers can update, so…
Marylia Gutierrez 00:17:46 Well, on that one, maybe also, like, a feedback, because we have, like, the thing from the browser there, but the browser seek is also this repo. Are they having their own, like, focus topics? Is it worth, like, saying, like, having this title
to specify what areas, like, here, just, like, core or something, or have, like, two issues, one saying, like, for browser, so they would know, just to, like, make
easier for people from… that are not aware that they're all on the same repo? I don't know.
Marc Pichler (Dynatrace) 00:18:20 I guess, we could link to the browser phase one doc, that's…
I think outlines what they're working on right now. I'm not aware of any, like, similar setup.
in the browser repo.
Trent Mick 00:18:41 Marilla, would you be able to ask Ted, actually? Because I think Ted had started trying to have GitHub Project to direct goals there, but I think he soured on using projects, and since then, I think there was some of this work from
I'm not sure if it's coming from the TC or GC about having
a document, or an issue, or some… some kind of similar process between the different SIGs for how they're talking about their roadmap, something. So, I don't know if Ted would have the best idea on what the browser SIG might want to do, or might be doing for… for having a roadmap.
Marylia Gutierrez 00:19:16 Yeah, I can check with him.
Trent Mick 00:19:18 Because he's the GC liaison for the browser, SIC, right? Yeah, yes. Yeah.
Another thing that I guess, isn't on here, but… and maybe it doesn't even need to be a focus topic, but boy, do I want to kill…
dash dash experimental… Loader.
behavior. Our docs are still pointing to using that, and that's, like, that's ancient at this point. Everyone's moved on to having base version of Node that can use, module.register.
I don't think there's a whole lot of work for us to… to move to doing that. It might mostly just be docs, and I'm not sure if…
things need to change in Auto Instrumentationist node, or something for that, but anyway.
Jamie Danielson 00:20:08 Yeah, I was trying to figure out if we should have a specific topic for, like.
other general ESM stuff,
Some of it is in that first tracking issue for stabilizing the instrumentation packages. I think there's some stuff there about
I don't know if it's making sure everything works, or if it's mostly documentation.
Trent Mick 00:20:34 ESM instrumentation in there.
Jamie Danielson 00:20:36 Yeah…
Oh, so some of that's… Done.
Marc Pichler (Dynatrace) 00:20:47 Yeah, this one might be a bit outdated. I remember writing this.
Jamie Danielson 00:20:53 Yeah, it was a long.
Marc Pichler (Dynatrace) 00:20:53 Yeah.
Jamie Danielson 00:20:56 But yeah, maybe… Maybe we, like.
Review this and potentially add a focus topic, because we also have, like, the testing of… ESM…
And stuff like that. Like, we could have a bucket for… we have one for publishing, but we could have a bucket for…
Other stuff, updating documentation and… Unless we reuse this one. But updating documentation, making sure pests cover
ESM instrumentation and things like that.
Marc Pichler (Dynatrace) 00:21:30 Yeah, we can also, like, if there's a follow-up to… if there's a better, more up-to-date plan, we can also close this issue and just put a comment here that links to the new one. That's how I've done things in the past with
Stuff that has gotten outdated and needed a new summary.
Yeah, we can either do the,
We can probably split a bunch of stuff.
from that thing here, especially in the ESM instrumentation part, and move that to its own focus topic.
Cop.
Alright, I guess we have two candidates to move up now,
I guess we can circle back on that topic.
Next week, and finalize, what we decided on.
And then we can also look into, prioritizing the rest of the backlog to see what's up next, to have a bit,
Have a few more topics that we will, that we know that we're gonna pick up.
And then we go from there.
Does that sound okay to everybody?
Trent Mick 00:23:04 Yep.
Marc Pichler (Dynatrace) 00:23:05 Alright.
I guess if there's nothing else to talk about for this, then we can move on to…
Next topic, which is mine. This was just me asking for a review, but I guess,
David already rebuilt this, so thank you for that. I will see to merge this in after the…
meeting,
And the next one is… Andre, looking for reviews to support instrumenting libraries that use subpath exports.
Andrei Borza (Sentry) 00:23:58 Yeah, basically same for me, this was already…
Trent Mick 00:24:03 Sorry. Implemented for import in the middle?
Jamie Danielson 00:24:09 This is the thing that we were talking about earlier this morning, Mark, or I don't know if it was this morning for you, or afternoon, but that Trent had mentioned.
We're looking at.
Trent Mick 00:24:20 So Andrea, warning, this is…
It has some subtleties to it, or at least…
I'm struggling with it. I've lost a day lost to this one. Yeah. I haven't written up findings, because I usually like to have a suggestion, and I don't have a good suggestion.
For this one yet, that kind of fuel.
Things that get in the way here. Anyway…
I've started… I've started looking at it, but sorry, go ahead, Aaron.
Andrei Borza (Sentry) 00:24:52 Yeah, if you need anyone to bounce ideas off of, or anything, I can connect you with Isaac.
Trent Mick 00:24:59 Sure.
I mean, I can hit up Isaac, he was asking me in…
Andrei Borza (Sentry) 00:25:02 Okay, yeah.
Trent Mick 00:25:03 the CNCF Slack as well, so… Yep.
Andrei Borza (Sentry) 00:25:07 Okay.
Cool, thank you.
Trent Mick 00:25:14 Is Isaac working at Sentry with you as well?
Andrei Borza (Sentry) 00:25:18 Yes, he is.
Trent Mick 00:25:20 Okay, cool.
be interesting.
Marc Pichler (Dynatrace) 00:25:28 Alright, I guess, Brent, you're looking into that one, right? And you have already…
Quite a bit of insight on that one.
Marylia Gutierrez 00:25:41 I just got back from TED, because I was asking if, like, if they have any… he said that they didn't write
like, in any place, because he said, like, the browser is the focus topic, pretty much, so they are working on instrumentation at this time, so I guess…
There's nothing specific for them.
Marc Pichler (Dynatrace) 00:26:02 Makes sense.
So, for this right here, is there anything in particular we wanna…
Trent Mick 00:26:14 Are… Andrea, are you guys blocked? Because, I mean, I feel bad.
Andrei Borza (Sentry) 00:26:20 I think, yeah, I think this blocks some of the AI instrumentations that we're trying to create, but…
Yeah.
Trent Mick 00:26:29 Okay.
I guess one request then, because I think it helps…
The correct answer is yes.
If it helps motivate a little bit of, specific…
package examples are on there. I know it shouldn't decide on the technical
Side, and the… there are already test cases that are showing the specific examples, but…
Andrei Borza (Sentry) 00:26:52 Yeah, basically, that's PR.
Yeah.
Trent Mick 00:26:56 Who just… Oh.
Langraph.
Thanks.
Marc Pichler (Dynatrace) 00:27:29 Right. So… I guess you were keeping in sync about this, and…
Trent Mick 00:27:40 Yeah, I'll try to get on top of that one.
Hmm.
Marc Pichler (Dynatrace) 00:27:43 I'm… I miss out if I don't have,
I don't have any opinion on it yet, so… Boom.
Yeah.
Trent Mick 00:27:53 Cuts.
Marc Pichler (Dynatrace) 00:28:00 Right. Are there any questions, or…
Things that you would like to talk about on this?
If not, then we can move on to the next topic, which is Carlos.
update on the M4 parsing logic.
Carlos Alberto Cortez 00:28:22 Yeah, this is the one on, this, PR that we discussed last week about auto resource attributes. We very briefly discussed, the spec call
Because it's under a specified.
So it turns out that, well, I started doing some digging on all the SIGs, so once I had a complete idea of what, like, not a few SIGs, but, like, most of the… like, all the SIGs, what are they doing. And it's very interesting, because mods 6 are not… are doing, like, different things.
So I don't know how in the rush we do… are we going with this one?
People initially discussed that it could be better to do a fail fast, like, you know, try to recover, like, valid entries, for example.
So, I'm…
I will keep discussing that today with an issue with the, you know, the list of all the six, like, explaining what
what is doing what, what they're not doing, etc. We'll go from there, we will discuss that next Tuesday again. And most likely, the output from that, it seems, it will be, like.
Hotel will say at the spec level what the user should be passing. Like, this is expected value, this is what 6 should do, and in the case of a user passing something outside this requirement, it's unspecified… unspecified behavior.
So let's see how that goes.
I don't know, as I was saying before, how in the rush are we with this one?
Marc Pichler (Dynatrace) 00:29:56 I think this is mostly a question to, Jackson, who opened the PR, I think.
He is on the call. Though I dumped…
Trent Mick 00:30:05 Yeah, I followed up and dumped a long comment on there, which I was a little bit hesitant to do. There are kind of some unrelated or peripherally related thoughts.
Jackson-iPhone15 00:30:18 Yeah, sorry, Trent, I haven't gotten back to you on that yet.
Trent Mick 00:30:22 That's cool, I'm not sure how helpful my thing was, it's just kind of… it's weird space in there.
Jackson-iPhone15 00:30:29 Yeah.
Trent Mick 00:30:30 Like, quite different parsing on how we handle key-value pairs in hotel resource attributes versus key-value pairs in…
hotel exporter, OTLP headers.
Which I thought was interesting. Some of that's kind of history in the reference to using baggage stuff for parsing, and the baggage utils is…
probably… like, I think… I think it was more of the hotel spec to refer to the baggage spec for doing this kind of stuff, because the baggage spec has weird things in it that aren't related to key-value pair.
Carlos Alberto Cortez 00:31:00 stuff at all. Yeah, that's correct, and I think that one of the questions was, like, whether it was a mistake. I mean, this is, like, very old part of the spec in Hotel, and we were doing that out of convenience. It seems simple enough.
But probably was a mistake. Let's see what happens now.
Trent Mick 00:31:23 Okay,
Yeah. If… if someone does go through and look what the other SIGs are doing, it would be interesting to have that table written down, so… because, like, sometimes…
That's the decider. Great, if you can get that in there, that'd be a.
Carlos Alberto Cortez 00:31:39 Yeah, I only need to go and check Swift. I already checked most of them. There are 6, like, ROS, that they are doing no decoding, they are not, they are taking all the web space that you provide.
They are… they are not doing, baggage octet checks, for example.
So, it's very interesting.
I mean, so, as a way of saying that, it's interesting that because of this being kind of underspecified, everybody's doing different… a different thing, you know?
But anyway, yeah, I hope that… sorry for the delay, yeah, so let's see, let's keep on iterating on this one. I really hope next Tuesday I can get, like, a more or less final initial agreement, so we can iterate on this one.
Marc Pichler (Dynatrace) 00:32:30 Thank you for looking into that and driving that on the spec side. It's very much appreciated.
Alright, next… Topic is… Oh, Martin…
Buponos.
Missing for months.
Yes.
I guess.
Marten Hennoch 00:33:03 If they don't show up, To, at some point, just… Do it ourselves?
Marc Pichler (Dynatrace) 00:33:09 Yes, that's how we've… Done it in the past.
Jamie Danielson 00:33:16 I think I've seen them somewhat active on CNC.
Marten Hennoch 00:33:18 Yeah, they're very active on GitHub. They're very active on GitHub. It's just not in here.
Jamie Danielson 00:33:23 Oh.
Marc Pichler (Dynatrace) 00:33:26 Do you.
Marten Hennoch 00:33:27 They're even working on some spec stuff on OpenTelemetry.
Marc Pichler (Dynatrace) 00:33:32 Did you try reaching out to them on the CNCF Slack already?
Marten Hennoch 00:33:37 I don't think they're on there, I tried to find their email, but…
Let's see if they're on Slick.
Marc Pichler (Dynatrace) 00:33:44 Yeah, I can also,
if you, if you, feel uncomfortable with, chasing them down this way, I can also,
try and, send them a message somehow.
Marten Hennoch 00:33:58 Yeah, if I find government system.
Jamie Danielson 00:34:00 in Semantic… OTL Semantic Convention's channel, one of them recently posted about, like, Oracle… semantic conventions?
Marten Hennoch 00:34:11 Okay, good, that would spam… spam him.
Jamie Danielson 00:34:14 Okay.
Marten Hennoch 00:34:16 And then… We'll see you next week.
Jamie Danielson 00:34:18 Maybe that will help.
Marten Hennoch 00:34:22 Thanks.
Marc Pichler (Dynatrace) 00:34:24 If it, hasn't been resolved, please feel free to send me a Slack message, and then I will, look into,
Finding them another way.
I have written emails in the past, so, that's the last resort.
Marten Hennoch 00:34:44 Do I see someone's GitHub email? From the logs, you do sometimes, but I didn't see theirs.
Marc Pichler (Dynatrace) 00:34:52 I'm not sure if they have, what they use to author their, GitHub commits, but the commits, commit messages is usually where I get the email from.
Marten Hennoch 00:35:03 Yeah, I don't think there's somebody.
Trent Mick 00:35:13 They're using the, the…
Marten Hennoch 00:35:16 Users.noreply.github.com emails for their commissions.
Marc Pichler (Dynatrace) 00:35:29 Yes, awesome.
Marten Hennoch 00:35:31 I'll start disagreeing with his spec contributions, and then he will talk to me.
Marc Pichler (Dynatrace) 00:35:39 Alright,
Yeah, let's see how that goes. If it doesn't work out, please feel free to message me, and I will try to find other ways.
to talk to them. Otherwise, if anybody has time to look into this one, please,
Please have a look, and we can also get this merged without owner approver, if necessary.
Alright.
Any, additional topics or things you would like to discuss?
If not, then I guess we could move on to bug triage.
As always, if there's anything that you would like to discuss, please feel free to interrupt me, and then…
We can… talk about your topics. So, it looks like here there's…
No new bugs. We crossed a few off the list, and, the releases
pending at the moment. Oh.
Seems that it's already been published, so the new version should be out, and this should be fixed.
Moving on to the contrary people, we have… The system information…
dependency, unassigning this to myself, because it's actually already updated, and the…
code path that is vulnerable is not used by us. This is just waiting for another release.
So… Just gonna kick off the… Update PR.
Workflow here, and, hoping to get the release out soon.
For a controversial.
And this is actually… I don't know.
before.
Let's see…
Right.
This one here, it's AWS… the MODP traces split with other services after instrumented for… London.js application, this layer.
Lots of moving parts, it seems.
Application has interactions with…
Lovely people praises.
split between… Dash.
Have any initial guess of what might be wrong?
I guess it's just not using the correct context, though…
I'm not sure.
I guess this is most likely an AWS SDK thing,
Since… redesign MySQL seems to be working. The only thing left is,
there's something wrong in the DynamoDP instrumentation, which is part of the AWS SDK package.
That looks fairly standard.
the Lambda instrumentation.
Or the other things, they haven't turned off any… Okay, just predicted.
Jamie Danielson 00:40:39 Wait, I'm… There's another issue, 3304.
By the same person?
That's clo- oh, so maybe this is a new issue following up?
Okay, this is just a new issue.
So, like, We helped them with their original issue, and now this is a follow-up.
So, nevermind.
Marc Pichler (Dynatrace) 00:41:15 So… The problem that they were having before is they had no traces at all.
Jamie Danielson 00:41:21 Yeah, and so they got that working now with the collector, but now they're having the two trace IDs. So, I was like, I thought this sounded familiar, and I was trying to figure out why, but it's a… it's a new issue, so…
Marc Pichler (Dynatrace) 00:41:36 Yeah, I will ping, transcend on this one.
And, there was not a owner's where…
Trent Mick 00:41:54 Really also perhaps has to… A user to provide more details, like… what is…
Because he's talking about tracing from lambda to lambda, right?
Isn't that in there?
Jamie Danielson 00:42:07 Yeah.
Trent Mick 00:42:08 What is, you know, the bottom part?
Well, bit.
what are your Lambda setups? Like, what's the call in one Lambda to the other one? Is it via…
Marc Pichler (Dynatrace) 00:42:21 Alright, might be something that's not instrumented.
Trent Mick 00:42:30 Is that an HTTP trigger call to the other one, or is the…
trigger on a DynamoDB edition, or something else.
And it… Yeah, it could be a path that's not instrumented, or…
A trigger path that isn't actually supported for carrying context across.
Here's a second ask.
I'll add a comment.
Marc Pichler (Dynatrace) 00:43:06 Yeah, it seems here that…
Specific questions where… I seem to remember that,
There was something.
Wrong with propagation?
in lambdas.
I'm fine.
Anyway, let's see what they come back with, here.
Jamie Danielson 00:43:55 Thank you for typing up the comment.
3, 2, 1, 9… Looks like an issue for…
Something was fixed in the Lambda Node.js layer.
version.
Marc Pichler (Dynatrace) 00:45:08 I'll have to look into that a bit more, what actually happened here.
S, let's move on to the next one.
Also AWS Lambda.
Not working for… and also not using layers.
Works fine with no chest when it… so this looks now similar to…
Be interested.
Looked in to know this is a different one as well.
Oh, but that seems to be fixed already.
I'll just send a box of the thing.
Fix… Do we need to worry about this? I would say yes.
It's a reproducer here.
It'd be that the thing before was not bundled, and now it is?
Anyway, I will put the AWS, and there's fermentation labor on here.
I don't have any… input right now, that I can… No, it.
Or take some time, to look into this.
problems later on. Seems to be everything kind of related to each other, and might have been fixed somewhere already, but, difficult to tell from just looking at it right here.
I guess we'll move on to the next one, and… Look at that.
I guess we said that we are going to…
Put this on hold for now.
This is essentially CI, problems.
We have, like, an internal label on here.
David Luna Bistuer 00:49:34 You can assign it to me, Mark.
I'm already working on that.
Marc Pichler (Dynatrace) 00:49:39 Great, thank you.
David Luna Bistuer 00:49:43 So there is a… there is a PR on…
Actually, well, it varies for something else, it's just optimize, start faster the CI, but also
It changes the value of the cash.
So, basically, TLDR is, like, the cache for compiling is just one day.
And if you want to rebrand the…
the… a failing job on the next day, the guys is not there. So, testing fails because there is no…
There's no copulation result.
Marc Pichler (Dynatrace) 00:50:15 So we can, hopefully for us, it's like, there is, there is…
David Luna Bistuer 00:50:20 the caching of the GitHub, the DCI, the actions, and then there's the, artifacts cache, which is different, so…
We are kind of safe of having a higher value for the… or artifacts.
So we can, I don't know, my proposal is maybe just to have there for a week, 7 days.
And then, the… the workaround is easy, is to… Running against the hole.
CI again, and you will have the compilation cache again for 7… for 7 more days.
Marc Pichler (Dynatrace) 00:50:56 Awesome. Alright.
Trent Mick 00:50:59 To be clear, if there are trade-offs, we don't want to fix this. I'm okay with this being closed as it won't fix. It was mostly a, oh, this is a new fix.
behavior in CI because of how we're doing caching, but… Anyway, yep.
Marc Pichler (Dynatrace) 00:51:16 Thank you for, working on this. I guess this is well on track, then.
Looks like we're done for,
And with the country repo here, and then we can move on to old PR triage.
Currently, the core repo has a few more, PRs.
So…
Trent Mick 00:51:47 We gotta get up to 50? We were almost at one page for a while.
Marc Pichler (Dynatrace) 00:51:51 Yeah, the, blame the Holy Spirit.
Marylia Gutierrez 00:51:56 Holidays.
Marc Pichler (Dynatrace) 00:51:59 I came back.
Trent Mick 00:52:00 Take out holiday people, and you guys went crazy.
Marc Pichler (Dynatrace) 00:52:05 I did come back, and I opened the page, and then I immediately closed it again. Yeah.
Marylia Gutierrez 00:52:13 Apparently, bugs don't take vacation. That's sad.
Marc Pichler (Dynatrace) 00:52:22 Alright, so the first one here is…
or the metrics API that delegating Noah meter provider,
There have been some changes since I last checked this.
But… I think it's just been…
Date that's secure.
Where's the delegate meter… And the proxy meter…
Doesn't do any proxying of instruments.
I guess I'm… might as well.
While we're looking at this one.
Oh, it's a… It has, like, a delegate cage.
Or assign this to… Myself, to have another look at this.
Since I, requested the changes here.
I guess one question, to everybody on the call. Would you be,
okay with having just, delegating no op.
up to the meter level, and skip the instruments for now? Or,
Would you rather have all of them at once?
The reason why I put my changes requested review on here was that I,
think that just having the meter be delegating and not the instruments themselves also be delegating, is…
a bit of a confusing behavior, because if you have obtained the meter before registering, then that will work. You will be able to create instruments from it, but if you obtain the instrument.
Already, and then register a new meter provider, then you won't have your, instrument updated.
And it would just continue to not work.
I'm not sure if that made any sense, what I was just saying.
Trent Mick 00:55:08 No, that makes sense. So there are two cases. One is instrumentations and what they should… well, okay, I mean…
You can slices different ways, but… so instrumentations that have metrics.
And I think typically, at least for the internal ones, we have that Kind of semi-gross… Internal method for…
The meter providers changed, re…
Marc Pichler (Dynatrace) 00:55:30 Re-up your instruments, basically, right?
Or is that meters, even?
Trent Mick 00:55:35 Okay. And then the other case is…
user code that's using their own custom metrics, and whether they would be aware. The meter provider
Is… how dynamic is this thing gonna be, or is it only… is it set when we do SDK start?
Marc Pichler (Dynatrace) 00:55:54 Yeah, exactly. So when we do SDK start, we set the globe, and everything that you obtain
after the start operation, will work. It should be fine.
Yeah, and everything that you get before that, won't work.
So, with this PR, you would be able to Get a meetup before registering.
after register, if you obtain an instrument, it will work.
But if you have obtained the instrument before registering, the instrument won't work.
Trent Mick 00:56:32 Do you know if the,
Becca's strict anywhere on this, or no?
Marc Pichler (Dynatrace) 00:56:38 The spec doesn't specify this, I think. This…
Unspecified behavior, if I recall correctly.
There are… like, different SDKs to different things, last time I checked.
I think Python has, like, a full delegating thing, where they, once it's updated, you get, of course, a new instrument.
But there's also one caveat, there's this,
what's it called? Like, pool, metrics or databases?
That have an up-down counter, and the instrumentations hold state.
Trent Mick 00:57:24 And…
Marc Pichler (Dynatrace) 00:57:25 if you…
Write code without having this update, function where, like, you send a signal for the internal state to reset.
Then the delegating thing will yield,
wrong metrics in the end, because you're still keeping the old state, which you wrote to a no-op instrument. So your up-down counter will always be off by a certain amount.
Anyway, I will, have a look at this again, make sure…
My assumption is correct, that this, just goes one level right now.
Yep.
Trent Mick 00:58:47 That was my memory, I don't know. I don't… Feel a little bit…
Not experienced enough with metrics to know if… we're gonna be…
Causing surprises to users if we don't do that, but…
Marc Pichler (Dynatrace) 00:59:11 I guess, people are kind of used to the state that it is in right now.
I know in the beginning, there was a lot of back and forth on, also having this for metrics, but the discussion has kind of died down.
Jamie Danielson 00:59:29 Yeah, I put a link to an issue in the spec, that Tyler Jan had created in 2023, talking about how it's underdefined in the spec for
meter provider, and each language does stuff a little bit differently, I guess.
But that's kind of just left alone. I think at some point, there was a suggestion, like, there's a suggestion on how these things should work, but…
Nothing's really… specified.
Marc Pichler (Dynatrace) 00:59:57 on.
All right, I guess we are out of time. Thank you, everybody, for joining. I'll have a look at this, meet the provider situation, and then,
Or see how we can move forward with this.
All right, then. Thank you, everybody.
Next, Mark.
Jackson-iPhone15 01:00:28 And see you next week.
David Luna Bistuer 01:00:30 Thank you. Bye.
Marc Pichler (Dynatrace) 01:00:32 the order pipe?
