SIG: JavaScript SIG
Date: 2026-02-25
Duration: 59 minutes
Zoom Recording URL: https://zoom.us/rec/share/iMaZfuHwYVFqhPETLthKKhgMZm6SvxGDwuv9qzSdaFJvor23X-XerqUp2lnO0q4f.ry2DzBdf1F421JGZ
============================================================

## Zoom Recording Transcript

**Marc Pichler (Dynatrace)** 00:22 Hello!
**Trent Mick** 00:25 Ace.
**Andrei Borza (Sentry)** 00:25 Hello!
**Trent Mick** 00:29 Short meeting today?
**Marc Pichler (Dynatrace)** 00:31 It looks like it.
**Trent Mick** 00:35 I mean, spend hours going through bugs.
Nice.
**Andrei Borza (Sentry)** 00:47 Boom.
**Marc Pichler (Dynatrace)** 01:13 No topics for today.
**Marylia Gutierrez** 01:18 I was just… I was just about to put one. That is just a question if we… well, let me put the… about that node, PR?
Do we want to have a discussion, like, here? Because I can then talk to the person To ask them to join one of the SIGs, or if you want to have another place to talk about.
Anything that would help here?
**Marc Pichler (Dynatrace)** 01:44 I don't know, Trent, do you want to…
**Trent Mick** 01:48 Yeah, I can… well, I can say something.
**Marc Pichler (Dynatrace)** 01:50 Yeah.
**Trent Mick** 01:51 So, maintainers discussed a little bit, legendicus… Cheng Zhong was gonna reach out to the… EC or the GC, to discuss there.
Chin Zong is also on the… the Node's Technical Steering Committee.
So it's nice to have someone who has ears on both sides of that. So, I would say he's probably point, from our point of view, on that, and he said he was gonna reach out.
Also, in mid-April, March, so, yeah, not too far away, there's a Node.js Collaborator Summit in London for one day, and, Chen Zhong was… Scheduled a, alright, so the proposal, the system that they have for… for getting those scheduled for that, to have a discussion of this… PR, or the idea of having, OTEL support in NodeCore. So, his, his view is that, there probably won't be much movement on that node core PR until then, because they would basically defer until they have face-to-face discussion in the CoLab Summit there.
So I think things are happening, but, I mean, certainly we can answer questions here or discuss it, if you like.
**Marylia Gutierrez** 03:08 I was more because, yeah, I saw this… that was the input for April, but I was like, is that person, like, the author, are they okay with waiting for, like, 2 months to have any feedback on this? Or…
**Trent Mick** 03:21 So, Bengal there, that's Brian English. Yeah, I mean, I think so. He, if you read down some to the comments, his second response there was saying that, yeah, he does intend to have some Have it not be a fork, so have, I'm failing English here. Some level of compatibility there, and Ed said that there'd be subsequent PRs and things. So, my expectation is that or my understanding, though I'm not a Node core guy, is that there'll be… a lot more discussion and maybe other follow-up PRs before.
This really goes any further. Bet.
**Marylia Gutierrez** 04:05 Okay, so yeah, I don't… I don't need to… Well, in case he has questions, I can tell him, he can reach out, but otherwise… I guess it's being handled, but yeah, if I can help in any way, just let me know.
**Trent Mick** 04:18 Okay, yeah, that's great. I would expect you to hear from… from Chenso. That was… it was only earlier today that maintainers have discussed it, so… Yeah, yeah.
And it's… this is… from my understanding, asking Chenzong, that this is not in a state that's going to get merged anytime soon. So the… it does have one approval from Stephen Belanger, but that doesn't mean that it would get in, so that's an approval from a collaborator, but not someone on the TSC, and my understanding of the node process, is that adding a new module is significant enough that it would require two approvals from TSC members to get through, and there's still open discussions going on, and so this is… yeah, it's something that I think it would be expected to take time, because it's a pretty… it would be a significant addition to notes, so they're… they're not gonna… have a PR come in, and 3 days later.
**Marylia Gutierrez** 05:14 Merchanting.
**Trent Mick** 05:15 Yeah, so, yeah. It's super interesting, though, so if people are interested at all, just take a look or play with it, so… There's a potential future there where there's… I mean… one would hope some interoperability between, but some level of OTEL support in NodeCore, which could be cool.
But yeah, it's definitely the thing that happened this week in JS.
Hotel. Definitely.
**Marc Pichler (Dynatrace)** 05:58 Yes, and, there's going to be this, collaborator summit, and one thing, I think I mentioned to you, Marilla, is that, Probably also makes sense to have maybe somebody from the TC or the GC there.
To represent the project as a whole, not just the JavaScript side. I'm not sure if we have any… anybody in the area, who could take that, because I know London is quite far away for you.
**Marylia Gutierrez** 06:30 Yeah, I can't take a look with any of them, because yeah, we have a few people in Europe, but yeah, I can… Bring out to the rest of the group.
**Marc Pichler (Dynatrace)** 06:42 Yeah, I think the… one of the things that might come up is, like, trademark discussions and stuff like that.
Because the OpenTelemetry trademark still exists, and Making sure they don't get into trouble with that. It's probably a good idea.
**Trent Mick** 07:06 Though there is a degree to which, in my understanding, I haven't… I probably haven't read cover to cover all the hotel-related things for this, but there's a degree to which this is a good thing for Hotel, in that they… they want open telemetry to be… A thing that is, Used by the various languages. So, as long as this doesn't require… Result in kind of a hard fork and bifurcation of the community, then it's… it's probably a pretty good thing.
**Marc Pichler (Dynatrace)** 07:48 Does anybody want to discuss further? We have a lot of… time today to discuss. There's not much else on the agenda, so… If not, yeah, feel free to head on over to the, PR and check that one out, and, yeah.
Then we can discuss further in the coming weeks.
Oh, I see somebody typing releases.
**Trent Mick** 08:23 Well, that's me, I… Duriously.
Had you, just to know what intents are, there's a semantic conventions update, and I could do a release for SimConf. Had you intended to do releases for other things? I'm not sure what the state of various things are. I know… Contrib could probably do the release, because there are a couple of fixes recently, but…
**Marc Pichler (Dynatrace)** 08:44 Yeah, I think Contribut could do for release, looks like the last release for this was also… Oh, wow, 2 weeks ago already.
**Trent Mick** 08:53 Yeah, it wasn't too far. Oh, is it old? Okay.
**Marc Pichler (Dynatrace)** 08:57 Yeah, so I guess we could go ahead and, do another core release as well.
Where does Shick, what?
changed, and… That's the resource attributes thing.
Yeah, seems fairly… fairly small changes for this, and then also Experimental probably has a bunch more.
Pulling on.
That sort of just fixes.
**Trent Mick** 09:40 That HPP double instrumentation thing is a thing that kills… Me, at least for my case, were our… Elastics Distro.
by default, or at least in the Golden Path, enables both import in the middle and require in the middle. So the double instrumentation's kind of a killer.
But I guess, yeah, I could start a release if I wanted to.
**Marc Pichler (Dynatrace)** 10:10 Yeah, if you want, you can start a release.
And… possibly kick it off already while we're talking here, and then I can approve, the… Published still, so you don't need to wait.
**Trent Mick** 10:26 Okay, cool, I'll do that.
**Marc Pichler (Dynatrace)** 10:28 Alright.
I guess one question kind of adjacent to that is, I think we… Had a brief exchange, I don't know, on Slack, maybe, about an API release?
We haven't done one in a while, and there's, I think, actually no new features, but bug fixes and refactors.
in the API right now. Would we be comfortable to do a patch release for the API?
Usually, I'm not sure how we handle… Performance changes… activities are, put into… future territory.
But most of these should actually be… Bug fixes and internal changes.
**Trent Mick** 11:36 I guess let's not release Please Bass, so we're not stuck.
With those results. It could be a patch-level release, so… Yeah, password release, no problem.
Minor release, we have to start getting into updating.
See, the peer dependency settings, and a lot of things, right? I think you…
**Marc Pichler (Dynatrace)** 11:58 I think we have automation for that, so if we do a minor release for the API, the dependencies will update automatically.
But I'd much rather do, Patch release, in this case, because, it's… Just internal changes.
And, yeah, shouldn't… shouldn't affect the public API much. There's this change from… Any to unknown, but this is, just for the component logger and shouldn't affect any, Anything.
on compile. So, I think we should always be good with that change.
And then, I think it might also unblock the, the browser sig with the… console instrumentation.
Because it has this, fix in here, too.
Keep the original console methods before they're instrumented.
**Trent Mick** 13:09 Yeah, I guess that would help the instrumentation console.
If they wanted to use that.
Yep.
**Marc Pichler (Dynatrace)** 13:19 Alright.
I guess I can also, put the topic on here while we have everybody on the card. We have, I think we talked about this last week, right? There's the API 3… Not API, SDK 3.0… Discussion issue about dropping… the supported Node.js versions, and I saw, Andre here had the ask to consider not dropping, note 20, because that's, like, 50% of the installation base right now.
And I had kind of a follow-up question for that.
I'm not sure if you've seen it, yet, Andre.
**Andrei Borza (Sentry)** 14:19 Yeah.
Yeah, I've seen it, I'm trying to get that data right now.
It does look like it's on the decline, so, Note22 is definitely catching up.
But yeah, it still… it still makes a huge chunk of our installation base right now.
Yeah, I'm trying to find out how long it took after end of life of Node 18 for people to jump to Node 20.
**Marc Pichler (Dynatrace)** 14:48 Because one thing that I was, going to propose, in that case is that, Maybe if we have a good idea of what the behavior looks like of users moving to the new Node.js version. We could delay, when we do the 3.0 release, to a place where we feel somewhat comfortable that, it's not gonna… like, drop support for, like, half the user base, but something lower than that, I guess would still be subject to defining, like, what the threshold is where we feel comfortable doing that.
**Andrei Borza (Sentry)** 15:31 Yeah, that sounds like a nice compromise there.
I'll get back to you with some more data.
**Marc Pichler (Dynatrace)** 15:41 Good, thank you.
**Andrei Borza (Sentry)** 15:42 Yeah, thank you so much.
**Marc Pichler (Dynatrace)** 15:44 Yeah, on the… on the O2.js side, unfortunately, we don't have any… any telemetry about our users ourselves, so.
**Andrei Borza (Sentry)** 15:54 Right.
**Marc Pichler (Dynatrace)** 15:54 getting some additional data from vendors is also good. I might also check, some internal metrics, but I need to ask another team for that.
**Andrei Borza (Sentry)** 16:07 Yeah, cool, thanks so much.
**Trent Mick** 16:10 Yeah, I suppose that it's hard… we're not really tooled up well to be doing, two maintenance branches either, right? To still be doing Even security releases for… What is the setup?
2.x versions.
It's made a little bit harder because of the 0.X still for some packages, but… yeah.
**Marc Pichler (Dynatrace)** 16:32 Yeah, we do have the 1.x branch, from which we could technically do some releases if we needed to, but as you said, the tooling is not there for it, so any releases would have to be manual.
I guess one thing to look into when going to 3.0 would also be to ensure that we have some tooling in place to release from 2.X branch.
To make sure that we can deliver, security fixes and stuff like that, because that's also what the specification requires us to do, is if we go on a major version pump, then we do, security releases, essentially, for a year.
We haven't had to do that necessarily with the 1.x branch, because there were no, Varnerabilities in our code, so we didn't need to do it.
But for stuff like bug fix backports, we have… tooling in place, then it's also easier to do these.
And keep some fixes going back to the, to the next branch.
**Andrei Borza (Sentry)** 17:58 For us, this is not really necessary. We would definitely like to be on the latest major as well.
And we can just maintain our own previous major.
So, people don't actually have to update.
So I don't… I don't think that's strictly necessary for us, that you guys maintain, A previous branch.
**Marc Pichler (Dynatrace)** 18:23 Yeah, I think it's required by the spec anyway, so we should definitely look into that. But yeah, it's also good to know that you're maintaining, like, different versions there.
Yep.
Right.
**Trent Mick** 18:49 I guess we should look into which… Bits of tooling that we'd be… Like, how much pain there would be for us if we're on… If we're still supporting Node 20, like, what versions of the tooling can we not pick up then?
Maybe it's not so bad.
Next.
**Marc Pichler (Dynatrace)** 19:10 Yeah, I think for Node 20, the thing that you mentioned, a module.register, oh, register.
**Trent Mick** 19:20 Register hooked, yeah.
**Marc Pichler (Dynatrace)** 19:22 Yeah.
that… might be a big improvement that we could do. One thing that I was thinking of was also changing the exporters to use etch over HTTP.
Because that also has some benefits, especially to the way that the exporters API is structured right now.
when we use Fetch, then we would use the same, or more or less the same, across all platforms.
And not rely on load HTTP anymore.
**Trent Mick** 20:01 I like NodeHP, though.
I've been using it forever.
Yeah.
**Marc Pichler (Dynatrace)** 20:08 I don't know.
It would allow us to consolidate a lot of code, and get rid of a bunch of differences between the exporters.
We're also possibly allowing, More cross-platform compatibility.
**Trent Mick** 20:27 Here's a serious question, actually, on… if… if our node exporter was using Fetch, which he's using Indichi under the hood.
that's gonna be… I don't know if we can set it up to not instrument.
that thing, or I guess we're… we have to be relying on this suppress… Tracing working, then? Because, Like, we can't use this trick of having an uninstrumented thing that we're using, because the diagnostic channels will be emitted regardless, so there's no, kind of, Non-instrumented fetch.
**Marc Pichler (Dynatrace)** 21:02 I guess it would be similar, though, to what HTTP is doing right now, right? Yes, that's right.
**Trent Mick** 21:08 relying on suppressed tracing. Though, yeah, if you turn off the context manager, you have an infinite loop going on there, but anyway, yeah.
Yep.
Okay, interesting.
**Marc Pichler (Dynatrace)** 21:26 a tooling-wise, I don't know, if there's… anything. One thing that I always see is that, like, as, Or the Node.js version goes out of, goes into EOL, there's an uptick in, like.
dev dependencies dropping support for it, and that is then followed by an uptick in security warnings in GitHub, because we can't update these dependencies.
And it kind of drowns out old stuff. It drowns out stuff that, is new, and Yeah. Might be actually needing attention, so…
**Trent Mick** 22:12 we can…
**Marc Pichler (Dynatrace)** 22:12 with.
**Trent Mick** 22:13 Yeah, it's a… it's a royal pain, but we can probably also never really get away from it, because… I don't know. It feels like… you always want to feel like, okay, this one, finally, node 20 will be the one where everyone just, like, settles down a bit, and it's not going to have a round of everyone dropping support, but no, maybe 20… no, maybe 24, or maybe… Like, unless we do very harsh releases the day of.
No dropping support for whatever we drop support for the same thing, which is… not even just the Sentry example, but it kind of ends up being a disservice to downstream users, because then they get stuck.
So yeah.
**Marc Pichler (Dynatrace)** 22:59 Yeah, unfortunately, there's some time until we will do the reader or release, so we can still look at the data and discuss, and then make a decision based on the data.
**Trent Mick** 23:12 Yep.
**Marc Pichler (Dynatrace)** 23:15 Right?
As if there are no more topics… And we can hope.
Onto the favorite.
Topic of everybody on the call here, which is bug triage, and… OTPR triage. Seems like nothing here on… Core, and then, there's a few things in… contrib… I guess this one will be solved by another release.
**Trent Mick** 24:03 I think that'll be solved by the contributor.
**Marc Pichler (Dynatrace)** 24:06 Absolutely.
**Trent Mick** 24:06 Right now, we've already updated, yeah.
**Marc Pichler (Dynatrace)** 24:09 Yeah, I was, just looking for… I keep forgetting what the header is for, linking PRs here.
**Trent Mick** 24:30 Oh, because it's already been merged. It's 3398.
**Marc Pichler (Dynatrace)** 24:36 Okay, then I'll just close this one.
**Trent Mick** 24:41 Okay, remind me, because I forget, I did the contribib release, and I got the message on the release PR that the releases have been Done, is there any follow-up I need to do?
Think, or just release, please handle everything now.
**Marc Pichler (Dynatrace)** 24:59 Yeah, release, should handle everything. I guess there's… a proof step that I still need to…
**Trent Mick** 25:09 Right, and it's probably sitting there waiting for them.
I can go find it. We'll shoot it.
**Marc Pichler (Dynatrace)** 25:16 Should be running now.
Alright.
These two are, the same. We've been carrying these with us for a bit. Looks like the person here answered.
Mmm… they will confirm with their customers and then get back here. So, this still needs both a response, and this is a similar one.
Or assign this to me.
So that I get back to looking at this.
Yeah, I guess there's nothing on the car that we can do right now, unless somebody has, run into that somewhere.
You know… Immediately.
**Trent Mick** 26:23 I had looked… I had been looking at some of the Node 24 Thanks for EW Slender. There were some fixes for this in… December, I think?
But I don't know if there's something different going on here.
**Marc Pichler (Dynatrace)** 26:41 So the fixes were in… Were they in the contribo, or in the Lambda?
**Trent Mick** 26:46 So there were fixes for using the Lambda… So, okay, in November is when AWS released the new Lambda Node 24 runtime.
And… The… or a major change in that is they changed from… they changed from using require to load the user's function to using import, so… Await imports, so now you need… the import of the middle hook active, or there to be a chance at loading the thing, but it's possible there are also other… Changes that are needed.
For loading this thing. But… what I'm kind of wondering is if this has been fixed in the interim, but no one's checked again?
But I don't know.
So, yeah, you or I taking a look.
**Marc Pichler (Dynatrace)** 27:40 Grand.
**Trent Mick** 27:41 Sorry, not that.
**Marc Pichler (Dynatrace)** 27:44 That's, that's already helping. I will… Have a look at this one.
I've recently started, having AI to reproduce us, and it has been very successful in reproducing a bunch of stuff, so… I can also get into things that I'm not usually, Close to what I work at.
Right, old PR triage is next.
We have 47 and 37, just a few less than last week.
I'll jump over a bunch of these here, because there hasn't really been a lot of movement in those… Trace Decorator… I still need to always assign this to myself, because I wanted to… write a proposal about, having API extension packages, for experimental features.
Then this is the draft… This one seems to have had some activity recently.
Looks like they actually provided, examper now.
Or this one… Seems like that's just ready for another round of reviews, then. We need to try that out and see if it actually… dusted thing.
Is the change itself is fairly small here, but, I'm not too deep into that.
**Trent Mick** 30:49 Yeah, if I remember, I think the patch looks reasonable, but I couldn't… that's asked for the repo, so maybe I can.
Right with the repo.
**Marc Pichler (Dynatrace)** 31:01 Alright.
**Trent Mick** 31:03 I'll look again.
**Marc Pichler (Dynatrace)** 31:04 Thank you.
And then we have to renovate things, which I assigned to me, but didn't get to yet.
The draft for create instrumentation… And we have here, always record sampler.
Yeah, this is interesting, so we have… This specification issue here, and… And that was added here… I wonder, is that something that, fits into the new sampler, composite sampler thing, or is that a standalone specification here.
**Carlos Alberto Cortez** 32:36 Well, a long one.
**Marc Pichler (Dynatrace)** 32:43 Oh, sorry, I think I didn't get that.
**Carlos Alberto Cortez** 32:45 Yeah, it's, it's not related to the Composite Sampler API. It's just something separated.
It's supposed to help people, you know, write custom Processors and exporters that can report on stuff that is not, being, Recorded by default, you know? So you can do internal debugging.
By the way, this is part of education is experimental.
So, yeah, and it's… it's a simple one, I would say. The only thing is that, it has… it shouldn't go to anything, to any stable package, otherwise trivial.
**Marc Pichler (Dynatrace)** 33:32 Yeah, that makes sense. I'll have a look at that one then, later on.
It is indeed trivial.
Looking at the, get the code here, it's, very compact.
Yes, so I guess, I'm not sure if there's any stabilization work for this also going on, because it would be very nice to, if we merge this as experimental, also be able to stabilize it soon.
**Carlos Alberto Cortez** 34:09 I think it got… he got accepted 2 months ago.
Something like that, so it's very recent.
So I can imagine taking at least a couple of months maybe in one month, we can go ahead, depending on the prototypes. Actually, that's a good call. It's a… it's a very straightforward simple sampler, probably can… yeah, and I saw, now that you were opening the link, that it even has a PHP prototype, so probably, actually, that's a good one. I will try to one check.
Maybe we can already start that. Two months is… I would say it's not that long ago, but then again, this component is simple enough.
**Marc Pichler (Dynatrace)** 34:53 Alright, thank you. Yeah, looks like 3 prototypes already, and then if we get ours in, that would be 4.
**Carlos Alberto Cortez** 35:02 Yep.
**Marc Pichler (Dynatrace)** 35:03 So, looks like we're in a good place there.
Nice.
Alright, I will have a look at that one then, after the car.
Alright, there's this silo monitor, which is kind of lumped into the, renovate changes as well.
I'm gonna skip that. If any PRs or anything stick out to you, please feel free to just call out, and we can look at these as well on the call. We don't need to… necessarily do the order, that I'm going through here right now.
Alright, this is instrumentation fetch.
Looks like this one actually has… Another PR that's linked… Looks like a bunch of discussion going on here.
**David Luna Bistuer** 36:37 Yeah.
I have to come back to this VR, so I did the… There was a problem with the behavior, and we were… with propagation.
yeah, sorry to make the changes, but I didn't have the chance to review it again.
**Marc Pichler (Dynatrace)** 37:01 Okay, so I guess we can, If that is just waiting for, another round. Is that correct?
**David Luna Bistuer** 37:09 Yup.
**Marc Pichler (Dynatrace)** 37:11 Alright.
Then, moving on, this one… spear… Oh, I now skipped over.
Okay. Like, what was the first one? This one here is… Grpc insecure connection guidance.
some extra information… This is actually how, like, the… just reiterating the behavior that is required by spec, if I recall correctly.
it's just doing it for the gRPC exporter, so I'll ask them if they can… but for the trace exporter, so I'll ask them if they can also do that for metrics and logs.
**Trent Mick** 38:35 I mean?
**Marc Pichler (Dynatrace)** 38:52 Alright, Then we have… Something for… the exporters again. This is a feature to add.
Fetch later transport.
I guess this would be mostly… Interesting for the processing, if I recall correctly, fetch later is not… Baseline available right now.
Yeah, limited availability…
**Trent Mick** 39:53 It's only in Chromium.
**Marc Pichler (Dynatrace)** 40:12 Yeah, looks like this, being a… Thank you.
1… Or a relatively simple change, I guess.
Now we got rid of most of the, Most of the different transports for the browser.
I'm kind of hesitant to add a new one.
But yeah, I guess, it'd be…
**Trent Mick** 40:56 Nice if this structure were such that this could be added Entirely as a separate package, without having to be integrated into all these packages.
**Marc Pichler (Dynatrace)** 41:06 Yeah.
**Trent Mick** 41:07 That's pipe dream, I think.
**Marc Pichler (Dynatrace)** 41:10 And… I'm hoping that it's not, too far off.
That was kind of the plan with the exporters in the end, was to allow the transport to be, user implementable, to… circumvent all of these feature requests that we get always, because somebody might have some runtime, some obscure runtime that doesn't support whatever we're using.
And then instead of, like, adding all of that to the exporters and, like.
make the package grow larger and larger, we would just tell them to, like, create their own package with just the transport, and then, people could use that instead.
Should also help us.
Age a little bit, like, how… How much usage it gets.
But yeah, that's definitely something that I would… Prefer, us having.
Because that then also allows for tree-shaking red, so, You don't need to, like, programmatically choose Based on some flag, which transport you use, you can just, Like, pass in the one that you need, and then get rid of all the rest.
I guess that could be, We're also maintain us here.
Let's just see if that's something that's of interest.
To your processing.
And then let's go from there.
So let's officially the transport, And we move on to my draft here. I can actually close this one if it just… Sitting too much in the way.
had this PR value, it unfortunately got still closed.
So I just opened a new one there. I closed this one so that it doesn't sit here. But what this did, in essence, is just do a prototype for whatever I was proposing on SAMConf.
Is to have this, latest experimental thing, that you could use to, like, move SEMCOM ahead of, Old and stable, and also get some experimental stuff, in there, so that we can update the instrumentations already.
Have you…
**Trent Mick** 44:37 Seen any movement on that, or discussion on that?
Because sometimes when I'm looking at Whatever features I'm looking at.
Java code is basically the first one I go to look at, because, you know, what would Jesus do?
The… they sometimes have specific config that is about Allow this experimental feature, so it's using Java system properties, or the effect of the same as environment variables, instead of… I find using this opt-in thing. I wonder if the opt-in thing is a little bit limited, because it's limited to SEMComp, right? Because SEMCOM's in the name of the environment variable, as opposed to, like, other experimental behavior that we might want to allow in this instrumentation. It's otherwise stabilized.
Don't know.
**Marc Pichler (Dynatrace)** 45:27 Yeah, I think, so… One of the things that we could always do is have, Separate environment variables for these experimental features, so outer node, experimental… Whatever, could be… One way of going about it.
unfortunately, we don't have this nice properties thing that Java has.
**Trent Mick** 45:55 But it's basically the same thing, though.
**Marc Pichler (Dynatrace)** 45:57 Yeah, it's… it's similar enough, to… be able to use that. I guess that could be one way. If we still want to go ahead with that without, having… the sameconf PR in, then, what we could do is have, like, outer node.
Semconf.
auto node, experimental semconf, and then a list of keys.
So we would do… like, experimental SEMCOMF messaging, for example.
And that would enable… So, with this, we wouldn't be… we wouldn't need to make the changes to SENCOMF to specifically allow that.
Could be one way forward, if we want to go that way.
Though I think landing the change in SAMconf… Isn't too far off.
I wasn't, no.
Practice already had the proofers.
**Trent Mick** 47:25 Okay.
**Marc Pichler (Dynatrace)** 47:26 I will try to reopen that one.
by just taking the changes, replacing them, and then opening a new PR.
And then, Let's wait for a bit longer to see if we can get that merged, and if not, then we can go ahead and, build our own.
Way of going about it.
It would be nice, though, to have this, something that's available across languages.
Because I have a feeling that it would unblock folks.
Did wanna update.
their instrumentations.
**Trent Mick** 48:05 Okay.
I guess there's already a GenAI similar one, right?
**Marc Pichler (Dynatrace)** 48:15 Yeah, the 108 one already exists.
So… Just pray out.
Then this one here is actually the draft to a PR that I have, now ready for review. I guess we could discuss this here as well. Trent, you did a lot of, performance, Tests with… the previous PR I had here. Thank you very much for doing all of that, it was a really good read to look through all those things.
the actual PR that I had then opened in the end goes a little bit of a different route, instead of… so, just for everybody who isn't aware.
Here, I just, made a change where, instead of using protobuf.js, it uses a custom protobuf, log serializer that, basically is… tailored towards OTLP directly and the internal data format that we have.
To avoid these intermediate jumps that create a lot of allocations and stuff like that.
The way that this worked was it had a 64KB buffer that it always allocated, and it just used that to write Stuff in there.
And the actual PR that I then opened does a double pass, where it first goes over the whole message to estimate, like, how large it's gonna be.
And then allocates a buffer exactly of that size, so it doesn't over-allocate. That's at the cost of some CPU cycles.
But, it avoids, like, allocating more memory than is needed.
That has the result of it not being, we could, then, the JSON serialization.
But still gets it close enough.
While giving us the ability to change it later on, which we don't have with protopuff.js at the moment, which is… A separate library, so we don't have a lot of leeway in, changing the behavior that it, that it has there. It also goes towards fixing a bug.
Or… bundle, like, bundling, where, in the browser, this, protopuff.js library violates, CSPs.
So, yeah.
I guess the question I… yeah.
**Trent Mick** 51:22 No, go ahead.
**Marc Pichler (Dynatrace)** 51:23 I guess the question I have is, do we want to go ahead with a change like that, or… Are we unsure about it?
Still, it is a lot more maintenance, I guess.
Double.
**Trent Mick** 51:37 I don't know if it's… I don't know if it's crazy more maintenance. I was thinking, like, once I got over the hump of understanding your first one, I thought, meh, this is pretty straightforward. And there are also potential paths for… Getting faster, so, like, saving the serialized buffer of the resource, because you know that's not going to change.
I didn't really have other ones. When I was doing and looking at the performance things, I didn't really notice any change one way or the other with reusing that buffer or just creating a new one every time.
And I kind of got the impression that the size of the buffer that we're talking about here is insignificant compared to the amount of memory that's otherwise being used.
By the… by the… the tooling, but I'm not super 100% confident on that. So, yeah, I don't know if the… Do you feel that double pass is necessary? Did you have any external… Measurements that showed that there was a potential memory problem, or is it just…
**Marc Pichler (Dynatrace)** 52:33 So the reason why I made the change, it was just a theoretical thing, and I wanted to make sure to keep pretty much the same behavior as Protopuff.js has. I dug into, like, how Protopuff.js handles stuff.
And it does, essentially, this upper pass.
Where it, like, estimates that, and then, like.
Allocates exactly the buffer that it needs.
So I wanted to make sure that there's no surprises.
per…
**Trent Mick** 53:07 It basically does one pass and does a count of bytes, right, that it would have… put it into the buffer, and then creates a buffer, and then goes through again and does it? Okay.
**Marc Pichler (Dynatrace)** 53:15 It… it has these, I don't know, operations that it puts onto a… I think it just collects them in an array.
And these are just functions that it then, like, goes through and cores all of them, but while it does put them onto that, array, it also keeps track of, like, how large it's gonna be.
**Trent Mick** 53:39 Okay.
**Marc Pichler (Dynatrace)** 53:40 It's actually.
**Trent Mick** 53:41 I mean, you're doing allocations for that array anyway, so I kind of wonder if you're seeing anything there. Yeah.
**Marc Pichler (Dynatrace)** 53:47 Yeah, so my example here is a bit different in the sense that it, like, avoids these allocations on the double pass.
It doesn't do a lot of smaller allocations anymore, it just, uses the same code that it would for writing to just go through, and the writer is actually an estimator, so it just, like, when you write a variant, it just estimates how large the variant is going to be.
And, then it also reuses the same code for both.
The first pass and the second pass, so that you don't need to write it twice.
Which can be mindful and error-prone.
**Trent Mick** 54:29 Okay, yeah. On the positive side, the size win of dropping the protobuf… generated code could be huge, so I think this could be… I think it could be a good one.
**Marc Pichler (Dynatrace)** 54:42 Yeah. What's going to…
**Trent Mick** 54:43 for all the signals, and then we can drop it, yeah.
**Marc Pichler (Dynatrace)** 54:48 Yeah, one thing, that I've also tried that isn't included in this PR, because otherwise it would have gotten too large, it's already quite a lot of lines of code, is that I did a deserializer, and I have that ready Tool.
Push after this is merged.
And with that, like, there's a whole chain of, like, serializing and deserializing, so for logs themselves, we don't need protobuf.js anymore, once, we have that change too. And then we can do the same for the others.
Since the response message is fairly simple.
It's not a lot of code to get this working. We only need a subset of the available features in Protopuff to read the message.
**Trent Mick** 55:43 Yes, do we only drop the protobuf?
Does… sorry, does the gRPC library still have a DEP on Protobuff? Would it still be using that? Protobuff.js?
**Marc Pichler (Dynatrace)** 55:53 It… So, the gRPC library itself, I think it has a dependency on it, but we're not using it directly.
A while ago, I made, changes, to the GRPC… exporter, so that it just uses a generic gRPC client. So it uses the same serialization and deserialization logic as the protopuff exporters.
Before that, we used, I think we used to bundle the protofires With the package, and then use this dynamic loader to generate stuff.
Which, bundlers we're very unhappy about. So, yep.
should be a drop-in replacement for gRPC as well.
**Trent Mick** 56:49 Okay, cool.
**Marc Pichler (Dynatrace)** 56:54 Right.
So, that's… The protobuf stuff.
Yeah, if anybody has any questions about this, please feel free to reach out to me. I've gotten into the weeds for this one, quite a bit, so… I can… answer pretty much any question I feel like that can come up about this.
Alright, the next one. Parse keep pairs into record.
Looks like this one is on its way to get… They are closed, I cannot, easily figure out what it's… About from the title, too.
Fixes an issue where parse key pairs in the record dropped.
Baggage key value pass.
committee values. I guess this is, somewhat related to the change… About the resources that we made recently?
**Trent Mick** 58:25 Except, didn't that change stop using the baggage?
Details.
**Marc Pichler (Dynatrace)** 58:30 I think it did, yeah.
**Trent Mick** 58:32 I can't remember.
**Marc Pichler (Dynatrace)** 58:37 I guess this mostly went under the radar, because it has such a… Bunny.
Short title… Not sure if the person… is still responding to this, or just put a comment here and ask them if… They're still working on that.
AutoComplete not working.
Right.
**Trent Mick** 59:42 We're out of 10.
**Marc Pichler (Dynatrace)** 59:45 You're right.
Alright then, thank you everybody for joining.
Have a nice week, and see you next week.
**Andrei Borza (Sentry)** 59:55 Thank you.
Damn.
