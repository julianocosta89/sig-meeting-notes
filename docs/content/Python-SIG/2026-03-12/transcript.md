SIG: Python SIG
Date: 2026-03-12
Duration: 46 minutes
Zoom Recording URL: https://zoom.us/rec/share/nH7__dcSkZTRRS0IkRtFsYjPB7i3VDO0aWmwtQ3z8uDIKZLr06V3xS74LC8tKIk2.PkvCit8-8uleBa8q
============================================================

## Zoom Recording Transcript

**Aaron Abbott** 06:39 Is it going?
**Surya Teja** 06:49 Hi folks, how is everyone doing?
**Aaron Abbott** 06:53 Pretty good.
We can give it a couple more minutes for people to join.
I think Ricardo will be coming a little bit late, he said.
So let me just share the meeting notes.
Yeah, and folks, please add your… Items to the agenda.
Okay, should we get into it?
I don't think Tammy's around for, this triage, right?
No.
It's okay.
Can folks hear me and see my screen alright?
**lechen** 10:21 Yeah, okay.
**Liudmila Molkova** 10:21 Yes, Fed.
**Keith Decker** 10:22 Yep.
**Aaron Abbott** 10:24 Okay, great.
So, can somebody remind me what we usually do here?
I think this is a pretty new thing, and Tammy's been doing it. Should we just go through, the ones with no status?
**lechen** 10:42 Yeah, does Tammy usually run these?
I haven't…
**Aaron Abbott** 10:45 I think this is, like, Second or third time we're doing it.
**lechen** 10:48 Yeah, okay.
**Aaron Abbott** 10:52 Yeah, what was… Okay.
**lechen** 10:57 Filter for steel versus non-steel and burden.
**Aaron Abbott** 11:00 Why is this not opening in this sidebar here?
That's weird.
Refresh it.
**lechen** 11:13 So, it's strictly for triaging, right? Not for, like, asking for reviews or anything?
this…
**Aaron Abbott** 11:20 Yeah, this is the triage.
I don't know.
Did they change this in GitHub, where it won't open on the side?
Man, this UI got a lot more complicated. Alright, I guess I'll just open them and go like this. Alright, that's Dependabot. Let's just ignore that one for now.
**lechen** 11:49 I think.
**Aaron Abbott** 11:54 What's up, Clayton?
**lechen** 11:55 Oh, nothing, sir.
**Aaron Abbott** 11:58 Okay, looks like this one's already got two approvals, so I'm gonna… Move it to… Are you… We're ready for review, I guess? Yeah.
Sorry, this is approved.
Damn.
Add log handler configuration to auto instrumentation.
Looks like we've got some reviews here, I'm gonna put it in ready for review.
Nice, yeah.
**lechen** 12:43 I guess Pablo left some comments, do we have context if there's Oprah waiting on something?
**Aaron Abbott** 12:51 On that.
**lechen** 12:53 Yeah.
**Aaron Abbott** 12:55 I mean, it looks like… looks like Josh updated, addressed all the comments, so I think he's just waiting for another review.
**lechen** 13:02 Okay.
Sounds good.
**Aaron Abbott** 13:04 can, Hit those buttons.
And this is really painful when the sidebar doesn't open.
Yeah.
Alright, I think.
**Surya Teja** 13:25 Yeah, that was my shameless plug, because I'm completely new to async evade stuff.
And, I think I might, have, I might need some expert guidance on how I structure the code.
So just calling it here because people who are familiar with, the async event stuff in Python can chime in and correct me if I made any mistakes, or refine this a little bit better to make it more readable and stuff.
**Aaron Abbott** 13:57 Okay. Did you have it in the agenda, too? We can chat about it then.
**Surya Teja** 13:59 Yeah, I added this in the agenda quite early, so you can, Please remove it if, as this is addressed.
**Aaron Abbott** 14:10 Okay, sure, sure.
Yeah, we'll take a look at this one. It looks like it's got some reviews, just need a little more feedback.
**Surya Teja** 14:16 Yeah, I mean, it's not super urgent, people can take a look whenever they get time.
But thanks a lot.
**Aaron Abbott** 14:27 So, next one, replacePixMe for flags.
Alright, I'm gonna put this in easy to review, more lines.
**Lukas** 14:35 I think, actually, this one might be blocked. I thought that there… maybe I'm thinking of a different PR, but I think… Can you scroll down? See if there's comments?
**Aaron Abbott** 14:46 Oh.
**Lukas** 14:50 Yeah, this probably needs… we probably need to merge… there's some changes to add metric data point flags, so I don't know if you want to wait for that.
**Aaron Abbott** 15:03 Yeah, that sounds good, I don't think this one's urgent.
It doesn't look like we have a, blocked… Column in here, anyway.
**Lukas** 15:14 I mean, maybe reviewed PRs that need fixes, I don't know.
**lechen** 15:19 Octopus.
**Liudmila Molkova** 15:23 It's kind of cool to have blocked columns so that it's easy to know what to… Spend time on during… the calls.
**Aaron Abbott** 15:33 Yeah.
**lechen** 15:35 That's true.
**Aaron Abbott** 15:36 Let me just leave a note here.
Alright, maybe we'll just spend, like, another… Two minutes on this, see how many more we can get through.
Right, this one has no reviews, checks billing, I think this is some self-observability metrics.
Which is something we should definitely get in. It's, like, 158 lines…
**lechen** 16:13 Yeah.
I get to work.
**Aaron Abbott** 16:17 Okay, I'm gonna put it as easy to review, maybe.
looks relatively easy. I don't know if, The only thing here I'm not super sure about is, like, you know.
stability of these metrics, since they're kind of just directly in the SDK.
**lechen** 16:32 Right.
**Aaron Abbott** 16:36 Okay.
Yeah.
This is another dependable bot, I'm just gonna leave it.
Another Dependabot, and then this was the last one.
Layton, do you wanna… this one looks pretty easy.
**lechen** 16:53 Oh, yeah, I just created that. It's pretty… pretty straightforward.
**Aaron Abbott** 16:58 Alright.
Cool.
**lechen** 17:01 Nice.
**Aaron Abbott** 17:02 Let's go into the agenda agenda, then.
Keith, you're on?
**Keith Decker** 17:10 Yeah, looking to add the types for, like, server tool call request and response, as well as updating the old GenAI Utils tool call to match tool call request and response. These are just type changes in Gen AI Utils with the corresponding instrumentation updates to To align them.
And then, implementation of, like, start tool call, stop tool call, and that kind of stuff will be coming after this.
**Aaron Abbott** 17:37 Cool. Still looking for reviews, yeah.
**Liudmila Molkova** 17:41 I think this is related to the discussion we are about to have. I see it on the agenda about the release changes.
It sounds like, since it's a braking change, and it would modify pretty much every instrumentation.
It… we should release them together.
Otherwise, what's going to happen that instrumentations that are… if you're religion AI, and some instrumentation, then… the rest of them will become incompatible with it, right? They depend on the… on different APIs and GenAIO tools.
**Keith Decker** 18:16 So the instrumentations in contribib are just using them as types, and the tool call type still exists and has the same fields as tool call request. And so the tests are showing that they are still running with Too cool.
We can take a look at that.
**Liudmila Molkova** 18:35 Oh, okay, interesting.
**Keith Decker** 18:38 So they're not… there's no APIs that they're actually calling, they're just using the classes to… to form the… what eventually becomes the JSON.
**Liudmila Molkova** 18:49 So when, let's see, I don't know, Google Gen AI, switches that it uses to call, because it's data class, it doesn't matter.
the API name doesn't matter.
**Keith Decker** 19:04 I have not tested, though, if… Gen AI… UTILS releases before the instrumentation.
Dates. That's an interesting point.
**Liudmila Molkova** 19:17 I mean, you… we release Gen AI, let's say we release, OpenAI.
And then… Somebody uses instrumentation for balls open AI and Google Gen AI.
They could not agree on the version of GenAIOTOS.
**Aaron Abbott** 19:35 Yeah.
Basically a conflict, yeah.
**Liudmila Molkova** 19:45 Yeah, so.
**Keith Decker** 19:46 We will not.
table is till we have that discussion on release stuff. Go through the other ones, then.
**Liudmila Molkova** 19:52 Yeah.
**Keith Decker** 19:52 Come back to this.
**Liudmila Molkova** 19:54 Sounds good to me. Thank you.
**Keith Decker** 19:56 Okay.
**Aaron Abbott** 19:58 Okay. I mean… One… one thing to note with that is, you know, like, the… right now, they're all tested against the previous release, so if we release this GenAI Utils We should just, you know, make notes somewhere and update both of them so that they… Or all of them, so that they can be dependent on the right version before we do the release again. But yeah, it would be nice if there was a… I think we discussed, like, this issue.
Space it here.
This was the one.
About, like, the testing, and how they're not released together.
Yeah, it would be nice if we could just kind of release all the ones that depend on it in lockstep, but… Yeah, we can chat about it more later.
Alright, anything else there?
**Keith Decker** 20:49 No.
**Aaron Abbott** 20:53 Right?
Cool, Aaron, you're on?
**Erdenesaikhan Tserendavga** 20:57 Yes.
**Aaron Abbott** 20:59 Hi.
**Erdenesaikhan Tserendavga** 21:00 Hi, Ron. Yeah, I'm, working on the, UTs, for the, grading agent types and invoke agent types.
We have, ongoing issue the, Agent Unification Type, which is related to the server and client-side annotation, can be different dispensed.
This, current implementation following the, Align with the existing, It's about the conversions, which is, we have one, You know, agent type, and one create agent types.
Yeah, I have tested the, OpenAI instrumentation package, and which wraps the innovation Rob's, chat.
Thank you, Kevin.
**Aaron Abbott** 21:49 buildings?
Do you have, a link to the OpenAI kind of prototype where you integrate it? It would be helpful to, To see everything together.
**Erdenesaikhan Tserendavga** 21:59 I put it in the comment.
**Aaron Abbott** 22:02 Which is related to the, demo application clique.
This one?
**Erdenesaikhan Tserendavga** 22:07 No, it took.
Pulling up…
**Aaron Abbott** 22:11 I can go back to the main…
**Erdenesaikhan Tserendavga** 22:13 I think… put in the interpret. If you… if you see the, Agency Nucretion PR, I have,
**Aaron Abbott** 22:21 In the dock, yeah, yeah. This one?
**Erdenesaikhan Tserendavga** 22:25 Yes. If you go down, I have tested with the one I think… yeah, this one.
**Aaron Abbott** 22:35 Which, demo… which demo app is this?
**Erdenesaikhan Tserendavga** 22:37 It's, OpenAI, manual instrumentation, which near me the PRT, yeah.
**Aaron Abbott** 22:45 So did you integrate this into… like the… like, you're adding… adding new API here, and then you have to use it in… the OpenAI V2 instrumentation, I assume, right?
**Erdenesaikhan Tserendavga** 22:57 Yes, that's correct.
**Aaron Abbott** 22:59 Yeah, do you have, like, a draft PR for that one, also?
**Erdenesaikhan Tserendavga** 23:02 Yeah, I can agree with that PR and LinkedIn here.
**Aaron Abbott** 23:07 Okay.
Cool, so you're just kind of a call for reviews here?
**Erdenesaikhan Tserendavga** 23:15 Excuse me?
**Aaron Abbott** 23:17 Just looking for reviews here. Anything, anything else you wanted to talk about on these two?
**Erdenesaikhan Tserendavga** 23:22 No.
I don't have any, and if there is any, change in unwashed, I can make in there.
Agent integration type, as well.
In the future.
**Aaron Abbott** 23:35 Okay.
Awesome, thank you.
**Erdenesaikhan Tserendavga** 23:38 Thank you.
**Aaron Abbott** 23:41 Right, Surya, was this the one that we already mentioned?
**Surya Teja** 23:47 Yes, Aaron, that's the one that I mentioned.
**Aaron Abbott** 23:50 Okay, so we can… we can skip, right?
**Surya Teja** 23:52 Yeah, we can skip this, yeah.
**Aaron Abbott** 23:54 Okay, cool.
Oh yeah, Lucas, this one.
**Lukas** 23:59 Yeah, we don't need to talk about it too long, but… Yeah, it just… wanted to make sure this still got moving. Yeah, adding the new… Right, I'm trace ID Flay.
**Aaron Abbott** 24:17 Yeah, yeah.
So for, like, a little more context on why I kind of keep going back and forth on this, the, I brought… I brought it up internally, and people were like, you know.
not… People were a little concerned, like, they were like, yeah, I mean, I could see if this rolls out and this is broken, it would be… Kind of not great.
And I kind of agree, because, like, you know, people should be… the spec for W3C, I found it a little confusing, because it says people should ignore extra flags, but it also said that, any new flags that are added should cause, like, a version downgrade, but there was no, like, revved version in the W3C spec, and I linked Created this issue for that.
could probably, like, ping in some of the hotel groups to try to get feedback on this, but basically it says in, in the W3C spec that vendor will only parse trace flags supported by this version of the specification and ignore All other values, and like, if the version doesn't change, and we add more trace flags, I'm not sure.
How somebody would do such a thing, so… Yeah.
That was kind of my… But, sorry.
**Lukas** 25:37 Oh, I was just saying, yeah, that makes sense.
**Aaron Abbott** 25:42 So yeah, I mean, do we know if any other hotel Implementations have released this change yet?
**Lukas** 25:49 From the limited searching I've done, it seems not… So, yeah, we're likely the first.
I can, yeah, I can take another look, though.
Yes.
But it seems like, I think I was reading somewhere that In order for the W3C spec to move forward, there actually has to be implementations.
I believe 2 or something?
**Aaron Abbott** 26:20 Yeah.
**Liudmila Molkova** 26:22 prototypes.
With intent to merge, if… if… SPAC change comes through. Not, not… not… it doesn't have to be merged.
It would be great to bring on the call, if we are the first to do this change, and if there are questions.
People… other people would also have them.
**Aaron Abbott** 26:45 Yeah.
Yeah, you just mean the… not, like, W3C spec call, like the hotel one, right?
**Liudmila Molkova** 26:54 Oh yeah, of course, yeah.
**Aaron Abbott** 26:59 Cool. Yeah, we can do that.
And I think we could also merge this as, like, a separate subclass or something, that's something we chatted about, Lucas.
Any thoughts on that, or do you think we should just kind of wait until we have more clarity?
**Lukas** 27:16 We can probably just wait, but yeah, if we want, we can do that as well. I feel like… I feel like it's unlikely that people will… necessarily just want to opt into this. I'm not sure, though.
**Aaron Abbott** 27:30 Yeah.
Okay, so maybe let's bring it to the Tuesday call, the specsig, and Then go from there. Does that sound good?
**Lukas** 27:43 Yeah, the other options that we could, actually just update the ID generators to actually still return false for random, and then actually nothing would change.
And then when we're ready, we can flip it on to true.
**Aaron Abbott** 28:07 Yeah, I think the reason I kind of brought up subclass was, if you look at the W3C spec, there's also this section about downgrading the version.
And it kind of implies that, like.
You know, say they revved the… The version in the trace parent header.
It kind of implies that you would use an implementation for the version that you see in the header. So, like… if this becomes version 2, which supports this new trace flag, and you see version 1 on the wire, you would want to downgrade to the other implementation. And obviously, like, that's an implementation detail, but, like.
**Lukas** 28:43 Yeah, yeah, in that case, yeah, that definitely makes sense. So yeah, I can update the implementation depending on… I can take another look.
**Aaron Abbott** 28:53 Alright, Lucas, do you think you can make it to the Tuesday SIG, or…
**Lukas** 28:58 Yeah.
**Aaron Abbott** 28:59 Yeah.
**Lukas** 28:59 Yeah, just need the… the meeting link. You can just kind of… Okay.
**Aaron Abbott** 29:05 Okay.
And I'll paste these in.
I'll try to make it 2.
Well, that's unfortunate.
Okay, yeah, I guess I can ping you with the meeting details, but it should be on the hotel community site, or view of the hotel calendar.
**Lukas** 29:39 Got it, yeah. Thanks.
**Aaron Abbott** 29:41 Alright.
Well, thank you, Lucas. Thanks for your patience.
Alright, Ludmilla.
Completion hook, you're up.
**Liudmila Molkova** 29:52 Yeah, so I wanted to, get some eyes, but mostly I want to see if… This is the intended way we wanted completion hook to be used. So, what I do here is I… Allow instrumentations to pass completion hook to telemetry handler, and that telemetry handler will invoke it if configured.
And… Turns out that there is a bunch of changes in OpenAI. There's a major version bump. It's… it's fine.
But it… they created a new type for… it used to have not given, now they call it Amit, so it needs some minor cleanup to, support V2. I can, in theory, break this PR in two, but it's still relatively small. But mostly, I want to get your feedback on the completion hook. Is this how we want it to it to be… should it be called automatically by the UTIOs?
**Aaron Abbott** 31:00 Yeah, I mean, I think this… this makes sense to me.
It probably makes sense to also still expose it, kind of just, like, as a pure function, because, for example, we have the agent you know, we have… we were talking about putting the inference details on the agent… sorry, I shouldn't say inference details, but the prompt response input-output to the agent on the Invoke agent spend.
So if that one wants to do upload, we would have, you know, maybe separate different parameters, but, you know, still have a public API for it.
What do you think?
**Liudmila Molkova** 31:35 Right.
Yeah, having public API for it is totally fine. It's just easier to… not call it from every instrumentation that uses UTIOs. And there will be instrumentation who use UTIOs with Invoke Agent.
And they would also call… Hooked here?
The other… the other thought I had is, it's just instrumentation wouldn't even need to… have it an explicit parameter, or we wouldn't need to default. I'm currently defaulting to loading the hook here.
it could be the responsibility of the handler.
But I was… Yeah, I was thinking that… it's nice for instrumentations to explicitly obtain into this, maybe. I think Google does it slightly differently, right, because you use hook, but not the rest of the OTELs.
**Aaron Abbott** 32:50 Yeah, I see what you mean.
I mean, I could kind of go either way on it.
I guess, like, our auto instrumentation could make sure to always inject it for… instrumentations that support it. And that's actually kind of an interesting case, because like, if you look at the, the distro, OpenTelemetry Distro code, it basically, like, maps over instrumentations. It doesn't have a good way to tell If the instrumentation accepts, like, an extra parameter for completion hook or whatever, so… I guess those instrumentations could do the defaulting in their own setup code.
**Liudmila Molkova** 33:31 Right, and that's what I've done here. They default to the load completion hook.
**Aaron Abbott** 33:36 metic in OpenAI.
Yeah, let me look.
Yeah.
Yeah, it makes sense to me.
I think I can give it a review, and maybe I'll tag Dylan, too. I think he would have… A lot of context here.
**Liudmila Molkova** 33:56 Yeah, thank you.
**Aaron Abbott** 33:58 Thank you.
Cool.
Alright, this one, yeah.
Yeah, I think, Ricardo, you brought this one up on Slack. I thought maybe we should discuss it.
I don't know if Ricardo's around yet.
**lechen** 34:25 I think he was, yeah.
**Aaron Abbott** 34:27 Yeah, maybe he can't talk, maybe he's just listening.
Excuse me.
Yeah, I can… I can talk through this, It sounds like, basically, the user's concern is that The entire context object gets… enqueued.
So I think the issue is kind of phrased as, like, the log record stores the context, but… the issue, I think, is really kind of… Only in the batch… sorry, the… The batch log process… Sorry, batch log processor, batch log record processor.
Because that's the thing that's holding the memory around.
So, basically the concern is that when we stick it in the the queue.
all of the stuff in the context can't go… can't get… can't get garbage collected. Excuse me.
So, yeah, it seems like a valid issue to me.
Leighton, I see you left a… you left a comment last night.
**lechen** 35:28 Yeah, I originally thought this was, just an observation by the original Poster.
**Aaron Abbott** 35:35 Yeah, I don't think they even…
**lechen** 35:37 Confirmed whether or not this was the cause of the… Memory explosion.
I'm not saying that this is not a legitimate issue.
**Aaron Abbott** 35:47 Yeah. But I think…
**lechen** 35:48 This was just an observation by them.
I went ahead and asked for, like, if they had any, like, benchmarks or anything, because the original issue is that they had… They found that it was larger than the memory of the… You know, of other components, like the spend. But… As well, the other language implementations do this differently as well, so I don't mind even just making this change, just wanted to see what… like, even if we made this change and, like.
they had some memory problems. It's like, it doesn't solve the original issue, so…
**Aaron Abbott** 36:27 Yeah, that's true.
Yeah, I mean, I think their logic is sounding like, We could probably come up with a prototype that does.
Prevent garbage collection with the current thing that we have.
**lechen** 36:40 It'll be happy.
Yeah, it's most likely the contact.
**Aaron Abbott** 36:44 And that…
**lechen** 36:47 Also, so the original reason why we changed the API from just passing in span context, or at least the fields of span context, was just for passing baggage explicitly, right?
**Aaron Abbott** 37:00 I mean, I don't remember the… spec super well by heart, but I think… generally, like, the API should always… all the APIs, like, public methods should accept the context. Like, the full context, so that, processors or whatever can do stuff with it.
**lechen** 37:18 Yeah.
That's true, yeah.
**Aaron Abbott** 37:22 Yeah, I mean, I think the kind of classic thing that we… that we do is we do the suppressed instrumentation in the batch processor, like, around the, Around the call, so if somebody sets… For the synchronous one, if they set… You know, suppress context or whatever, and we'd throw it out.
**lechen** 37:41 Then…
**Aaron Abbott** 37:42 Yeah.
So yeah, I think, in terms of fixing this?
**lechen** 37:48 We're depicting this?
**Aaron Abbott** 37:52 Yeah, you could just go, probably, in here.
Really fast.
Yeah, we basically have to populate this thing with the log record, and we could… Make it a little bit… Yeah, this one has all the stuff on it, too. Okay, yeah, we'll have to think about this a little bit, but just wanted to share.
**lechen** 38:25 Yeah, makes sense.
**Aaron Abbott** 38:27 Bye.
Cool. The last one here is from me, also. I… Wanted to share this draft I did.
Of reducing the boiler… the boilerplate for the contribut instrumentations, like, most specifically the… the GenAI ones. It looks like Ricardo left… left a review.
So basically, the crux of it is, I think, the last couple of releases.
There was some boilerplate that we missed.
And when Ricardo did, like, the full contribib release, it tried to release some of these other ones.
And then also, just when people add new packages, it's been really difficult to review because there's a lot of small, little places you have to remember to add a line here, a line there.
So this… this PR basically moves some of that config into the PyProject… individual PyProject files for the instrumentation.
And the benefit there is, you know, like, if somebody just copy-pastes, it all goes in one place.
And, then we have, basically, templates for the… Releasing jobs, so… instead of having, like, the options hard-coded, which we had previously, we had to remember to update these workflows, it just generates them, so… Final result looks something like this.
So yeah.
**lechen** 39:54 Wonderful.
**Aaron Abbott** 39:54 Go ahead, Leighton, yeah, sorry.
**lechen** 39:58 Sorry, sorry about that. I wonder if we could get rid of that, support semantic convention and support metrics thing, finally, then, if we just embed it in the PHI project?
**Aaron Abbott** 40:09 Yeah, you mean for all the other packages, too?
**lechen** 40:12 Yeah.
**Aaron Abbott** 40:15 Yes, I think we could. I think we could do that in a separate PR, or in a… could split it up into multiple PRs. I think you're doing about this one.
**lechen** 40:23 Nope.
Thanks, thanks for doing this. The manual is very headache, so…
**Aaron Abbott** 40:29 Yeah, do you remember what the file is called that has the supports?
Just look.
**lechen** 40:35 Yeah, I'm gonna find it.
**Aaron Abbott** 40:36 Yeah.
**Riccardo Magliocchetti** 40:37 It's package BI.
**Aaron Abbott** 40:39 Yeah.
Oh, I'm not sharing the right tab, sorry.
So we could basically move these into the pipe project files, you know.
**lechen** 40:52 Nice.
**Aaron Abbott** 40:54 Okay. Yeah, so I can spend more time on this and try to get it… finalized, but I wanted to call out, like, the other possibility is to kind of… I mean, that's completely separate, but for the release workflows.
I wanted to bring up Release Please, I don't know if people have seen it before.
But it would kind of obviate the need for these individual workflow files, so… Basically, with Release Please, you have a config, And… A bot that runs periodically.
And the bot creates a release PR And it just keeps adding more commits to it.
I don't completely remember until you're ready to merge it. When you merge it, it invokes a release workflow. So instead of having, like, a drop-down on GitHub, which we have right now, it would just be… a PR that you merge.
So, that would… that would be something I'd be interested in, instead of… Going with these templated files.
But we can kind of do it iteratively, too.
**Liudmila Molkova** 42:00 The release pl… oh, sorry, go ahead.
**Riccardo Magliocchetti** 42:05 I was just going to add that… When I did the last release, the file I had to fix is hdist.ini.
That, you are not touching?
No, it's the one used… HDS.
We have an extraordial list.
**lechen** 42:31 Yeah.
**Riccardo Magliocchetti** 42:33 when we run htis.pi, I think it's inside scripts.
**Aaron Abbott** 42:42 Yeah, here, sorry, I can open it.
This one?
**Riccardo Magliocchetti** 42:50 Yeah, like, this one reads a configuration file.
**Aaron Abbott** 42:54 Hmm.
**Riccardo Magliocchetti** 42:55 And that configuration file was missing the exclusion of… a couple of GenAI packages.
**Aaron Abbott** 43:02 Yeah.
Yeah, I would love to get rid of that.
**lechen** 43:06 Cool.
This is the biggest culprit of… Instrumentation release mess-ups.
**Aaron Abbott** 43:14 Yeah, agreed.
Yeah, I think we could just… if you all like this PR, I could go a little more… I could take it the extra mile and get rid of the eachdist.inny, and just put everything in the PyProject files and read it out of there.
Is that kind of your concern, Ricardo? Would that… would that fix it?
**Riccardo Magliocchetti** 43:37 Yeah, yeah, sure. It's like… We're just going to, like, we have another… Another place where we duplicate the list of stuff to exclude, so… yeah.
**lechen** 43:51 Nice.
**Aaron Abbott** 44:06 Cool.
That makes sense. Oh, Clayton, you got a job. Udma, I think you were gonna say something maybe about release, please?
**Liudmila Molkova** 44:14 Yeah, I was just checking. It's the one that, has a convention on the PR, titles, right? The… And it relies on them to populate the changelog and everything, right?
**Aaron Abbott** 44:29 Yeah, you have to do the conventional commits.
That's the… URL. Oh, that's not the URL.
But yeah, you're right.
**Liudmila Molkova** 44:45 Yeah, it looks cool, I think JavaScript uses it.
**Aaron Abbott** 44:48 Yes, I think so. I think they've already used it. Like, obviously it's a Google project, so… I've seen it around, I haven't set it up myself before, but I was poking around at it.
This is… yeah, this is definitely the most invasive part. You basically have to follow this… I'm sure everybody's seen this around, but you write… Basically, like, a mini changelog in the commit message, and this is how it figures out how to do the version bump for each package.
Well, it sounds like nobody hates that, so… Okay, any other thoughts on release, please? Anybody have experience with it?
Right, that's all I had then.
Alright, it's the end of the agenda.
I'm going.
**Riccardo Magliocchetti** 46:26 Yup.
**Aaron Abbott** 46:30 See ya.
**Liudmila Molkova** 46:31 Thank you.
