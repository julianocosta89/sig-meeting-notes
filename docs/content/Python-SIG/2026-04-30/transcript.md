SIG: Python SIG
Date: 2026-04-30
Duration: 57 minutes
Zoom Recording URL: https://zoom.us/rec/share/KaxsUqRSsSDh7Y7wZ9kIodvlbLkvq2-bKhf8XtkJWWYFtVKMHNf51HwPqqFYCbpm.XZ8dBdB2B-xI3XcE
============================================================

## Zoom Recording Transcript

**Riccardo Magliocchetti** 01:03 Hello.
**shuwpan** 01:08 Hello!
**Hector Hernandez** 01:10 Hi.
**Tammy Baylis** 01:11 Hi, everyone.
**Liudmila Molkova** 01:31 Hello, hi everyone.
**Tammy Baylis** 01:37 Hi, Ludmilla!
**Mike Goldsmith** 01:41 Hey, good morning. Good afternoon, everyone.
**Tammy Baylis** 01:45 Hey, Mike.
**Erdenesaikhan Tserendavga** 01:49 Blow it on.
**Mike Goldsmith** 01:51 Hey, good morning, afternoon, wherever you are.
**Tammy Baylis** 01:55 Hey, Aiden.
**Riccardo Magliocchetti** 02:08 Oh, Welcome, everyone, to this week's Python SQL.
Please add yourself as an attendee to the notes, and also, if you have any topic, feel free to add them, because we… We don't have any at the moment.
And we're starting a… A couple more minutes.
We're waiting more people to join.
Yep.
Okay, we have some topics, so welcome again.
And I think we can start with the triage.
Tommy, do you want to let something?
**Tammy Baylis** 04:34 Yeah, I think we're still having… the approvers and maintainers are having some chit-chat still about the columns on this board, but we can continue that offline.
Yeah, maybe, Ricardo, if you don't mind, you could just do 5 minutes of… Checking new issues, is that okay?
**Riccardo Magliocchetti** 04:53 Nope.
**Tammy Baylis** 04:55 Thank you.
**Riccardo Magliocchetti** 05:00 Yep, ton of new issues here.
Okay, this is interesting.
They added some automation, For keeping them… Maintenance and approver list up to date.
And so we got this… Automated PRs.
Okay, I'm just waiting, just for the changelog. And… I don't remember, where's the… yeah, yeah, Mike was also wrong for Contrib.
And I think it's 6 months of inactivity.
To be removed from the list of approvers and volunteers, or… Something like that.
I think the script is the community repo, if I remember correctly.
Correctly, but…
**Mike Goldsmith** 06:01 Yeah, it is. The, TC and GC have been working on trying to make sure that the roles in each SIG is representative of who is present and contributing.
**Riccardo Magliocchetti** 06:20 And then… Punching AI… Bios… Okay, opening agents, MCPS response… Okay?
Okay, this is… I don't think this is… okay.
This is, an old PR that was closed, I think, and has been… Reopened as a new one.
Yeah, I think I already took a look at this some months ago.
But I don't remember.
what were the issues still open? This is, like, for adding, The WSX3, remote sampler.
And it's kind of… complicated sample.
like, more complicated than the rule-based one we have in experimental samples, so if any one of you are interested in samples or samples.
On the AWS.
Feel free to take a look.
And Ben, we have this one, from Leighton.
That is doing some… I think proper checking for the size of the baggage we inject.
Like, we have proper checks when we, I don't know how it's called the verb, what? Inbound, but for the outbound side.
Sorry, varies luck.
Oh.
some paganas.
And… And… and yeah, so we have just, like… Quite a bit of comments already, so… we'll find… Some drafts one about salary, okay. This one also is interesting, from Islam.
I think this also was already… Closed by the… Like, I remember seeing this already.
And this is adding an instrumentation in Contrib for, catching the… Like, uncatch the exceptions?
And the thing had to be reported as logs.
I guess… Yeah, don't remember the code.
But yeah, like, there is an, I think a Python book, okay? Quite a bunch of books.
Someone was talking, sorry.
**lechen** 09:13 Oh, sorry, I just…
**Riccardo Magliocchetti** 09:22 Yep.
One more greenhouse, let's see what else do we have.
Okay, somewhere fucked up… Right.
Yeah, please, when you… especially in contrib, please add a prefix of the instrumentation you're touching.
Otherwise, it's pretty hard to understand what this is about.
So this is OpenAI V2.
**Liudmila Molkova** 10:01 I think this is the, Which deals more than Company A.
**Riccardo Magliocchetti** 10:06 Sorry. Yeah, now, because I see it in the checklist.
It is a utility or okay.
**Liudmila Molkova** 10:18 I can never remember, Lord.
**Riccardo Magliocchetti** 10:23 Okay.
**lechen** 10:24 The tag, as well.
on the pier.
**Riccardo Magliocchetti** 10:31 You have a very low volume, Lato?
**lechen** 10:34 Oh, sorry, I'm a little bit far away.
**Riccardo Magliocchetti** 10:40 Okay, under the label.
This one… Okay… Just some logs.
Changes?
Yeah, as well.
Understood.
**Lukas** 11:07 Dylan also has an open PR that might make this irrelevant.
But, yeah.
**Riccardo Magliocchetti** 11:20 Some dependable tap-amps.
Yeah, we're past 5 minutes.
So we can go on with the topics, unless anyone want to highlight some… PRs or issues…
**Ridhima Satam** 11:45 There is a PR I want, reviews on. Should I talk about it here, or later? I just want… it's a new PR, and just want people to look at it. It's there in the middle.
**Riccardo Magliocchetti** 11:59 Okay, I see. Well, if you already added it in the topics, we… We'll go forward later. Thanks.
Okay, so, first topic for today is from Lucas.
**Lukas** 12:16 Yeah, so, yeah, if you click on these two issues, and I think I've brought up similar discussions here, but, there's, I guess, some… Desirability of, like, allowing… different HTTP client libraries for, like, the, OpenTelemetry HTTP exporter.
So yeah, there's this one for HTTPX, and then also there was discussion on maybe, like, changing the default to use URLib3, just to make the package a bit lighter weight.
So… one route that I was just curious if… We wanted to pursue is, sort of.
Generalizing the exporter to take a protocol, which… request sessions will already implement, and HTTPX will also implement.
To still allow backwards compatibility with some of the existing auth stuff.
That was added, so if you, yeah, so the main file is the, the session.py, the new file, you can kind of see, like, what this looks like. So, basically, if we were to make this change, then we could accept any session that would implement that proto- the HTTP session protocol.
And then we can also, like, if the user doesn't provide anything, we can default to the URL of 31.
So yeah, I was just kind of… before I go further on this, I was just curious, like, if we think this is a good idea or not, There might be some downsides with the protocol approach, because… they're… You know, potential for more runtime errors, but…
**Aaron Abbott** 14:15 Yeah, I mean, this is pretty cool.
I'm surprised, like, were there adapters needed, or it's literally they just both implement the same protocol already?
**Lukas** 14:27 So I kind of designed it with backwards, just to make sure we don't make any breaking changes, so… so requests will implement this protocol, and I think HTTPX automatically implements this protocol, but URLib3 needs an adapter.
**Aaron Abbott** 14:41 Yeah.
Yeah, that checks out.
I mean, I… I think it's pretty cool. I think I… I like this. The, the… I guess, two… I had, like, two, maybe, concerns. One was… If we try this out, and for whatever reason, it's like, oh, this is too much, This is annoying to deal with.
I guess it would be hard to revert the change, just because we'll be making the, like.
you know, in terms of the API, we're making the constructor more… Permissive, right?
**Lukas** 15:13 Hmm.
**Aaron Abbott** 15:13 So it's not just, like, an internal implementation detail right now.
So maybe that's okay, we should just make a decision. And then I guess you mentioned… Maybe I'll stop there. Any thoughts on that?
**Lukas** 15:28 Yeah, I mean, we could implement this and just actually leave the constructor until we're, like, confident that we're… we want to actually change it.
**Aaron Abbott** 15:37 Yeah, exactly, yeah.
**Lukas** 15:40 What else were you gonna say, Aaron?
**Aaron Abbott** 15:43 Yeah, yeah, I mean, we could also do, like.
If we say it's the contract, we could add, like, another overload that takes the protocol and, Or we could, yeah, and then we could, mark that one as experimental in a comment or something like that, but… yeah, the other comment I was gonna make was you mentioned the auth stuff.
Any complications there, or is it just because the auth accepts the session as the interface that it… that just works?
**Lukas** 16:12 Yeah, that was the idea, so the auth should still work, because… well, we wouldn't want to change the documentation to say, okay, the auth object that is returned from the entry point should adhere to the protocol, instead of necessarily being a request session.
**Aaron Abbott** 16:29 Yup.
Okay, I don't know if Dylan's around, but maybe we could just get some review from him since he worked on that stuff, but… Yeah, I think… I think it sounds good to me. I like that.
**Lukas** 16:39 Yeah, I'll, I'll clean this up. It was just, it's just in draft for now, so, no need to review it right away, but I'll, continue working on this. It sounds like there's at least some interest, since I think there's, at least, I don't think request supports, like, HTTP2, for example, so…
**Aaron Abbott** 17:00 Yep.
Thanks, Lucas.
**Lukas** 17:04 Thanks for… thanks for going.
**Riccardo Magliocchetti** 17:08 I also think that HTTP2 is still in competing in URLib3, right? So…
**Lukas** 17:19 Sorry, what was that?
**Riccardo Magliocchetti** 17:20 Yeah, I think that HTTP choose support is still incomplete in, your lib 3.
the reason why I requested here.
Wasn't that?
Okay.
**Lukas** 17:34 And then, yeah, this was, this is the next topic. This one's pretty small, So currently we're using the import lib meta, Backport, for… all Python versions, even though… the… even though 3.12 and higher, we can actually just use built-in import lib meta.
So we can remove, that dependency.
conditionally for versions 312 and above. Ricardo, you mentioned that, We just wanted to make sure that we're aligned on this.
So… Yeah, I'm just wondering, like, what concerns there might be here.
**Riccardo Magliocchetti** 18:29 Well, let me, like, repeat what I read in the comment, but… When we discussed this, that was… I guess, 2 years ago, or something like that.
We were worried about the change of behavior of the… Import lib in, standard lip.
So we decided to use the very same, implementation.
Even if the… The version in the standard lead.
Was, like, add all the required, addPerson function, or whatever.
But, yeah, as I've written here, since two years, Our past, like.
We have two more versions that supports what we need.
And so now, like… We have only… 3.10 and 3.11, but don't have all the… on the, I guess, yeah, imports we rely on.
So, like, for me, it's… Fine?
Maybe… Someone else has opinions. Diego, you already add?
**Diego Hurtado Pimentel** 19:54 Yeah, sorry. This is one of the things that I remember the most, as one of the difficult situations we found.
Years ago, because of the… The braking changes that, the… Importantly, metadata added across versions, so… I am, like, super excited about this. Lucas, you are the author of this PR?
**Lukas** 20:25 Sorry, what was that?
**Diego Hurtado Pimentel** 20:27 Are you the author of this PR?
**Lukas** 20:28 Yeah, yeah, yeah.
**Diego Hurtado Pimentel** 20:30 Okay, alright, so… I just wanted to ask, is this something that will allow us to have a uniform API, for importing metadata from now on. With that, I mean, have we reached the point where we can drop support for the versions that Added these braking changes?
**Lukas** 20:58 Yeah, so it looks like, for all Python versions, like.
at least the specific part of importlib that we're using is… hasn't changed.
I think there's, like, one minor change at 313, but we're not relying on that behavior from what I've checked.
So, I'm not sure if that answers your question.
**Diego Hurtado Pimentel** 21:20 Yeah, what, if I remember correctly, because this was years ago, the… we had this issue because we had to support some Python versions, old Python versions, that had version of imported metadata had, like, breaking changes. I'm trying to remember, right? This was some years ago. So we added, like, a layer on top of that that will allow us to hide those, differences, but maybe we have reached the point where we have prop support for those versions, and maybe we can now have, finally, the uniform interface that we wanted. So I just wanted to ask if that is the situation wherein, if we have, finally.
Drug support for these old versions, and we can live happily ever after with, A uniform interface for this.
**Lukas** 22:27 I think… Aaron, did you want to say something?
**Aaron Abbott** 22:30 Yeah, yeah, unless you wanted to respond to that, Lucas.
**Lukas** 22:32 Oh, I was just gonna say, actually, I'm pretty sure the reason that this was introduced in the first place is that, prior to, I think it's 3… Python 3.10, like, entry points would return a dictionary.
so but now the Entry Points API is pretty much stable.
From 312 and beyond.
**Diego Hurtado Pimentel** 22:58 All right, I'll take a look at this, maybe, I need to… take a look at the… the details to make sure that I am remembering things right. But thank you very much for working on this.
I remember this as a… as a… That's an issue that… cost us, quite a bit of trouble in the past. Thank you, Lucas.
There it is. I don't anymore. That's me.
**lechen** 23:36 Aaron Eusto?
**Aaron Abbott** 23:38 Yeah, yeah, yeah, yeah. So I sent… I sent a link, and I haven't been keeping up with, import lib in the standard library, but this, I don't know if… include whoever's sharing, Ricardo, maybe.
Yeah.
So, this… this is kind of hard to find, but this is, like.
the version of the standard library, since they keep making breaking changes in the standard library that they implement in importlib metadata.
And I think that was also part of the issue, was… like, I think, Lucas, you mentioned it's been stable since 310.
Since it's… so it's okay, and we can, like, you know, obviously have tests for this.
But part of the problem was, it was, like, we ended up writing all this shim code, and then… By the time it was done, we could have just used this library.
Which is what we ended up doing. So, Yeah, I think if the standard lip has been pretty stable for the APIs we use so far, I'm okay to just, get rid of it. It sounds like we still have maybe one more version, Lucas, because there was, like, still a… a case in the PR, right?
**Lukas** 24:43 It's, yeah, it's just 310 and 311, actually.
**Aaron Abbott** 24:47 Oh.
**Lukas** 24:48 I need the import lib metadata.
**Aaron Abbott** 24:52 Is that… is that because of braking changes, or just the functionality's missing?
**Lukas** 24:56 I'm pretty sure it's breaking changes to CMP meta.
**Aaron Abbott** 25:01 Yeah.
Yeah. I mean, I would be okay to just, like, leave it unless there's an urgent need to remove it, because it's…
**Lukas** 25:10 Okay, yeah, I'm…
**Aaron Abbott** 25:12 That's all, dude.
**Lukas** 25:12 We can just wait until 311 is dropped, I guess, but… Yep.
**lechen** 25:20 Yeah, so, I linked in the chat the original issue that, caused us to need to do this.
It was due to the import lib underscore metadata still making breaking changes, and we decided to have just that shim layer that behaves the exact same, regardless of, what Python version that you're using.
And then at that time, we did decide that, like, okay, until… Until, like, this becomes stable, so, like, post 3-10, I believe? Like, we will keep this shim layer. That was the historical context for this, and I guess not everyone has that context, but I would be more comfortable with kind of waiting until then, so… So we don't reiterate, kind of, the same problems that we had before.
It's also funny, because I think Diego worked on this, and then he left shortly after, and then we're still dealing with The same thing as soon as he came back, so… But yeah, thanks, Lucas, for bringing this up. Importlib has been such a headache for us, so happy to get rid of it and use the same thing as soon as possible.
**Aaron Abbott** 26:38 Yeah.
Yeah, and just like, Lucas, did you share some context on how this came up? Was there… because we've had occasional complaints about it being an extra dependency, and then I feel like when we dug into it, we found that it wasn't an issue in those cases, but if people are, like, actively saying, hey, this is creating conflicts or something like that, then we can address it, but otherwise, I agree with Leighton.
**Lukas** 27:04 I actually opened it because, I think, Alex Bowen was making some PRs to conditionally import Imported metadata.
to speed up initialization. So, I was just… and I was just looking through the code, and I'm like, why are we… why are we not, conditionally importing this? So… Yeah.
That's, yeah, kind of the context there.
**Aaron Abbott** 27:27 I see.
**Riccardo Magliocchetti** 27:34 Yeah, this one.
But, the rest is quite unrelated.
Okay.
Next one is Vladimila.
**Liudmila Molkova** 27:57 Yeah.
Yeah, I'd like to share. Thank you.
Okay, so we've been talking previously about, having… Gen AI Focus Triple.
hard conversation about it, to… maybe soften it a little bit. We're doing the same for semantic conventions. We're taking GenAI away from general semantic conventions.
Because they need some different approach. We want to version things separately, we imagine that GenAI conventions might get… A new major version bump.
More frequently than general semantic conventions, we think that the churn, yeah, will be higher, the velocity will be higher than in the general repo.
And, if, probably this… I can apply the same blame for being slow on semantic conventions. So, anyway, don't take it as any… anything to the Python, community, you're awesome.
But you folks have… a lot of Gen AI PRs, you need to, label them. There are people who are interested in Gen AI, people who are not.
And it kinda makes sense to… Try out a different repo.
And then, the… there are, like, a lot of questions, right? So, how do we live in this repo, what we will do in this repo, what we put there, what are the policies, and I'm going to do a quick walkthrough, but maybe focusing more on How does it work for you, and what are the mutual… Dependencies and communications we need to have between each other.
So, let me say just a few words, and there are a bunch of open questions I think we should discuss.
The, plan, so for… for now is that, okay, we… it turns out we have, Some interest from Arise to donate their instrumentation libraries.
And this is not, a formal or approved proposal, it's not on the paper, but it's something we can share publicly now, and they… have a bunch of libraries. We have a bunch of libraries, and what we would do, we would take some of their libraries. There is a criteria, but mostly it's the agentic and inference libraries that we know how to describe semantic conventions, and that they are, active, and they don't have native instrumentations.
And we can migrate them in bulk.
And, precede the new repo with them.
Well, take existing cartel instrumentations out from Python Contrip.
We would release the last version of them, we would point to the new package name. We'll change the package names. So, for example, the pattern would be… the instrumentation, Gen AI, library name.
Yeah, Ricardo?
**Riccardo Magliocchetti** 31:27 No, it's, related, but I've seen something interesting in the text, but please go ahead, I'll ask, go ahead.
**Liudmila Molkova** 31:34 Okay, So, essentially, we will precede this repo with, open inference. We have a skill to migrate, it still needs some polishing, but it's pretty promising.
We'll port existing ones, and we'll drop any legacy as we port.
I'll make sure that the… there are links from PipePy and from… from old PyPi and from Python country to new places, so people know where to go.
And there are, like, probably a bunch of rules we wanna… start with, but they're just the practices that we already probably do in the Python Country repo, just slightly more focused on Jenny A stuff.
So, if… I think what's an interesting question, like, what we do with stooling, how much of it we take from Python country.
The goal is to just drop any bad practices and enforce as much as we can that's reasonable with… in the new repo, because it's a greenfield.
Okay, I have talked a lot, and I want to talk about specifics of, like, coordination between two different things, but I want to hear your high-level Thoughts on this, or questions?
Yeah, Diego, go ahead.
**Diego Hurtado Pimentel** 33:15 Yeah, thank you.
So… From what I understand, you're planning to move, One instrumentation from the country repo into its own repo, right?
**Liudmila Molkova** 33:30 A bunch of instrumentations, from Gen AI, plus instrumentations we don't have.
Yeah, it's from a project called Toppen Infront.
**Diego Hurtado Pimentel** 33:44 Right, okay, yeah.
**Liudmila Molkova** 33:47 rents.
**Diego Hurtado Pimentel** 33:49 Okay, okay. Question. So, the idea is to put each one of them into their own repo, or are you creating a new repo that will hold them all?
**Liudmila Molkova** 33:59 It's the new repo, this one.
**Diego Hurtado Pimentel** 34:03 Okay.
Years ago, I… I was also thinking about, how things… Could be, and I had this idea that maybe it's better to have one repo per package, because in that way, the Git history doesn't get, I mean, it's, independent for each package, so just a suggestion, maybe that's something you want to consider.
The other thing is, the… one of the things… the reasons why I think we followed this approach, if I remember correctly, was, Because we were… we wanted to be able to test all these instrumentations with every release that we make, so that we make sure that nothing breaks. Now.
That doesn't mean, I think, this approach that you're proposing is wrong. On the contrary, actually, I'm gonna lean more forward to this approach, where there is one repo per package.
I just wanted to… to, to tell you that, in case that, you want to maybe, think.
Or consider some approach, to test your… Your new, instrumentations with every release.
of, the core API and SDK.
So, just that, just a couple of, maybe, suggestions for you.
**Liudmila Molkova** 35:45 Yeah, so I think we need one repo for all of them, because we will do cross-instrumentation changes a lot, and having a repo per package, and we'll have A lot of them, seriously. Like, I can show you the full list of things that exist in the ecosystem.
And I don't know how many there are, but it's… the list is pretty long. I don't think it's feasible to have repo per each, and there are a lot of cross-cutting features that will update… be updated at the same time. It doesn't mean we cannot test, so I think that today, how we… we tested is through the latest and oldest, and we can include up in telemetry API, SDK, semantic conventions, and whatnot.
In each of them.
**Diego Hurtado Pimentel** 36:35 Really quick. Okay, okay.
Alright, no, seems like, you have already figured it out.
Thank you.
**Liudmila Molkova** 36:43 Yeah, I think.
**lechen** 36:43 Thank you.
**Liudmila Molkova** 36:44 Yeah, Leighton?
**lechen** 36:46 Yeah, also for some context, back when Diego suggested the splitting up of instrumentations, it was mostly due to the annoyance of having to release all instrumentations in lockstep, every time we release.
I think that is mostly solved now with the per-package release and everything, so that was the primary motivation behind the idea. We didn't wind up going through with it, because, like, the kind of the… the tooling overhead and, like, like you said, the cross-instrumentation changes Also made that other idea kind of unfeasible as well.
So that's primarily the reason why, we suggested that.
Just for cover context.
**Liudmila Molkova** 37:31 Yeah, thank you.
Yeah, Ricardo?
**Riccardo Magliocchetti** 37:39 Yeah, this was mostly, like, a curiosity.
like… Like, like… When I read, like, the open inference name on the doc, I was surprised.
And so… Yeah, like, so the plan is to merge also the semantic convention where Topper Inference was… Is the instrumentation are you using?
Cool.
**Liudmila Molkova** 38:13 So, Open Inference has their own conventions, I think they are enabling support for the hotel ones, but, what we… we… I don't think we should take their instrumentation libraries as is, assuming they will donate that.
But what we will do is that, as a part of this bootstrap process, We would, rewrite… their instrumentations to essentially use, Gen AI tools.
And throw it follow.
Autel semantic conventions.
So we will not… All traces of open inference would disappear as we go through this process.
**Riccardo Magliocchetti** 39:03 So, like, is this, like, a donation, or… Some of you guys, like, ugh.
**Liudmila Molkova** 39:10 It's a donation…
**Riccardo Magliocchetti** 39:11 Donated? Okay.
Triple, sorry.
**Liudmila Molkova** 39:14 they are considering it, right? And if they, make a proposal, what we would do is we will, go through this migration story, and we would change copyrights. It's very unethical to take Dear quad.
and just translate it to ours, and we cannot really remove their copyrights if we do this without the donation. So the donation is, them allowing us to use this however we want, and replace copyrights.
It will not be donation of the code.
as is, at least this is, what I'm thinking, does it help?
**Riccardo Magliocchetti** 39:59 Yeah, yeah, thanks. Later.
**lechen** 40:03 Yeah, so Lumila, I think a couple of us from the GenAI side have already reviewed this. What do you need specifically from the Python community to help you move this forward?
**Liudmila Molkova** 40:15 Right, so I think there are some questions that affect us both.
The… was the instrumentation decoupling from the core… from the contribo.
We'll still depend on up and telemetry instrumentation, and not telesemantic conventions.
And, well, these packages remain de facto stable, I think, mostly.
Long term, I think we should try to stabilize them and, like, make them V1 in the core repo, since we're going to depend on them from a different place.
I'm kind of curious what you folks Think about this one. And it's not, like, something we will need to do right away, but, like.
In 2026 timeline.
**lechen** 41:11 Yeah, so if we were to itemize the, kind of.
topics that relates to Python SIG, specifically, it would be, like.
and I'm sure we can create an issue for this, too. It's like, oh, let's try to stabilize the dependencies that instrumentations might rely on, like semantic conventions and instrumentations, as well as, do we want to include a open telemetry distro of a Gen AI, something like that.
And how does it relate to the already existing OpenTelemetry distro existing in Python? I would think those are the… open items for at least the… this repo side. Correct me if I'm wrong or missing… if I'm missing anything.
**Liudmila Molkova** 41:57 Yes, you're right. Yeah, so… this reference or cross-repo concerns.
Maybe we can talk about them before that.
The big question… It's, like, your repo. You… How do you feel about the split? We talked about it before.
Do you… does anybody have any remaining concerns around this one?
**lechen** 42:35 This, this is fine to me.
I like this idea.
**Liudmila Molkova** 42:40 Okay. If anybody has any thoughts later on, feel free to ping me, or Aaron, or someone else, maintainer, about it, but let's talk.
**Riccardo Magliocchetti** 42:51 You have a question?
**Liudmila Molkova** 42:53 Huh.
**Riccardo Magliocchetti** 42:54 Like, yeah, here, like, the… You, you're thinking on… Like, an optional dependency on the distro package?
**Liudmila Molkova** 43:05 Yeah, for the distro, it's interesting, so how do we do this?
Having two distros would be… Difficult, right?
Would we… Could we do something like this? There are a bunch of questions we will need to figure out. What is the versioning? If we bump Gen AI to a new major version, what would it mean for the… the open telemetry distro.
I'm looking at you folks who own telemetry Distro to share your feedback on this.
**Riccardo Magliocchetti** 43:46 Yeah, like, I'm a bit confused, but, like… Like, what dependency will it add to the distro package?
**Liudmila Molkova** 43:57 It will discover if any of the GenAI libraries are present, right? GenAI instrumentations, and would call GenAI the instrument or instrument on the corresponding packages, if they are present. So the dependency would be the… Soft.
Okay. Runtime, discoverable, dependency on… All of the open… sorry, all of the GenAI instrumentations from the other repo.
**Riccardo Magliocchetti** 44:32 Yeah, so, like, the instrumentation are not instrumentation, like… Hours?
**Liudmila Molkova** 44:40 Oh, it's just from a different repo.
**Riccardo Magliocchetti** 44:44 Yeah, it's… And so, like, even… I don't understand why we need the option, On the distro package. Maybe it's me, I don't remember what the distro package does, but… .
**Liudmila Molkova** 45:05 Yeah, Erin?
Maybe you have… Yeah, yeah.
**Aaron Abbott** 45:08 But I think, if my understanding of this plan was we could include this, extras in OpenTelemetry distros that people can install the GenAI packages, easily, but the idea wasn't to depend on Distro in… the new Gen AI repo, right?
**Liudmila Molkova** 45:26 Right, yes.
**Aaron Abbott** 45:28 Does that make sense, Ricardo?
**Riccardo Magliocchetti** 45:30 Yeah, but, like, the package, like, it's sometimes a… I have to check again what the distort package does, but as far as I remember, it was just configuration.
So, yeah.
**Aaron Abbott** 45:46 Yeah, that's fair. So maybe, like, the contributions all package.
**Riccardo Magliocchetti** 45:50 Yeah, exactly, yeah.
**Aaron Abbott** 45:52 Okay.
**Liudmila Molkova** 45:54 So it seems there are some technical details to figure out here. Directionally, I would push for one distro and… figure out how to include or not include Gen AI.
There.
For some options.
**lechen** 46:11 Don't want to go too deep, but I thought OpenTelemetry Distro was needed for the zero-code scenario.
Specifically.
It's not really.
**Liudmila Molkova** 46:20 Yeah.
**lechen** 46:21 like, know of Gen AI instrumentations, right?
**Liudmila Molkova** 46:25 Yeah, and it's a question what should be included there, and how… what should be included there by default, and how to expand it?
all I want to figure out is what are the feelings about just one distro for everything, and inclusion can be discussed separately.
**lechen** 46:47 Right, yeah, I think… I think a lot of these concerns can be separate from the fact that we want a separate repository to hold all of these components.
It would then just be, like, a request or, like, an issue to the Python community, because, like, hey, like.
We need to stabilize OpenTelem Transportation, can we push the issue?
Like, similarly to… Any other process that we follow.
**Liudmila Molkova** 47:15 Yeah. Yeah. Go ahead, Terry.
**Aaron Abbott** 47:19 Oh, sorry, I was gonna say, I think it's just a terminology issue, so this distro thing… predates when we had, like, Distro in the spec, and I think the… The distro package doesn't, do any of the installation, it just has, like, some setup hooks that it can use, so… I think you mean colloquially distra will have a single, like, distribution that has both, right?
**Liudmila Molkova** 47:43 Right.
**Aaron Abbott** 47:44 Okay.
Cool, just wanted to clarify, thank you.
**Liudmila Molkova** 47:47 Yeah, thanks. I don't… I want to take all the time for this. The last thing I wanted to mention, that there is a special thing… thing for bedrock, for… because bedrock is part of bot instrumentation.
I think bota Instrumentation should stay inside the country repo.
And it will ultimately need to take a dependency on a released version of GenAIOTOS.
It introduces some interesting circular dependency, but this is… Duh.
based on the released version of Gen AI tools, it should be solvable.
You're surprised, Clayton?
**lechen** 48:34 Oh, that's… I guess that's a… Yeah, that is a surprise face. Yeah, no, I was just being like, oh, okay, interesting that we have a scenario like this.
**Lukas** 48:45 Actually, for… at least for BotoCore, we could look into actually, like.
splitting off the GenAI-specific functionality into… move it into the GenAI repo, and then… just have it as an extra in Boto Core.
To pick up that library, and then we would just… you know, do everything we need to do there, because I think the Bodo… like, BodoCore is set up so that they have, like, an extension set up, so it'd be pretty easy to externalize, like, the GenAI-specific instrumentation logic and pull it in when we need it.
**Liudmila Molkova** 49:21 Okay, interesting. I'll ping you, because I'm curious, what would be the best outcome for end users. I mean, we can split, we can keep things as they are. Ultimately, it's the… user experience, that should be important, but I think I've got, just general Okay, Shresponds, and if you have any additional thoughts.
Please reach out, we'll keep polishing it from the GenAI side as well, and it's definitely not the end of the… this discussion. Thank you.
Going to stop sharing.
**Riccardo Magliocchetti** 50:05 Thank you.
Next one is Redima?
**Ridhima Satam** 50:17 Yeah, so this is just a PR for the Langchain.
instrumentation, adding workflow support, since we have all these types in the GenAI utils, so… It's that and some refactoring. We have new APIs in the generutels, for the handler, so just adding that here.
You will see more, PRs from me for the lan chain, introducing agent invocation and tool invocation and other stuff, yeah. So just asking for reviews.
Thanks.
**Liudmila Molkova** 50:54 Redima, sorry, I have a stupid question, and I probably can't answer it by looking into the code, but we are reusing the blank chain handlers for this. We are not, like, doing the manku patching, right?
**Ridhima Satam** 51:07 No, we are using the callback handler, yeah.
**Liudmila Molkova** 51:10 Okay, cool. Yeah, it's another thing I want to discuss at some point, but not right now, but not related to your PR, thank you.
**Ridhima Satam** 51:19 Yeah, and this package was also not released yet, so… I mean, just want to mention, like, I think you were talking about separating out the journey and… It has no backward compatible issues with the refactoring as well, yeah.
**lechen** 51:35 I know that, Magkumar, published a bunch of PRs related to Langchain conflict with any of that?
**Ridhima Satam** 51:44 Okay, I didn't look at it. It's there?
Oh, okay.
**lechen** 51:49 I know, like, 5 different PRs, so… I think he's oof?
For, like, a week or so. I haven't taken a close look at the rest of them, but just wanted to Could you, who's sharing? Ricardo, are you sharing right now?
**Riccardo Magliocchetti** 52:08 Yes.
**lechen** 52:09 Would we have to add the GenAI tag to this PR as well?
I feel like we need some systematic way of identifying these things. But yeah, like, feel free to take a look at his open PRs. There's, like, 5 of them related to Langchain. I don't know if it's exactly conflicting with what we're doing, so…
**Ridhima Satam** 52:26 Okay, let me see, and even if he's using the JNI utils, I have to talk to him, but yeah, thanks for pointing that out.
**lechen** 52:38 At least with my brief preliminary reviews, he's not using GenAI util, so…
**Liudmila Molkova** 52:47 I think I left a comment on one of his peers that it's not… Not a great approach.
For not using hotels.
**Riccardo Magliocchetti** 53:03 Alright, thanks!
Luke Mita, see you again.
**Liudmila Molkova** 53:08 Hello, yeah, Montana C. I, I, it's just… okay.
Canceled.
**Riccardo Magliocchetti** 53:19 Okay, also respond, yeah.
**Liudmila Molkova** 53:21 Thank you.
**Riccardo Magliocchetti** 53:23 Thanks, Ethan.
And later, you're next.
**lechen** 53:29 Yeah, so, real quick, I updated this PR based off of the feedback that was made.
I think Lucas left a really good suggestion for using just simplifying the logic, just TLDR, this is just to kind of enforce the, The… the baggage header size limits, for… outbound requests as well for the inject call. We already enforced this for extract, but, just trying to abstract it out and then apply it for both sides, so… I think… was it Dylan who suggested the… the bite size?
Issue? Yeah, it was Dylan. Yeah, so, I did take this feedback, and it's like, yeah, we should probably not… kind of change the behavior in which, like, we just reject the whole payload if there is non-ASCII characters. So what I did was, per entry, we need them to be ASCII, so that the length Is accurate, but… Prior to iterating, the entire… header… is encoded to… You know, make sure that none of the… it doesn't exceed the entire, kind of, length.
Feel free to take a look at the logic, so… Yeah, Aaron.
**Aaron Abbott** 55:01 If I understand right, like, the original issue was that… was it… was it that the context would get too large, or was it, that it would cause, like, an oom. It's like an attack vector or something, because I'm a little… Yeah.
Because if we do the encoding, then it's gonna… Consume memory, right?
**lechen** 55:21 Yeah, I didn't want to say anything, because I thought it was, like, a… Like a, you know, like a security thing?
But the original problem was that, like, people can fill up the… unbound header.
I was debating on… like, not using encoding, and just, like, dropping the whole header if there are any ASCII characters, because checking if… is ASCII is much more trivial than coding.
But I didn't want to change the already existing logic of, like, We accept pairs.
That are valid.
And we just drop pairs that are invalid.
Just wondering what you thought about that.
**Aaron Abbott** 56:10 Yeah, makes sense.
I'll take another look at the thread, sorry.
**lechen** 56:16 Yeah, yeah, no problem.
And, yeah, feel free to… Talk in Slack, too, if, For, like, privacy reasons, those things, so…
**Riccardo Magliocchetti** 56:34 Thank you.
And this was the last topic for today.
Any last-minute topic, or you have 3 minutes back?
Okay, so… Thanks, everyone.
And see you, have a nice day.
Bye, bye.
**Liudmila Molkova** 56:58 Kim.
**Lukas** 57:00 Thanks.
**Diego Hurtado Pimentel** 57:02 Thank you, bye bye.
**Erdenesaikhan Tserendavga** 57:05 Thank you.
