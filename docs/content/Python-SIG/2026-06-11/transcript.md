SIG: Python SIG
Date: 2026-06-11
Duration: 66 minutes
============================================================

## Zoom Recording Transcript

Aaron Abbott 00:06:12 Hey everyone, how's it going?
Hector Hernandez 00:06:16 Hello.
Diego Hurtado Pimentel 00:06:17 Hey, Rudy.
Tammy Baylis 00:06:19 Hi, everyone.
Erdenesaikhan Tserendavga 00:06:23 Blown on.
Aaron Abbott 00:06:24 Abe.
We'll give it a few more minutes for people to join, maybe, and start around… Maybe in, like, 1 minute. I don't know if, any other maintainers are gonna show up today, but if not, I will… probably run the meeting. Oh, and feel… yeah, I think Timmy shared a link to the doc, feel free to add your… your names to the attendees and any topics you have.
Okay, cool.
So, we don't have any topics… oh, sorry, we have one topic, and we have the triage board. I think, Teme, I heard… I heard Joe on the call. Do you want to… on the triage?
Tammy Baylis 00:07:52 Yeah, I'll share my screen.
Hmm… Yeah, I think, Erin, you'll have to stop sharing first.
Thank you.
Cool. Project port 88, Python, let's go till 9-10.
Let's look at no status, ignoring chore and build PRs.
There's quite a few of them.
Okay, we have a unique one for add rolled dice reference application for FastAPI.
by Reggie D. Implements OTAL reference application specification.
But it's in the core repo for uninstrumented, instrumented versions of FastAPI, okay?
Oh, it uses the declarative config.
Cool.
Linked issue from Severin.
Yeah, I'm wondering, I think this… yeah, this is ready for review, for sure.
Or, actually, I'm wondering if we want this… Example… To be in the core repo, if we want it to be in the contrib repo instead.
So we go to… Registry, yay.
No, maybe not, maybe this is the right place.
Sweet look in here… Yeah, okay.
Main docs examples… Sorry.
Okay, I'm gonna mark this as ready to review, and I just had an idea… Are we considered… Putting it in toxic samples instead.
Okay… And the approvers on that list… cool.
Next one, feature, add Kafka Consumer Group Batter for Kafka Python.
In the Contra repo, we do have a leaked issue, thank you for that.
New feature… Yeah, this is ready for review.
Aaron Abbott 00:11:36 Yeah.
I wonder, I didn't look at the issue yet, but I wonder if there's a semantic convention for this one already, or if they're just kind of… YOLOing it.
Oh, there it is, awesome.
Tammy Baylis 00:11:50 Oh, all the homework, that's awesome.
Hmm… other one… Refactor for Prometheus.
Simplify Collector. I think DQ was optional.
Oh… Fixes… $2,500.
Oh, that's a slightly old one.
Hmm…
Aaron Abbott 00:12:30 kind of random, but I guess it's, worth a review.
Tammy Baylis 00:12:35 Yeah… Before and after… Okay.
One minute, let's do one more.
Oh, this… Documenting the… We just talked about SemComp often last week, but it's still gonna be, I guess, a little while.
Before we change the defaults and stuff, so I… I think doing a dock update will still be helpful.
Aaron Abbott 00:13:16 Yeah. One other thing is this, environment variable is also not specific to HTTP, so… I don't know if it's documented generally in the spec, but it's, like.
It has different values depending on, Different signals, so I…
Tammy Baylis 00:13:35 Right.
Mmm, should I…
Aaron Abbott 00:13:43 I think it's okay, it looks like they've… Just updated the specific instrumentations.
Tammy Baylis 00:13:49 Yeah.
Yeah. Sounds good to me.
Cool, Oh, stop sharing. Sorry, who's speaking?
Leighton Chen 00:14:03 Oh, sorry, yeah, I was wondering, like, did we want that, or just, like, update the instrumentation README to… Cover the generic use case.
I can, comment on the issue, the PR, too. No big deal.
Aaron Abbott 00:14:20 Yeah.
Tammy Baylis 00:14:20 Sorry, thanks, Leighton. You, you, started speaking and it was really quiet on my end, so I didn't hear you the first time.
Leighton Chen 00:14:27 No, no, no problem.
Tammy Baylis 00:14:32 Alright, back, back to you, Erin.
Aaron Abbott 00:14:36 Great. I think you can all… can you see the doc? Yeah.
Pin?
Cool. Log stabilization status, who… Does anybody want to speak to this one?
Hector Hernandez 00:14:48 Yeah, I added that one. Pretty much, we're still very interested in having, like, logs stable. This is one of the main blockers for, Azure Mona Exporter to be GA.
And I was going through the issues yesterday, and looks like at least 3 or 4? Looks like they're already addressed. Is this something that we can just continue to look at this project?
to understand what… where we can help, if there's any gaps, if there's any… because there's, like, issues, like, 3 years old. Yeah.
Aaron Abbott 00:15:25 No, thanks for bringing this one up.
I think… I'm trying to find which issue, I wish we had Ricardo around today, but… We did have, like, an issue where we… It's unfortunate it's split between issues and this kind of project board, but there was one where we documented, like, all the, you know, final breaking changes we wanted to make before Making, like, an RC.
And I don't know if this… maybe this project board has the, you know, the correct status, but… Yeah, I mean, I personally would love to see this move forward. I think this… this is way overdue, from our side.
Leighton Chen 00:16:04 Yeah, can you, was it maybe the first issue that's in to-do? Perhaps that's the tracking issue?
Aaron Abbott 00:16:12 This one's from Jeremy, I remember a different one, but…
Leighton Chen 00:16:15 Yeah, probably not.
Emídio 00:16:17 I have just shared the link, in the notes, Aaron.
Oh, good, yeah.
Leighton Chen 00:16:21 No, thanks.
Aaron Abbott 00:16:25 In the meeting notes? Oh, yeah.
Yes, this one.
I feel like we should… Just use the project board, or use, open… Anyway, I think, yeah, let me…
Leighton Chen 00:16:50 So you're saying we should use the project board instead of this tracking issue?
Aaron Abbott 00:16:55 I don't know, I think… I think Ricardo… I think it was a long time ago, obviously, it was, like, over a year ago, or almost a year ago, we were talking about this, so I… I'll defer to Ricardo, but… I assume this one's up to date. Looks like we did everything here. Merge, merge, merged.
Liudmila Molkova 00:17:14 There is a community issue you folks created a while ago to request GC review for logs.
And I've been your proud reviewer.
And there are a bunch of things linked to it, and there are a couple of minor things. Well, they look minor.
That are still open, but everything else looks merged.
And, we can plan another TC review, but it looks like we are on a great track.
Aaron Abbott 00:17:53 Cool. Yeah.
Leighton Chen 00:17:55 Oops, sorry, go ahead, Aaron.
Aaron Abbott 00:17:57 Go ahead, I'm trying to find the issue.
Liudmila Molkova 00:18:00 I pasted in the chat.
Aaron Abbott 00:18:02 Oh, perfect.
Okay.
So…
Leighton Chen 00:18:12 Nice.
Aaron Abbott 00:18:13 Yes.
Liudmila Molkova 00:18:18 So, I'll… Try my best to, do it within the next two weeks.
But yeah, it looks like we're a good truck.
Carlos Alberto Cortez 00:18:30 Sorry, Neil Mila, what did you say you were… you will be doing in the next two weeks?
Liudmila Molkova 00:18:35 Hey, hey, Carlos! This… this is the existing community issue for TC review for pipe and log stability. I've done it, I don't know, it seems a year ago, or more than a year ago, and it seems everything's been addressed, or pretty much everything. I… I can do the final round.
And then approve on this issue, close it, and then folks should be good to go, if they feel like it.
Carlos Alberto Cortez 00:19:01 Great, thank you.
Leighton Chen 00:19:03 Thanks, Lumila, for… Scan again.
I think a lot of the TC-identified issues have been merged. We did mark a lot of the outstanding PRs or issues in the… for the RSE project board, but there's also a lot of PRs and issues that were created That perhaps the maintainers didn't, like.
comb through to identify whether or not we wanted to include those as part of the RC.
Some of them are, like, actually new features that… maybe we don't want to include as part of the stable release, or it's not, sorry, it's not required as part of the stable release. So probably just another pass-through from the maintainers to To add that, or the object… update the project board as well.
Aaron Abbott 00:19:59 Yep.
I also wanted to raise this one, so… there's the Events API, which we prototyped, and now, obviously, that's not a thing anymore, we just have the Logs API.
Oh, Dylan left a comment 2 minutes ago, and Hector, you were commenting. So, I guess we need to make a decision on this one.
I… I don't know if it's, like… gonna be disruptive to people. I think we reached out to a couple downstream projects, maybe, like.
log fire or something about this one in the past, and I think we've… they've, like, removed their usage, but… I mean, I think ideally we would probably remove this before the RC.
What does everybody think?
Leighton Chen 00:20:45 Yeah, I'm okay with it.
I think we did our due diligence with the deprecation warning, so…
Dylan Russell 00:20:55 Yeah.
Aaron Abbott 00:20:59 Yes, and then… okay.
I guess the other thing is, when we… well, we don't have to talk about it now. I guess I want to give it back to Hector, like, Do you feel like you have a handle on how you can help?
Hector Hernandez 00:21:19 Yeah, yeah, I just was wondering where is the main place, but it looks like there's so many places. I can deeper to see what's… what's missing.
Leighton Chen 00:21:31 Yeah, well, the maintainers will try to help out, any new contributors that want to help with block stabilization, so I would refer to the project board as the source of truth, in my opinion, so…
Aaron Abbott 00:21:47 Okay, cool.
Hector Hernandez 00:21:48 Sounds good.
Aaron Abbott 00:21:49 And maybe… maybe offline, like, let's… Try to make the bookkeeping a little cleaner.
I think, just since Ricardo was involved, I'll probably… sync up with him. I think he's… he's just out on vacation or something like that, so… Yeah, we should make this more clear for everybody.
Okay, cool, anything else on this one?
Alright, cool. So I added this one.
kind of on behalf of, Lucas, I figured we should talk through it.
There's two PRs, and they're kind of independent, but I wanted to talk a little bit about the forking… stuff in Python, and… You know, get the lay of the land and decide if we need to have this complexity, but… Yeah, I approve this one. I think it's ready to merge. I left, like, one nit here.
Okay, immediate sounds good to you, too. I know there was, like, a question about doing it in a separate class versus leaving it in, the default hotel detector?
Emídio 00:23:04 Yeah, I left a comment about that, but, Lucas answered that, we can make it enabled by default, even by using another class, like.
Set of instantiation on the hotel detector.
Which sounds good to me.
Aaron Abbott 00:23:21 Bullet.
Emídio 00:23:22 Yep.
Lukas 00:23:24 also how JavaScript does it, which is also why I followed this book.
Aaron Abbott 00:23:32 Yep.
Very cool. And the thing I'm excited about is this will fix Metrics when people fork, hopefully, because the… well, I guess we have to wait for the second PR, but this was the thing I wanted to discuss, was it creates, like, a stable service instance ID, and it will detect if there was a fork and reset it.
So I think this one's kind of long overdue, and let me show you the other one.
Yeah, so this is the other one.
Yeah, I left this wall… wall of texts yesterday, Lucas, like, I think… Does… does anybody… have thoughts on, like, working in the Python ecosystem. This was the kind of other solution that was proposed, was, like.
Just document that we don't work with fork, and stop adding a bunch of hooks everywhere to try to make it work.
Leighton Chen 00:24:34 Could you… I haven't taken a look at the issue, could you summarize?
what the PR's trying to do, but… the alternative.
Aaron Abbott 00:24:43 Yeah, so a simple example is, like, the PID.
I think it's process.pid resource attribute. When we set it in the resource, it's all good, but when somebody calls OS.Fork, or if it happens in, like, Gunicorn or something like that, the PID is just copied from the parent process into the new child, and it becomes out of date.
Leighton Chen 00:25:09 Right, so is that… is the PR trying to solve that, or, like…
Aaron Abbott 00:25:15 Yep.
So the… the PR has, like, a kind of general mechanism for detectors to…
Leighton Chen 00:25:22 I see, okay.
Aaron Abbott 00:25:23 Do you want to say something?
Yeah, maybe it was echo. Yeah, the… basically there's, Feel free to interrupt me, Lucas, if you want to speak to this, but there's… See if I can find it quickly.
Yeah, so there's this new function, isProcessSensitive on the resource detector, and If it's true, the resource detector gets rerun in a post for cooked. I got that right.
Lukas 00:26:00 Yep.
Leighton Chen 00:26:03 And, what was the issue that you identified, Eric?
Aaron Abbott 00:26:11 Can I say that one more time?
Leighton Chen 00:26:13 Oh, what was the issue that you identified, like, that you had a problem with?
Aaron Abbott 00:26:17 Oh, I mean, so, like, among other things, the PID… It's just a basic example, so I think we updated it here. Probably find it.
Lukas 00:26:31 I think it's been the same file.
Aaron Abbott 00:26:33 Oh.
Yes, yes. So, like, the process resource detector returns true for this, and, this is the function… that returns… Can hide that for now.
Basically reruns that… the resource detectors that are process sensitive and merges them.
Lukas 00:26:59 And I think… Your concern here, Aaron, is just the operational complexity?
Aaron Abbott 00:27:06 Yeah, I mean, I think if it's all private, I'm totally okay to go ahead with this. I feel like I was just a little surprised by your comment here, Lucas, like, Most, what'd you say?
you know, most Python processes won't work. I feel like It's probably true, but, like, the important edge cases Most, like, web servers still do this, as far as I know.
Lukas 00:27:30 I think… well, I mean, like, UVCorn is, uses Spawn, and I know we have docs on GUV corn on… Setting the instrumentation… Doing auto instrumentation.
post-fork, but I do… I do still agree, like, we should support it, but I was… my second… my last comment was just, like.
I mean, Python even documents this, like, forking can, like, in many, many cases, lead to deadlocks with locks and stuff, so… and I'm not even sure if, like… yeah, so… But… I think… I mean, this seems like a reasonable solution to me, I didn't have time to respond to your last comment, but I feel like even if we did special, like, just do a special case for it, we'd still have to register a post-fork hook, right? Unless we…
Aaron Abbott 00:28:26 Yeah.
Lukas 00:28:27 Unless we, went with the, like, lazy string approach that you mentioned.
Aaron Abbott 00:28:33 Right, right, right. I guess the concern was more, like, the number of hooks we have. I think we have, like.
hopefully most… like, some of them are at the instance level, so, like, this one is a hook on the… on each tracer provider or whatever, so… like, there's also this proposal in OTEL about, what's it called? I think it's called, like, multi… multi-otel, where you can have basically better multi-tenancy support by having SDKs be, like.
Easier to instantiate, like, every time you add a hook.
as far as I know, it just becomes a memory leak in the Python runtime.
So, I think there's things we could do to fix that, like, we could… we could have a single hook and then add stuff to our own weak map or something like that, but, It is a bit whack-a-mole, like you said, like… I think we don't update the gRPC connections, for example. There's a separate issue for that one. There's a bunch of things we don't do at Fork, and it's still not super safe, but as far as I understand, it's still really prevalent in Python.
Okay, so… if nobody has an opinion, like, I think I'm okay to move ahead with this one. We're keeping everything private, so we could always, Go back and change it, but… Yeah.
Leighton Chen 00:30:01 I'll take a look at it today.
Dylan Russell 00:30:04 Yeah, I'll take a look, too.
One question about the naming is, like.
Is process sensitive? Should we say, like, is… Process, like, will process be forked or something?
Lukas 00:30:24 Yeah, I wasn't… Yeah, I'm open to alternative names.
I think, yeah, the… Probably the biggest one is just documenting it in the doc string, like, what this, does…
Dylan Russell 00:30:45 Sounds good.
Aaron Abbott 00:30:51 Cool.
So, I don't want to labor this point too much, but there's, like, at least a handful of PRs and a handful of issues that are, Also concerned about fork safety, so… it would… it would be nice to have, like, party lines here, or have, like, a… better support for this, I don't know.
So…
Lukas 00:31:17 Fantastic.
Aaron Abbott 00:31:19 Yep.
Lukas 00:31:19 Last thing I want to add, to your concern with, like, registering a bunch of post-work hooks, we could try to, like, consolidate internally and have our own internal post fork hook, and then just only call os.post forkhook once.
Aaron Abbott 00:31:36 Yep.
Yeah, that's what I was thinking, and if I remember right, somewhere in CPython, I saw some code that did Like, in one of the standard libraries, it does exactly this, and they had an issue with memory leaks, so… Yeah, there's lots of stuff we could do, for sure.
Okay, cool. I don't… I don't think you need to do that for this PR, by the way, Lucas. We could… we could do that as a follow-up, but yeah, if nobody else has thoughts, let's keep going.
Leighton?
You wanna talk about this one?
Leighton Chen 00:32:18 Yeah, sure. Would you be able to… Yeah, thanks. So… Just a follow-up from last week's conversation, this kind of came up due to some issues asking about, like, erroneous behavior in old semantic inventions, or erroneous behavior for some semantic inventions, and it turns out it was only in the old implementations, so it kind of kicked off the discussion about Reintroducing, the work for stabilizing, the already Kind of… instrumentations that are on the stability path, so I left… Sorry, my to-dos were to find out which components we kind of needed to… kind of tackle first before doing that effort. I think, just going through the… my comment a little bit, So, semantic conventions, and the instrumentation base package would probably need to be stabilized first, before Tackling individual instrumentations, or all the instrumentation at once.
If you take a look at the bottom section for number one, the considerations, you can read there, we have to… we want to decide What's due for… The coupling with OpenTelemetry API.
So, right now, when we release, Like, we have… semantic conventions.
released with the API, so I think we either… Move and add a… Add the semantic convention package to the stable section, or we need to create, like, a separate, like.
stable, but not the API versioning scheme for releasing. It's not really a… This is more of, like, a… just a… Like, an overhead for maintainers, so it's more like a… Operational.
Oh, Aaron, I did see you leave a comment. Sorry, I didn't, I didn't, get a chance to see it, so…
Aaron Abbott 00:34:42 No worries. Yeah, this… this was, like, related to the, First topic that you had about incubating.
I think… and somebody keep me honest, but I think the idea was just to indicate that the like, attributes are incubating, but the Weaver-generated code, in theory, shouldn't have any breaking changes, like… Fields would get deprecated, but they should.
remain API compatible, is my understanding.
Leighton Chen 00:35:12 Yeah, that was what my understanding was, too.
Aaron Abbott 00:35:18 Right, in which case, I guess… hopefully this is not a concern, right? Like.
Leighton Chen 00:35:27 Yeah.
Aaron Abbott 00:35:33 I know we had a couple accidental close calls with changes in Weaver, or changes in the semantic conventions repo in the past, but… it could happen anywhere, right? Like, it's just the intention… we have some checks for it. We have, like, the grift check, Right.
Leighton Chen 00:35:53 Right.
Aaron Abbott 00:35:54 Yeah, I think I'm pretty comfortable with that.
Leighton Chen 00:35:56 Yeah, so barring any, like, like, mistakes in upstream or something like that, I think the purpose is to have incubating be backwards compatible.
So as long as we're, like, true to that, I think this is fine.
So I can state that, like, okay, we're not deciding to split the incubating into different packages, we'll just release this as part of the semantic dimension.
That's the… Result from this?
Aaron Abbott 00:36:29 Yeah, I mean, I think so, but we should get… Get, you know, more thoughts from other people.
Leighton Chen 00:36:35 Yeah.
Did you mention also removing the private… er, sorry, the underscore, Bing.
Neither.
Aaron Abbott 00:36:46 Maybe I did, I don't know. Oh, yeah, yeah.
Leighton Chen 00:36:49 Nice, nice.
Yeah, I'm good for… yeah.
Aaron Abbott 00:36:54 I don't know how much value it adds, it is kind of… like, I think the original expectation was that, it was to tell people that, hey, this thing is gonna have breaking changes, but they're not, like, API breaking changes, so…
Leighton Chen 00:37:07 predicating. Yeah.
I guess it is kind of weird to have a…
Liudmila Molkova 00:37:12 Hard.
Aaron Abbott 00:37:17 Say more, say more.
Liudmila Molkova 00:37:20 So… The semantic conventions are experimental.
We don't remove anything from semantic conventions now, so… But you can still expect… Breaking changes, because what it generates is… Not stable.
It's like it's best effort.
Essentially.
Leighton Chen 00:37:52 Like, for example, if you, If you change… if you don't remove an attribute, but you change what it represents, maybe?
Liudmila Molkova 00:38:01 Yeah, but… it's essentially the best effort that we don't remove attributes, because we don't want to break everyone. But let's say, I don't know, 10 years from now.
We want to remove some attribute and introduce the semantic conventions.
10 years ago.
Should we be able to do this? Probably, yes.
If they were experimental, and never… and deprecated for 10 years.
So, one day this change might happen, where there could be behavior changes that, I don't know, the metric unit changes from bytes to kilobytes. It won't, but it could.
Leighton Chen 00:38:47 Yeah, that makes sense. I think… I think if the change is, like, 10 years from now, like, We could use.
Liudmila Molkova 00:38:54 I don't know one.
Leighton Chen 00:38:56 Like, we should be able to, you know, utilize just a major version of semantic conventions, but, like, to your point, like, let's say we wanted to make a change, like, 3 months from now, or 6 months from now, like, that… what you're saying still holds true, right? Like, there could be behavioral changes, even though it's best effort, it's not a removal of a… field, but it's still changing what the field means, so that's inherently, I guess, breaking.
Liudmila Molkova 00:39:27 Yeah, I guess the discussion is whether to keep underscore or not, and whether incubating on its own means some level of instability.
Like, conceptually, this is not a stable thing.
Regardless, underscore or not.
Leighton Chen 00:39:48 Yeah, this is more of, like, a convention rather than an actual enforcement, and I think… at least from what I've seen internally in Microsoft, like.
If a package is marked stable, users expect all… all symbols in that package to be stable, really. Like… They don't like seeing, like, oh, like.
I want to have a sure thing that my thing will never break.
But that's just… That's just my opinion.
Liudmila Molkova 00:40:22 Yeah, we actually don't want anybody to be using this except this repo.
Right? Because if it's an external instrumentation.
We don't want them to depend on this.
Unstable part of the artifact, even if it's marked as stable.
They would be better copying the constants over.
in my mind, this is the… in Java has it codified, they're saying if your third-party library don't depend on the unstable artifact, don't depend on incubating conventions.
they ship to different artifacts, but I don't think it's the right choice for Python. But anyway, so I think nobody except us in the Contribu, maybe another Python Gen AI, would be using those.
And to a large extent, they're internal.
And it shouldn't be a blocker to stabilize, regardless, but putting them in the… Non-underscore.
Would… would send a signal that somebody else on the outside should use them.
could use them.
Leighton Chen 00:41:43 Yeah, so, I'm all for not having to maintain multiple artifacts.
But I think, I think some… some… I don't know if Hector's still here.
So I guess it does come down to, like, a… a messaging. Like, we want to prime users to not use this. I guess we can rely on that, because we do… kind of do that for other aspects in Python, too.
Liudmila Molkova 00:42:18 Yeah, so if I understand what you're saying, let's just keep underscore, it's internal. Don't use it.
Leighton Chen 00:42:24 Yeah, right, like, if Java is similar to Java, like, if they are just stating and trying to notify people not to depend on this.
Like, that could be a way, that we want to follow as well.
Aaron Abbott 00:42:44 I think… I think that's fine, we don't need to, like… solve everything right now. I just… I feel like the actual issue we're trying to solve is dependency conflicts, right? And… Even if we have, like, a separate artifact or whatever, if people are using instrumentations, because the intention is to contribute, but would still use the incubating attributes, right?
And somebody keep me honest.
Liudmila Molkova 00:43:10 Yeah, and we do the best effort not to break, and stable instrumentation should never depend on the incubating part of it.
Aaron Abbott 00:43:17 Right, but then that means that the experimental ones need to not pin the incubating version, and just accept that it may break, because we… the whole point is to, like, remove the dependency conflict issues that are… that everybody's facing, right?
Liudmila Molkova 00:43:32 They're… I think we… I'm not proposing separate artifact for Python, it's just, like, I'm sharing this because Java just tells not to use the unstable part of it, regardless.
And we can do the same with underscore incubating.
And we do absolutely best effort to have no word dependency conflicts. Did we have any dependency version conflicts with… some comfort effect. We don't need to… Pain, actually.
We can have bigger… Oracle, all the time.
Aaron Abbott 00:44:10 Yeah, I think that's the important part, so, like, the… the dependencies in, say, like, an unstable instrumentation for the semconv artifact are just gonna be… a little bit floating, and it's gonna be a little up in the air. People just need to… Test it, and things might break, but there's not really anything we can do about it.
Liudmila Molkova 00:44:30 We're doing a lot, right? We are not removing things.
And we are pretty much… We have very, very high backward compatibility rate, but not… it's not guaranteed to be 100%.
Aaron Abbott 00:44:50 Yep.
Sounds good to me. Leighton, do you feel… Are you… is somebody writing this down? Do we feel good about this?
Leighton Chen 00:45:07 Yeah, I think… I think… I can… I can summarize in the… And the issue, what we discussed about this.
Liudmila Molkova 00:45:16 My understanding is just nothing changes, this artifact can go stable.
And incubating… underscore incubating is for us to use in the country.
Leighton Chen 00:45:29 Yep. And we should, let a lot of users know this.
So, from what I've seen…
Lukas 00:45:43 Oops, sorry.
Leighton Chen 00:45:43 No, sir.
Aaron Abbott 00:45:44 I was just gonna ask anything else on this topic. I think, Lucas, did you have something?
Lukas 00:45:48 Yeah, I was just gonna say, for the st… so for the new stable packages, are we gonna… not… Pin semantic conventions, then?
Because it looks like currently we pin, in all the contrib packages.
Aaron Abbott 00:46:04 Yeah, I think that was the decision.
For the recommendation.
Liudmila Molkova 00:46:10 Can't pit.
Lukas 00:46:11 Honestly, but we can still pin. Is that what we want, or…
Leighton Chen 00:46:23 I think… Because we're leaving incubating in the… semantic conventions as one package, and then once we go 1.0 for semantic conventions, even experimental instrumentations can Rely on it, but not have to pin, right?
Liudmila Molkova 00:46:48 In the lowest version.
Yes. Allow everything higher than certain.
Leighton Chen 00:46:54 Correct, yeah.
So this should alleviate a lot of, like, the dependency issues that users are having.
Thanks, thanks for taking notes, Aaron.
Aaron Abbott 00:47:14 Yep, somebody let me know if I'm writing something wrong.
Leighton Chen 00:47:36 I think for unstable instrumentations, they technically could still break because, we're not restricting them from not using incubating, right?
Aaron Abbott 00:47:49 Yeah, that's right, that's right, it's just kind of best effort or.
Leighton Chen 00:47:53 Yeah, yeah.
Aaron Abbott 00:47:54 Okay.
Liudmila Molkova 00:47:55 If I'm using the attributes from version 1 to 3, I should express that… I expect at least 1 to survey, right?
even for unstable. It's not like… Just not peeing at all.
Aaron Abbott 00:48:18 I mean, that… that's true.
So, like, I guess I don't understand what that gets us, because if somebody's using an old… especially if the instrumentation is unstable, people might not want to take upgrades on the unstable instrumentation. And if it's pinning, even if it's, like, a version range, say it's, like, one year's worth of version ranges, like, people are still going to get conflicts, right?
Liudmila Molkova 00:48:46 If they want to run a very new instrumentation, and a very old instrumentation in the same application, I… They cannot do this freight.
They cannot do this today, and they should not.
We should not… Make it easier for them, or make it possible.
Yeah.
Lukas 00:49:09 I think I agree here.
Like, if… if a new… Unstable attribute is added, and we want to add it to an unstable library. The only way to do that is to bump the minimum version, right?
Aaron Abbott 00:49:25 Right, but, like, there's… there's also… it's pretty common in the Python ecosystem to do… like, very, very relaxed pinning, and I don't think that's… excuse me, always good, but, like, for example, what happened with Flask and, Roksoig or whatever, last year, like.
they wrote a whole article about how you shouldn't pin your dependencies and all that. I don't know if this is, like, a… good time for the topic. We have a couple more… Agenda items, but… Is everybody… I'll post this on the issue, and then can we take the discussion in here? Is that alright?
Liudmila Molkova 00:49:59 Okay.
Leighton Chen 00:50:01 Yeah, sounds good.
Aaron Abbott 00:50:02 Okay, cool.
Moon, I think you're up next.
Liudmila Molkova 00:50:07 Yeah, this is, an ad. So we are trained to stabilize everything around logs in our town, and the piece that's not stable yet is Wow.
semantic conventions around them. So one of the things that's happening, we are deprecating span events.
And Python uses span events, I think, even in the… Core repo, not in just instrumentations, for any exceptions that happen during a span.
The plan is… That, for well-known instrumentations, we now recommend emitting exceptions or logs.
for HTTP and DB ones. And they should replace… Span events, eventually.
This is a long road in the spec and in semantic conventions to stabilize every piece of it.
I'm looking… I'm asking here if there are any people interested in helping prototype this in Python and see how it can eventually land.
If you're interested, please comment on the issue. If you want any additional context, ping me.
Yeah, it's Annet. Thank you.
Carlos Alberto Cortez 00:51:39 Sorry, I have a question. What's the timeline that you have in mind for this?
Like, how urgent, like, can it… do you expect this to happen, hopefully, in the next, let's say, a month?
Or is… Like, even more urgent.
Liudmila Molkova 00:51:55 And it's… it's not urgent, but… This whole effort of… figuring out span events versus logs and stabilizing all aspects of it. It's already a multi-year effort, so I don't… We don't want it to take many more years, right? So if… if somebody is, has capacity and interested in the topic, I would love for it to happen sometime soon.
Carlos Alberto Cortez 00:52:25 Okay, yeah, thank you. Understood.
Liudmila Molkova 00:52:28 Yeah, thanks.
Aaron Abbott 00:52:38 Alright, marcelo?
Marcelo Trylesinski 00:52:42 Yeah, yeah, I guess you folks talked about HPX2 last week?
About native instrumentation, or if it should be on the Super Monorepo stuff?
Aaron Abbott 00:52:57 Yep.
Marcelo Trylesinski 00:52:59 So, I checked a bit. What I'm… I'm open to have it on HPX2, like, native, but I don't think there is a nice way to do, like, you know the HPX Instrumenter class?
There is no nice way for me to offer that in the package.
But anyway, my question is, last week I saw the comments about being able to instrument HPX2 with the HPX normal instrumentation stuff.
Is that what's gonna happen, or… The idea of having… the OpenTelemetry Instrumentation HPX2 package.
Lukas 00:53:49 I think I have… or… I think I have a little context here. I think my original, or one of the suggestions that… I mentioned was that, like, we can just… adapt the HTTPX library to add HTTPX2 support, just as, like, an interim solution, until, like.
You guys decide, like, what approach you're gonna take for native instrumentation?
And it should be doable in a pretty minimal amount of work, because the APIs are the same, right?
At least, currently.
Marcelo Trylesinski 00:54:25 What on?
Yep.
I don't intend to change any API anyway, but yes.
Lukas 00:54:30 Okay, yeah. So… Yeah, if someone wants… I think, Aaron, I think you also commented in Slack that You were okay with…
Aaron Abbott 00:54:41 Sorry.
Lukas 00:54:42 So, if someone wants to open a PR, they're welcome to, otherwise… I might have some extra capacity to do it if, if we want, then…
Aaron Abbott 00:54:58 Yeah.
I mean, I'm open for it, I don't… like, please, by all means, I think we have this issue. I think, maybe, Lucas, if you could drop a comment on here, or we could use this as the issue with the work and just capture the decision there, that'd be good.
Lukas 00:55:21 Does that answer the original question?
Marcelo Trylesinski 00:55:26 So, the plan is to actually do it in this repo, and then on HPX, you actually are instrumenting also HPX2, right?
Lukas 00:55:38 Right, I mean, that was… I guess, like… I mean, ideally, like, you guys could add it natively, but, like, we understand that that might take a little time, so… the int… I guess… if HTTPX2 does actually add the instrumentation natively, then we could deprecate the usage of this old package, right?
Marcelo Trylesinski 00:56:05 When you mean old package, you mean the normal OpenTelemetry instrumentation HPX1?
Lukas 00:56:12 Yeah, yeah, yeah.
Marcelo Trylesinski 00:56:13 Okay, yeah.
Lukas 00:56:15 Yeah, I mean, there's, like, a bunch of… like, ideally, you should only have to depend on OpenTelemary API.
If you were to add the.
Marcelo Trylesinski 00:56:23 Ideally, yeah.
Lukas 00:56:24 Yeah, but, like, I mean, actually, you could even get away with having no dependencies at all if you were to add some sort of, like, a hook system or something.
And yeah, I guess, yeah, if you're having, like.
issues, you can just, like, post in the Slack, because I think, like, I mean, you should be able to define your own, like, entry points and stuff so that the auto-instrumentation is able to pick it up.
Marcelo Trylesinski 00:56:52 Yeah, my problem is not on how to do it, it's more… I mean, I did it on the MCP one, and the way to… I mean, I… It's just adding the plumbing in the… in the reports of the publisher.
Lukas 00:57:07 Okay, got it.
Marcelo Trylesinski 00:57:09 But anyway, if it's first year, and then I have time to check how to be in HPG X2, then all good.
Aaron Abbott 00:57:20 Cool. Marcel, I think… You know, tell me if you don't want… we don't need to discuss this anymore, but you mentioned it's hard to use the instrumenter in HTTPX, too.
Marcelo Trylesinski 00:57:31 No, it's just that I don't like the API. I don't know how to put it in a cute way.
Aaron Abbott 00:57:37 Okay. Do you want to talk about it, or no?
Marcelo Trylesinski 00:57:40 No, but we can discuss offline, but no, no.
The other thing is about the MCP thing. So, I've added instrumentation natively to the MCP Python SDK.
Aaron Abbott 00:57:53 Yes.
Marcelo Trylesinski 00:57:54 But I think I just started one or two spans.
For now, I'm not that motivated to add more, like, or metrics, or whatever. If someone here wants to have that, I encourage you to do it. I'm happy to review stuff.
yeah. We're gonna release the version 2 of the MCP SDK end of, July.
But the sooner… Someone helps, the sooner, we can release the beta releases and all that stuff.
Because this will probably annoy… well, not annoy, but it will conflict a bit with the… well, you'll have more events since you are using FastMCP, then I would like to be able to solve with them to remove some of their side, to have only on our side, because they depend on us.
Aaron Abbott 00:58:54 Yeah, I filed an issue for them, actually. They seemed open to it. I don't know if you have a good relationship with them.
Marcelo Trylesinski 00:59:00 Yeah, we have a good relationship.
Aaron Abbott 00:59:03 Okay, let me just drop it here for context, Yeah, I mean, I'll take a look at the, instrumentation. I'm glad it got in. I know I kind of… it was a little back and forth during, like, holidays or whatever, but, I think this… this bands… we're covering most of the semantic convention, and I don't know, Lyudmila, do you want to… like, we were discussing stabilizing some of the semantic conventions, but then I also know that MCP just released, like, their new transport in the spec, the stateless transport, or they're about to release it.
Any thoughts on, like, just since we're talking about the semantic conventions package and stabilizing it, I think we copied the constants into the MCPSDK, but… Any thoughts?
Liudmila Molkova 00:59:58 I mean… For this one, I think we should, authorize it, I can't… we can bring it up. I can bring it up in the GenAI SIG in case people are interested. There are people interested in contributing to MCP, instrumentation.
the… stabilizing some con for MCP, Yeah, like… Let's do it! Let's do it tomorrow, can we?
Aaron Abbott 01:00:29 Yeah, the only thing was, I think the context situation might be a little simpler. I think the new stateless protocol is designed to work just like REST, so just propagating in headers would probably be fine. But we can… we could do that as, like, an addition. I don't think that's… Something we need to, like, change or remove from the spec.
Liudmila Molkova 01:00:49 Yeah.
Okay, I didn't read about the new protocol. That's cool that they have it, like Rust. It still might be… I'll iterate, but I can easily imagine that the transport protocol and the actual flow protocol are… different contexts.
Aaron Abbott 01:01:16 Okay.
Marcelo Trylesinski 01:01:17 Yep.
But we also don't have the new transport implemented yet.
Aaron Abbott 01:01:22 Okay.
Yeah, I think it's fine. We'll just, like… especially if there's a new transport, what we have right now could be for the current transport, and then if there's any changes, we could just add it to the spec, I think. I love the idea of stabilizing it right now.
Marcelo Trylesinski 01:01:39 Anyway, happy to review everything there.
Liudmila Molkova 01:01:43 there was a little bit of sarcasm in Let's Do It, just because it needs effort, and I… I don't feel like if we had the energy we would spend it specifically on MCP, we'd probably start with inference and agents, and MCP would come naturally as a part of it.
Aaron Abbott 01:02:02 Okay, so it's a… it's like a time issue, not a.
Liudmila Molkova 01:02:06 It's a wishful thinking, right?
Aaron Abbott 01:02:08 Sure.
Okay.
Cool. Well, thanks for dropping by, Marcella. I'm excited to see native instrumentation, so… Yeah.
Marcelo Trylesinski 01:02:21 Notice.
Aaron Abbott 01:02:24 Alright, I think that's the end of the agenda, too, and we're just about time, so thanks, everyone. Really appreciate it.
Marcelo Trylesinski 01:02:31 to.
Liudmila Molkova 01:02:32 Thank you.
Marcelo Trylesinski 01:02:32 week, folks.
Diego Hurtado Pimentel 01:02:34 Agoo.
