SIG: Python SIG
Date: 2026-05-21
Duration: 54 minutes
============================================================

## Zoom Recording Transcript

**Riccardo Magliocchetti** 00:29 Hello.
**Liudmila Molkova** 00:33 Hello, hi, Ricardo.
**shuwpan** 00:35 Hello?
**Aaron Abbott** 02:17 Well… I'm a little late.
**Dylan Russell** 02:22 Whoa.
**Aaron Abbott** 02:27 Alright, I think I'm gonna be sharing today. I don't know if Leighton's joining, so I'll just start now.
Cool.
I guess we can wait a couple more minutes, but please add your names to the attendees list, and… Yeah, we'll give people another minute or two to join.
Alright, get started then. Let me open the triage board… I don't know, Tammy, are you around?
It's like, no.
**Dylan Russell** 04:20 I have a question about this.
Why is my PR in approved PRs that need fixes?
Which we are? It's… Bad, yeah.
This one? Details to the… Yeah.
**Aaron Abbott** 04:38 It's… possible that I… I think I moved it, with the changelog thing.
So, like, I guess, And this, you know, this mostly probably applies to approvers who have permission, but if, if it's just, like, a changelog or a merge conflict, I've been moving it to needs fixes, and feel free to just move it back to, like, ready to merge if it was there before.
Or whichever column it was in before.
**Dylan Russell** 05:05 I don't know.
**Aaron Abbott** 05:07 Oh, yeah. You should be able to click this thing here, or just drag it in the board.
**Dylan Russell** 05:14 Okay, nice.
**Aaron Abbott** 05:17 Yep, And if not, yeah, I don't know… Mike's not here this week, I don't think. He's on vacation, but we could see if we could automate some of this, because I think… that was one thing that was a little bit of a friction for me as a maintainer. I was going through this board, and then a lot of the ones here were, stuck, especially with the changelog thing that we did, where people had to update their PRs, but also just merge conflicts in general, or pre-commit, or whatever, so… Yep.
So, I guess we'll just go through… Some of the ones with no status, and I think the time box is, like, 5 minutes or something like that, so you just go until 10 after.
Work? Okay.
This is another, Another one about the flicks. This should probably be in not no status. There's no reviews yet.
And… it looks like a media left the review, but the changelog is broken, so I'm gonna move it to… Reviewed PRs, I need to fix it is okay.
**Leighton Chen** 06:32 Aaron, I think, Amidio's comment was the automated one about Tomcire.
**Emídio** 06:37 Yeah.
**Aaron Abbott** 06:38 He also left a review, right?
**Leighton Chen** 06:41 Oh, I'm a shelter.
**Aaron Abbott** 06:44 Go ahead, Amelia, sorry.
**Emídio** 06:46 No, yeah, the last comment was the automated one.
**Aaron Abbott** 06:49 Yeah.
Okay, yeah, I think we had, like, a doc, actually, that we were discussing all these, like, all these new rough lent checks that we wanted, and we were gonna decide on which ones we wanted. I don't know if… We actually did that, though.
**Emídio** 07:10 I don't think so. Like, you have a bunch of rules already, which I'm… I believe is fine.
Yeah, this is useful for catch breeds only.
Not sure if we want.
**Aaron Abbott** 07:27 Yeah, I think… Yeah, I mean, I'm in favor of most of these, but, like, I think we can… either continue the dock, or we can just go one by one. But, yeah, I… I don't know.
This is another one, this next one. It's debugger plugin rule.
So… Like, I… I… there's definitely ones that I don't think we should turn on unilaterally, but, maybe let's discuss, like, after Josh Block. It's okay.
I'm gonna move this one to the same.
**Leighton Chen** 08:02 Great question. Is everyone, contributing to, like, a Uber PR… sorry, an Uber issue, or something like that?
For the… the rough winter ones?
**Aaron Abbott** 08:16 I can check, let's see… It's this one, which is closed.
Very pleasant. Yeah.
**Emídio** 08:30 I closed because, there were, like, plenty of rules already.
And I'm more interested on having the same rules on both Ripple stories, instead of… Starting on adding new ones.
**Aaron Abbott** 08:44 Okay.
Yeah, so maybe let's just leave it… stop accepting new ones. I think if the issue is closed, it's likely we won't get more PRs.
**Emídio** 08:52 Yeah, yep.
**Aaron Abbott** 08:54 Sound good, Leighton?
**Leighton Chen** 08:55 Yeah, and I think if, people want to suggest more, we can take it on a case-by-case, but they have to open up an issue themselves. I think that's the… That's the way to go, and then we can evaluate whether or not something is important or not.
**Aaron Abbott** 09:10 Yeah, and that's… that's the thing I was mentioning, like, maybe we could start using the… This is a default one.
No, it's not.
You know, we can add a label that says, like, hey, like, somebody agreed that we should do this thing, so people don't start working on it before it's kind of agreed on in the future, but…
**Leighton Chen** 09:30 Right.
**Aaron Abbott** 09:32 Leighton, if you wanna… maybe let's add an agenda item, we can chat about that a little more.
**Leighton Chen** 09:38 Sure, yeah, yeah, I'll alert that then.
**Aaron Abbott** 09:40 Okay, cool. We'll just take one more minute, we'll go through this one, and then call it. So this one… DPAPI, instrument commit and rollback.
Yeah.
Lucas asks if it's part of the spec.
This is exactly what I meant, I guess, like, it's not clear if this contribution was accepted from the issue beforehand, and I hope this person didn't spend a lot of time if we're not gonna accept it.
Yeah, Lynn Miller raised a point.
So anyway, this one looks like it's in review already. I'll move this one, and let's go into the agenda.
Alright.
Okay, cool. Ricardo, you around? You want to talk about the release issues?
**Riccardo Magliocchetti** 10:32 Yep.
Bequit, sir?
I've been with a couple of… Release issues with 142.
The first one… It's strange, because it happened only once.
like, I haven't seen that in the following patch releases or stuff like that. That is that… I think at the… The regular expression we use to bump the version is a bit too broad.
Because, like, we don't look for, like, a space between the… The operator, and the name of the package, and so, like, For example, like, once.
for the JSON Proto something package.
The version was bumped with the plain Proto package version.
And so, like, this should be trivial, someone already opened, a co- yeah, an agent, Pr?
Either a comment there, but we can maybe… Yeah, like… agent reads the comments at Updated PR, so it's… But yeah, like… No, Ari, but I think we can take a look at this.
And then the other issues… issue I had was… With, mergeQ, not… being able to see the labels we use for pointing the CI towards, like, a branch instead of main.
You want to fix that by just ignoring the… Something in the workflow, but it's fine, but maybe, like, we can find, A proper solution for the next release.
And nonetheless.
As well.
**Aaron Abbott** 12:43 Sorry, am I muted?
No, I'm not. Oh, yeah, I think the fix I push should be okay, right? It's just, like, basically the merge queue doesn't, doesn't require any checks if we… If it detects that PR.
**Riccardo Magliocchetti** 13:06 Yeah, like… It's fine, but, like, we should probably update our workflow to do that, in advance, like, I think… Your change only did go to… to the RIS branch, right?
is not on main, like, so the next time we'll have the same issue, I think.
**Aaron Abbott** 13:27 No, I think it should be in Maine. It was the… it was, like.
**Riccardo Magliocchetti** 13:31 Yeah, right, correct.
Yeah. It was the bump of the changelog in May. Okay, so it's fine.
**Aaron Abbott** 13:38 Okay, I mean, if not, yeah, we should… we should figure it out, but I think… let me double check.
**Riccardo Magliocchetti** 13:44 Well, like, I'm trying to release a patch release, And I've seen that on the releasing document, we have a bunch of issues. Like, we still haven't updated regarding the new way we are handling changelaw.
And… yeah, should be… trivial to fix.
**Aaron Abbott** 14:08 That was this one, the releasing needs update.
**Riccardo Magliocchetti** 14:11 Yep.
**Aaron Abbott** 14:12 Okay.
**Riccardo Magliocchetti** 14:14 Yeah, like, it's not a link, but yeah.
**Aaron Abbott** 14:17 Yeah, maybe I'll update the docs, because I sent another PR.
Unless you've already done it, Ricardo.
**Riccardo Magliocchetti** 14:24 Not yet.
**Aaron Abbott** 14:26 Okay.
Great.
We talk about the, the batch release next, or…
**Riccardo Magliocchetti** 14:41 Yeah.
Yeah, I'll be quick again, like, I started releasing 142.1, actually release, with the… First issues we have, we are in this list.
It was the first time that, workflow… The backport workflow worked out of the box, thanks to the new change logo mechanism.
So… Pretty cool.
And then… yeah, we have a bunch of regression reported.
against, well… True aggression, one, I don't know.
this one?
Like, it has been a… a long issue with a lot of text for reporting an issue with the newly added random trace ID flag, In the spawn flags, in the spawn flags, yeah.
And… yeah.
I think she had to…
**Aaron Abbott** 15:45 what else we're after.
**Riccardo Magliocchetti** 15:47 Yeah, like, we had done a… like, we had an automated VR again, but it was clean, and so we merged the viewer merged it for, like, avoiding setting the flags if the parent didn't have it.
And so, yeah, like, again, I start the process for 142.1, I did the backport, I did the, the branch update, and I just need to run the release workflow.
And… yeah, like, maybe we want… Like, we want to talk about the… Issue as well? I don't know.
**Aaron Abbott** 16:37 Well, yeah, why don't you finish… I'll… maybe I'll just move it in the agenda.
I'll talk about it, but what… you mentioned the release, you still need to run the actual last step. Is there anything blocking that?
**Riccardo Magliocchetti** 16:49 Nope, just… But, yeah, I joined this, this call, so I stopped, but, yeah.
And for the other issues, one… If you can go to the notes and open the other issues, please?
Yeah, this one was a warning, like, this user is using the… transforming warnings to errors, and, like, I think we have plenty other warnings in the OpenDelemetry API, Package raised, so… but… Yeah, like, this one… like, at least, like, we can… like, the issue is because on older Python versions.
We… we raise a warning because… For cash, like, for leveraging the cash.
use, we call, like, a specific function without parameters, like, without filtering for the group.
Yeah, I think that, again, someone opened a PR.
Yeah, again, the same… Personnel Bonapierre?
And sorry if it's noisy.
And… Yeah, but I think that we can make it… Simple… Like, maybe it does… Yeah, like, the original PR was changing the… This is the full PR, or the last commit.
**Aaron Abbott** 18:34 This is the full PR.
**Riccardo Magliocchetti** 18:36 And it doesn't make any sense, the diff, as far as I can say.
Yeah, it removes a line.
Okay.
So, yeah.
I think, like.
the fix for this will be, like, the suggestion was to, I think, from… from Lucas to just… Silence the warning.
Since, like, this warning will be only for 3.10 and 3.11.
Yeah, I think the agent, took, The wrong decision by fixing this, but… Yeah, so, like, I don't think this is urgent, but…
**Aaron Abbott** 19:17 Yep.
**Riccardo Magliocchetti** 19:20 Yeah.
And the next one is from Diego.
It's… like, he proposed a PR, fixing the build of the… like, update of the proto… yeah, protocol JNJ zone.
I think it has been requested to also update the README, and I don't know if, Diego, you updated the PR in the meantime.
Yeah.
**Diego Hurtado Pimentel** 19:48 No, I haven't, Updated… updated the REME.
**Riccardo Magliocchetti** 19:57 Okay, so… Yeah.
again, like, when this is merged, I think we can also include this In an uneventual patch release again.
Yep.
That's it for me.
**Aaron Abbott** 20:15 Okay.
Awesome, thank you for, dealing with the release. I think we should talk more about the, the random trace ID flag, because we went back and forth on that, but it seems like there was a bug there, but I think there's some other issues with it, so… But yeah, we can add it to… The end of the agenda, so we'll just keep going then.
this one. Also, I… I think… Yeah, Diego, did you want to talk about JSON HTTP exporter?
**Diego Hurtado Pimentel** 20:50 Yeah, so I've been working with the… some folks on the OpenTelemetry Injector project.
And the issue we have with Python, in particular, Is that, our… Exporters use Protoboof as a dependency.
which, it's a very common dependency.
For many applications. So… We can, introduce a dependency conflict in the injector.
If we use exporters that use protocols, so.
Right now, we're trying to develop an exporter that doesn't use Prodobo.
I think Lucas already got through the PR with an exporter, a file exporter.
the… the… it uses JSON.
And I think, there is, There's a possibility to be able to order that uses OTLP.
HTTP and JSON. So, I was just curious about… If anyone here… it's already… working on that, or if I can start working on that.
**Aaron Abbott** 22:26 Dia, which one were you asking if people are working on? A JSON… sorry, a HTTP proto that doesn't depend on the protocol library?
**Diego Hurtado Pimentel** 22:33 Yeah, so, we can develop I think we can develop an OTLP, exporter that uses HTTP and JSON.
So that it encodes, the spans and metrics and everything.
inside… an HTTP request, in the body of an HTTP request as JSON, I think.
So… That won't use Protobuff, and that will help us with the injector.
So I was wondering if anyone else is already working on that, in order not to duplicate efforts?
And if not, I would like to… Work on this.
**Aaron Abbott** 23:24 Yeah, I mean, I think… I think Lucas is working on it, right? I'm trying to find the issue. Amita, you want to go?
**Emídio** 23:31 Yeah, I would say the same. I think there are at least two PRs open from Lucas. He's trying to get this measured.
But I believe we didn't, have a chance to review it.
**Diego Hurtado Pimentel** 23:45 Okay, so there's already PRs.
**Emídio** 23:48 Yeah.
**Diego Hurtado Pimentel** 23:49 From Lucas to.
**Emídio** 23:52 Yeah, I'm trying to find the exactly pure numbers to share, but…
**Diego Hurtado Pimentel** 23:57 Yeah, sorry to look… I couldn't find them. I don't know if I was… Looking… in the right place.
**Aaron Abbott** 24:09 Yeah, we probably should… clean up the issue backlog, because there's a bunch… I just had trouble when I was searching, but I think you… because you sent that other PR, Diego, you probably saw, but we generate, like, these JSON structs, and then I think the next step was to have a… we wanted to reuse the HTTP code, potentially, and then… like, the HTTP protocol, and then we could just swap the encoding implementation with JSON. So it would be, you know, have no dependencies on heard of Buffett, but… I would sync up with Lucas. I think… I don't think he's here today, though, right?
Yeah.
**Diego Hurtado Pimentel** 24:52 Yeah, I mentioned Lucas on Slack.
Message, but didn't get a reply from Lucas, but, you guys are sure that there is already a PR that implements this, this portal?
**Dylan Russell** 25:10 I don't think there's one for the exporter yet.
**Aaron Abbott** 25:15 Yeah.
**Dylan Russell** 25:18 But if you look at the PR I posted, there's… What is it?
**Aaron Abbott** 25:28 Yet.
This one?
**Dylan Russell** 25:30 Yeah, yeah.
So this… What does it do exactly?
**Aaron Abbott** 25:41 I think… I think our bookkeeping has not been great, but I know this is… this is Lucas's end goal, is to have the JSON exporter.
**Dylan Russell** 25:51 Yep.
**Aaron Abbott** 25:53 We just need to find the right issue.
**Diego Hurtado Pimentel** 25:58 I mean, there's already a PR that added OpenTelemetry, ProtoJSON, come on.
package.
That was already merged.
And, And that… I think that was a PR from Lucas, and the other PR from Lucas that is pending is, it appears that adds the OpenTelemetry Proto JSON file exporter.
**Dylan Russell** 26:30 Yeah, I'll just ping Lucas.
**Diego Hurtado Pimentel** 26:38 See if I can find Lucas as well.
Anyways, that was the question I had. I guess I'll have to check with Lucas.
Thank you.
**Aaron Abbott** 26:51 Okay.
Great. Yeah, unfortunately, I can't.
find the issue bookkeeping really, really great right now, so we should maybe take that. Let me just jot that in the notes.
And then we can move on.
So… Alright, so I added two… I think I'm gonna… go to this one first, since Manny, I saw you're on the call. Do you want to, I think we were waiting on some updates, and… maintainers, like, I tried to push changes, but I wasn't able to do it. I think because this… I've seen this before when the fork is made from main.
So it was kind of stalled, but were you able to update it? Yazdankhah,
**Mani** 27:42 Sorry about that. Yeah, I was away for a while, but I updated the conflicts. I also added the new changelog using the Tongueer format, so I think it should be good to go.
**Aaron Abbott** 27:54 Awesome, yeah. I think it's ready to emerge, yeah. Yazdankhah,
**Mani** 27:57 Thank you.
**Aaron Abbott** 27:59 Thank you, sorry for the, Back and forth, it's been. Yazdankhah,
**Mani** 28:03 Yeah, no, I was away as well, unfortunately, so… It's on me.
**Aaron Abbott** 28:10 Okay, cool. Yeah, let's get that one merged in.
I had wanted to discuss this one.
Okay, so this was the one that… We did the backport for.
And it's… it's unfortunate we don't have Lucas, but it was introduced by this PR that we… that we decided to include in the release, and we were going back and forth on some concerns about the safety of it, because… Yeah, so we checked with, like, the spec sig, we checked with the W3C, I raised, an issue, and then this is the overall issue in the spec for this feature, but basically it just adds a new trace flag.
To what gets propagated on the wire, and the result of that was if a span is sampled in random, you would see 03 in the header instead of just 01 for the sampled flag.
And it seems like a lot of downstream components, which was the concern, don't, don't support it well. They either just hardcode a check for 01, Or they look for flags that don't exist that it was expecting.
And they dropped the spins, I guess, so… That's kind of the context, but there was a, an actual bug in the PR, so that's the… that's the thing that we did in the patch release, which was this PR.
So this was if the incoming trace ID, which is obviously not chosen by the process, doesn't have the random flag.
we need to preserve that, because we have no way of knowing if it was random or not. So… That's fine, Ricardo's doing the patch fix, but I think we should probably talk about this a little more, and I'm kind of inclined maybe to reopen this issue, or slightly differently, because… No response yet, but basically, like.
the… let's see if I can find it… Yeah, the user reported, like, several APM backends, homegrown collectors, treat… 002, as an unknown flag suddenly dropped the spins they receive. So… like, the original concern was they parse for, like, a specific number instead of actually just checking the bitmask, so… I guess Go has already implemented this as well, and it wasn't an issue, but I think… if it's true that APM backends and collectors drop these spans, if the span originates in a Python process running this code, it would get the sampled flag, and then we would have, issues where the spans get dropped, so… Yeah, that's… that's kind of the context. I'll probably… I don't know, we should probably share this feedback with the spec, at a minimum, because there was this issue.
Let's see if I can find it.
Sorry.
**Dylan Russell** 31:23 Isn't the flag on the trace parent header? Why is… why are spans involved?
**Aaron Abbott** 31:29 So they… we record the flags in the spans in OTLP as well.
**Dylan Russell** 31:35 Okay.
**Aaron Abbott** 31:42 So this is, like, the kind of upstream spec, and basically we're just looking for feedback that this thing could be implemented.
So yeah, my, like, my understanding was this was always intended to be not a breaking change, and… if what I'm understanding from the issue is correct, like, if a user was sending traces originating from Python.
It would have those trace flags, and it would break a sizable portion of the ecosystem, so… Yeah, I don't know if anybody has any thoughts, but I'll probably just raise that feedback to the spec.
Yep, Ricardo?
**Riccardo Magliocchetti** 32:26 Yeah, like, I agree that we should keep an eye on… on this.
And… yeah, like… If we, like, understood what the issue that the reporter had with the… They're called, like, Once we have the fix out, understand if the fix was enough, or… Or something else?
And maybe, like, when also we have more information on what the backend is.
And then I think we can revise, it eventually revert if, we have back hands, but we misbehave.
But, yep.
**Aaron Abbott** 33:09 That sounds good.
Yeah, and I guess another option is we, like, the propagator behavior is kind of separate from the exporter, so we could… potentially add an option in the OTLP exporter to only support the sampled flag in, what we record in spins, like what Dylan was asking, like, why is this affecting collectors downstream?
Okay, cool. Well, if no one has thoughts, maybe I'll just, take care of that offline.
And… yeah.
Alright, Leighton, do you want to talk about this one?
**Leighton Chen** 33:54 Hmm.
Yeah, I actually need to drop in a bit, but, we can discuss this real quick.
Yeah, I think this was from the earlier discussion, and as well, kind of several PRs that Aaron and I have noticed.
that… There's some… there are some issues that are open that, There's no approvers or maintainer, feedback on… Prior to… The original… contributor, creating a PR for it.
Now, we always, like, encourage contribution, and we don't want to, you know, turn people away or anything, but there are cases in which, it's leading to, kind of.
just… additional PRs that sometimes aren't the… kind of direction that we want to go with. So… Aaron and I have noticed, like, a couple of these instances, so perhaps we should just very simply… Have an automation for, like, op… labeling something with a PR, sorry, labeling an issue with a, specific label, and… enforcing that PR is, like, Need to refer to an issue with that label, or something of that nature.
To kind of prevent this, spamming of PRs that are not approved yet, so… or sorry, a spamming of issues that aren't approved yet.
**Aaron Abbott** 35:30 Yep.
I think, like, in particular with, like, what Ricardo noticed was there's bots that are just going around and looking at issues and sending PRs, and… it would be nice… I don't know, we could put it in AgentsMD, because I don't know if we could stop the bots, but… It would… it would be good to tell the bots that they can't proceed until there's some kind of, you know.
feedback on the issue. But also, like, I feel bad when people… I feel even worse when somebody spends a bunch of time on a PR, so I… we talked about this one last week.
Can open it again.
So I think we're… this is also being discussed, like, in the spec, But, like, there's this issue… I think, Tammy, we discussed it a little bit, but there was no, like, clear approval that we would want the solution that was proposed, so… it's fine for people to send draft PRs, but I just feel bad when Sorry, I'm not even sharing it. I feel bad when people spend a lot of time on something, so this one… Does this kind of dynamic recursive split batches and retries if the payload is too large.
Which, you know, it's… It's cool, but it's probably not… the right solution. Like, it would be nice if the client and the server just knew what the limit was, and they could, you know.
And that's the thing we're discussing in this fight. So, that one's just an example, but… Yeah, go ahead, Ricardo.
**Riccardo Magliocchetti** 36:59 Yeah, like… I'm not sure it will solve the issue.
But I think that our contributing, pile could use some love.
Because, like, I think it… does too many stuff, and I guess with, new contributors, so we just keep it.
And… And yeah, like, maybe we can… You know, make it the… You know, separate the topics more in different files, so that it's clear that we prefer, like.
To have issues, discussing the issue before having an implementation.
But again, like, I don't know how many people will read that file anyways.
**Aaron Abbott** 37:56 Okay, so you just… you mentioned, like, it's too long, Ricardo?
**Riccardo Magliocchetti** 38:01 Yeah, I think we have, like.
Really, a lot of different topics.
Interesting to different people.
like, I think we have some, like, maintainer-specific stuff, we have some PR-specific stuff.
Good, meet up.
**Liudmila Molkova** 38:21 Yeah, I kinda agree with it. I think we have two ways to communicate to contributors.
that can be… I don't know, more successful? The first one, AgentsMD, is that they're communicating to agents.
people use, and probably everybody… well, a lot of people, I think, use agents to work. The second one is, the Copilot instructions are actually not bad, so if we can put a few important things in Copilot instructions and have the Copilot to review PRs automatically.
Then, at least contributors would get the practice-related feedback immediately.
And it's also easier for maintainers, because it's hard to believe.
It's, difficult feedback to… break your PRs and repeat it over and over again with… a lot of people. So, like, if we can automate this.
Two things, we can reach people, more people, and, at least give them faster feedback.
**Aaron Abbott** 39:45 Yeah.
Agreed. I was gonna share also, like, I'm sure many of you have seen this, but this is for, like, the OTEL SEMCOM repo. They have, you know, kind of exactly what we're discussing, and this is more implementation details, but there's, like, very specific labels that communicate, which are automatically added and communicate to the user what is gonna happen with the issue. So, you know, like, it gets sorted to a product, to a person, which we probably don't need in our repo, because it's a little bit smaller. There's all this stuff, but I think there's a… is a ready label, which tells people, hey, this thing is ready for a contribution. Or, like, we accept the general idea of this semantic convention, so… I don't know if we want to reuse this automation, because we probably don't have as much complication, but, like, this is the kind of thing I was thinking. We just need Yeah, it will say, like, you know, somebody needs to… approve it, or, you know, like, we decline this idea, or whatever, so… Share this in the notes.
Oh, yeah.
Any other thoughts, or… Okay, I think Leighton probably dropped, so… In papercloth.
Alright, so maybe, maybe we can, I don't know if we have somebody to own this right now.
Maybe I'll chat with Leighton offline and see if that's something he would take on.
Okay, let's go on to the next one. Keith.
Iran?
**Keith Decker** 41:39 Just call-outs for additional reviews on retrieval invocations. We missed that with adding all the types to GenAIOTILS, so, thank you, Libila, for your feedback, and, yeah, look for another one.
**Aaron Abbott** 41:55 Cool.
Looks like we hadn't reviewed, so… Anything…
**Keith Decker** 42:07 Oh yeah, pink.
**Aaron Abbott** 42:08 Yeah, yeah, sure. Anything important to discuss here, or is it pretty… It's.
**Keith Decker** 42:13 Pretty straightforward. It's just the type and the API methods for it.
**Dylan Russell** 42:19 Did you get rid of… Oh yeah, let's… I don't think we should be using any anymore.
like… and get metric attributes, I think we should replace that with, like, the attribute value.
**Aaron Abbott** 42:35 Yep.
**Keith Decker** 42:36 Okay, I'll go take care of that.
**Liudmila Molkova** 42:39 Can… can we link it?
**Dylan Russell** 42:44 Say it again?
**Liudmila Molkova** 42:45 Can we have a winter?
**Aaron Abbott** 42:50 Yeah, let's put it in the co-pilot, that's probably the easiest thing.
**Liudmila Molkova** 42:55 And we can't put it in Copilot, can we have a deterministic winter?
Can we make a winter?
Fire on it.
**Aaron Abbott** 43:08 Maybe? I mean, the thing is, like, any is still valid in some cases. I think there is probably a linter for this.
**Liudmila Molkova** 43:14 Oh, okay, wh-what… what is… Like, when we do an attribute value, it should be an attribute value instead of any? Is this the rule?
**Aaron Abbott** 43:27 Yep.
**Liudmila Molkova** 43:28 Cool, okay.
And I'll create an issue so we resolve.
Booker something out.
**Dylan Russell** 43:38 Yeah, I was gonna go through and change… all, like, the existing, because I think there's a bunch of pre-existing anys that I was gonna… Yeah, go change.
**Keith Decker** 43:49 Okay, yeah, I'll fix them in this one, and then we can make other PRs for the other types.
**Dylan Russell** 43:55 Is any ever valid? Do we ever want to see any?
At all.
I think that's a good question.
**Keith Decker** 44:02 We have… We have the generic value, right? That's the fallback that is kind of a wrap around any?
**Dylan Russell** 44:11 But I don't think we should allow that either.
Because any is, like, how do we serialize any into the proto?
Like, it's… The instrumentation?
**Liudmila Molkova** 44:23 logic, and we will extend it for others. Oh, the attribute value, I see, yeah.
**Dylan Russell** 44:32 Yeah, I'm saying, like, Any, we don't know. We can't serialize any, because we don't know how… We don't know what it is.
So I think instrumentations should never pass any to this.
**Aaron Abbott** 44:46 Yeah.
**Dylan Russell** 44:47 Basically, yeah.
**Aaron Abbott** 44:49 Yeah, I mean, it should be, like, somewhere in the type checker, you have to tell it this… this supports attribute value, or… excuse me, it would be complaining.
Unless there's a case where it's not sound, because, you know, we could kind of dig through the code and try to figure it out.
But yeah, like, this one is string any.
And then we call… set, set attributes. So, for some reason, you know, the type checker is not checking that this… Sorry, the next call, next line, this one.
**Dylan Russell** 45:23 Right.
Kind of related to this, are we planning to switch this out to… Like, the new extended attributes?
**Liudmila Molkova** 45:49 Do we support them in Python already?
for everything. Spans, metrics.
**Dylan Russell** 45:59 What do you mean by support?
**Liudmila Molkova** 46:04 So, a few months ago, At least, maybe a year ago, the… any, like, extended attributes, any… We're only supported on logs, and not on spans and metrics.
And…
**Dylan Russell** 46:23 Why weren't they supported, though? What does that mean?
**Liudmila Molkova** 46:26 the SPAC didn't allow it, but now SPAC allows it, and I had a PR to support them everywhere.
I cannot volunteer to resurrect this PR in any foreseeable time, but if somebody else wants to, it would be amazing.
**Dylan Russell** 46:45 Okay, I might, I might do it.
**Aaron Abbott** 46:48 Yeah.
**Liudmila Molkova** 46:49 Nice.
**Aaron Abbott** 46:53 Well, I think, you see this? Yeah, I'm sharing the right thing.
I think the gist of it is we have this one, which is probably used in the logs, types, and then we have this one, but then there's also some validation that probably needs to be loosened.
I vaguely remember, maybe we did do it, but, Need to dig in a little bit more. Events, blah blah blah.
attributes… Yeah, but thank you, Don, that would be great.
**Dylan Russell** 47:25 Cool.
**Aaron Abbott** 47:27 Cool.
Alright.
Anything else on that one? It's the end of the agenda, actually.
**Keith Decker** 47:42 No.
Thanks for that feedback.
**Liudmila Molkova** 47:45 Oh, quick question, Keith, are you going, or somebody else, is going to start using this API from, I don't think, LinkChain?
**Keith Decker** 47:57 I think we were originally looking at adding this for Weeviate, and… I think there was one in Langchina. I don't know off the top of my head, I'd have to go look at our, or Splunk.
Distro version of it.
**Liudmila Molkova** 48:16 Okay.
I'm just curious, like, what, like… You folks added a bunch of things into the UTLs, which is amazing, and you're working on LinkedIn, just curious what's coming next, what do… what else do we need in utility also in the instrumentations?
**Keith Decker** 48:37 Yeah, I will, keep you updated on that.
I know I was just… I'm working on getting all the types in right now, so…
**Liudmila Molkova** 48:44 Okay, cool. Thank you.
**Keith Decker** 48:47 Yep.
**Aaron Abbott** 48:56 Alright, that's the end of the agenda, so I guess we can call it there. Get 11 minutes back. Yazdankhah,
**Mani** 49:02 Sorry, I had a question. I have some issues to fix on my PR, but is there a way for me to trigger the CI tasks directly?
I don't think I have permission.
**Aaron Abbott** 49:12 Yeah, I think because you're… because it's your first PR, you can't, but after this one has merged, any contributions, it would automatically run, I think. You can just, you know, ping me if you need or something, but… Yazdankhah,
**Mani** 49:25 Sure, I'll fix them tonight, and I'll ping you.
**Aaron Abbott** 49:27 Okay.
Okay, cool.
**Dylan Russell** 49:32 Alright.
**Aaron Abbott** 49:33 Thank you all. Later.
**Liudmila Molkova** 49:35 Thank you.
