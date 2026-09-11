SIG: Python SIG
Date: 2026-09-10
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Riccardo Magliocchetti** 01:49 Hello, everyone.
**Dylan Russell** 01:54 Whoa.
**Aaron Abbott (Google LLC)** 02:15 Oh, how's it going?
**Tammy Baylis** 02:27 Hey, Erin, hey everyone.
**Aaron Abbott (Google LLC)** 03:17 Maybe I'll share today?
Do you want to, Riccardo?
**Riccardo Magliocchetti** 03:25 Please go ahead, thank you.
**Aaron Abbott (Google LLC)** 03:28 problem.
Can everyone see okay?
**Tammy Baylis** 03:39 Yes.
**Aaron Abbott (Google LLC)** 03:42 Oh, actually, Tammy, did you wanna… Hey.
**Tammy Baylis** 03:45 Yeah, I'll… I'll share to start.
Oops.
But I'll, aaron, I'll need you to stop sharing.
**Aaron Abbott (Google LLC)** 03:54 Yeah, yeah, yeah, sorry, sorry.
**Tammy Baylis** 03:56 Okay.
Friends… Yeah, we'll wait… I'll wait one more minute.
Usually wait till the 5.
Okay, huh, let's get started.
Yeah, welcome back to the Python SIG meeting. The meeting notes are in the chat. I'm gonna start with some triage using these boards.
Before we get started on that, I wanted to point out… how… how short this list is today, and I don't think it's covering everything. For example, I… put in this PR… oh, I created it ages ago.
But it's finally ready, and 2 days ago, I routed it to the reviewers.
Hopefully correctly.
4300, it's not on the reviewer's list, so… Maybe someone could have a check on that.
hopefully I'm on the right issue as well.
**Aaron Abbott (Google LLC)** 06:24 Yeah, no, I've noticed sometimes the dashboard needs, like, manual bumping, so it's possible that some of the PRs are just, not getting picked up.
**Tammy Baylis** 06:36 Yeah, okay.
This one looks a bit more promising, this is for the core.
Or PRs. So I suggested we look at the waiting on reviewers list first. I'll do a little bit of that for a few minutes.
But this… This one's very old, I'm curious.
**Aaron Abbott (Google LLC)** 07:02 Yeah… I… I think I took a look at this one, and we went back and forth on the issue for a while, but… I… Had some concerns with just… Yeah, it's pretty conflicted now. But I had some concerns with just, like.
The amount of hooks that it adds, and generally it feels like whack-a-mole for us to have fork safety.
So…
**Tammy Baylis** 07:29 Do you have a card?
**Riccardo Magliocchetti** 07:31 Like, Tammy, if you scroll down a bit, there is, another PR referencing this.
What an issue, yeah.
I think.
**Tammy Baylis** 07:44 Yes.
**Riccardo Magliocchetti** 07:45 AI is mentioned that… We may need just a subset of that.
So, yeah.
maybe, like, I reopen that to not forget.
But I think, yeah.
Somewhere, what is it looking into it.
**Tammy Baylis** 08:10 Okay.
**Riccardo Magliocchetti** 08:12 So.
**Tammy Baylis** 08:12 Oh.
**Riccardo Magliocchetti** 08:13 Maybe we can close that.
See what a subset could look like.
**Tammy Baylis** 08:43 Great, thank you for that input.
That's a bump, we're not gonna look at bumps.
From bots, but this is, Docs SDK, remove stale trace config to do.
Oh, interesting.
There is a link tissue.
Yeah.
Okay… I think that's correct, Ben.
Oh.
**Riccardo Magliocchetti** 09:35 Oh my god.
**Tammy Baylis** 09:35 Okay.
**Riccardo Magliocchetti** 09:36 Didn't expect it.
**Tammy Baylis** 09:43 I think that's okay, sure, no, we'll just do an easy review.
Not sure if that solves, but whatever.
Next one… They're docks. Oh, more about free fork servers.
AG0708… We do have some hotel.io docs on this.
But… So they're just adding to the existing example.
for metrics… I think that's valuable to have.
Sorry, it's 9-10, I think we have other topics. We can come back to this later if we want to.
I guess back to you, Erin, today?
**Aaron Abbott (Google LLC)** 10:59 Yeah, sure.
**Tammy Baylis** 11:01 Thank you.
**Aaron Abbott (Google LLC)** 11:05 Alright, cool. Diego, you've got some topics you want to kick it off?
**Diego Hurtado (Dash0)** 11:13 Yeah, let me just click that one, please.
Alright, so… I think last week we had this, conversation regarding what to do with, Contributors who… who approach us with, New instrumentation they would like to add?
And we have no policy.
So, I tried my best to describe the situation we're in.
And the proposal I have… I try to be… quite, exact.
To avoid, misunderstandings.
So… In essence, the… sorry, the important point that I'm making here is that I believe That, we should abandon this idea that, We can count on other people to maintain an instrumentation we accept into this repo.
what I'm pretty much saying is that if we do accept an instrumentation in a country repo, we pretty much have to assume we will be maintaining it ourselves.
So… that's my point. When… if we're gonna make a decision, On any instrumentation.
I think that's what I think we should, keep in mind.
Something else, somebody, if you scroll down, Aaron, please, to the bottom.
Yeah, the very bottom, yeah.
Okay, yeah, somebody else… even… yeah.
Go down, right there. Somebody else, I think it's asking… This… this was opened 2 days ago, yeah.
Yeah, exactly. Some… somebody else wants to implement a… a contribution, right? So, just, dragging it there.
Because it's, didn't happen only once, but it's happening here again.
So I would love to hear what you think about all this, what do you think about this idea that if we accept something in in country, we have to assume that we will be the ones maintaining it. What do you think about that?
**Aaron Abbott (Google LLC)** 13:50 I mean, that makes sense to me, I think, ultimately, we might end up in that situation.
Dio, what's, like, the… Proposal for this issue is, do we want to, like, have a… Markdown file in the repo that lists this, or, like, what's the action here?
**Diego Hurtado (Dash0)** 14:12 Well, yeah, good point.
my… My point is, I mean, if… if you agree with me that, If we accept something in country, we… have to… take the maintainership of that object, then what I will propose is just to write this down in a… in a document saying.
If you're… If you want a contribution to be added to the contribut repo, please present it, we will evaluate it, and we will decide if we want to Accepted or not.
And we can explain, be transparent. The reason why we may reject it, it's because, if we accept it, we must, make the commitment to maintain it, and we may not be able to do that, and so on. So, this, basically just, changes nothing in our side. I mean, it leaves us… Free to decide on every… on every particular case, right? And it also gives, gives the… The rest of the people who may contribute, an explanation.
On what to expect if they propose And… a package to be added to Contra.
**Aaron Abbott (Google LLC)** 15:51 Okay, so… I think I see what you're saying. Anybody, anybody else have some thoughts?
**Tammy Baylis** 16:04 Yeah, thanks, Diego, for putting this together and the summary of last week. I… I think it's… it's a good idea to definitely have something in writing and in more plain sight than we currently have, just, like, tucked into the contributing.md of each repo. So I think, at least for visibility, this will be good.
And, yeah, the second possibility of A rejecting X 100% of the time, I don't think is good for… contributor morale, I guess, and general confidence, so, Depending on bandwidth on a case-by-case basis, I think, realistically, it would have to be our jobs to continue to maintain things that are dropped in.
**Diego Hurtado (Dash0)** 16:55 Correct, yeah, I… I think that the exact same thing, yeah.
Okay, if you're okay, I can write, I can create a PR for this issue that pretty much adds, what I've just described to the contributing document, so that, it's, it's a bit easier to understand what I'm proposing here.
What do you think?
**Aaron Abbott (Google LLC)** 17:23 Yeah.
Sounds good. I would say… like… Ultimately, I think there's still not gonna be a policy, it's still just gonna be, like, case-by-case basis, so…
**Diego Hurtado (Dash0)** 17:33 Sorry, I mean, the policy will be that we will evaluate on a case-by-case basis. That's my point.
**Aaron Abbott (Google LLC)** 17:40 Yep, yep, I gotcha.
What do you think about if we made… I don't think we have any issue templates right now, besides, like, the main one?
But, like, I know… oh, we do. What if we added, like, an issue template for this,
**Diego Hurtado (Dash0)** 17:56 Oh, totally.
**Aaron Abbott (Google LLC)** 17:56 Hello.
Yeah, we can update contributing as well, but that seems like a nice… Nice way where we could just link the issue template.
I think you can do, like, the link.
Okay.
**Diego Hurtado (Dash0)** 18:14 Alright.
That's… that's it on my side. I don't know if anyone else has any comments or questions.
**Aaron Abbott (Google LLC)** 18:26 Cool.
Alright, next one is also you, Diego.
**Diego Hurtado (Dash0)** 18:31 Right, okay.
Okay, yeah, I don't know, is Lucas here?
I think Lucas is not here, right? Oh, what?
Yeah, okay, real quick. So, I've been working on this… For a while.
For the packaging slash injector project, we would like to, remove some dependencies.
from our components.
PortableBuff being one of them.
And, the effort to do that includes… making a pure Python implementation or protobuf, or an implementation of Protobuff in some more language.
Now, I am proposing here doing it in pure Python, the possibility of making it rust is something that, we had discussed before, Lucas mentioned it here. I don't disagree with making, with… implemented it in Rust or any other language, the… I mean, what I want is just to avoid the portable dependency. Something that Lucas mentioned in the first comment.
added here is that… is to make this a separate, package in country, which I also don't disagree with, but, here's the catch.
If, we… what we're trying to do, or at least what I'm trying to do here, is to avoid the… A protobuf being a dependency in the virtual environment.
where the application runs, right? So… If the SDK or any component of the SDK has protobuf as a dependency, then we will… end up using… having Protob as a dependency, even if we use another extra package, that, does, this, this job, right? So… I'm… I will… like to investigate if there is a way that we can install the SDK. I guess it's possible using these arguments that go in square brackets.
That, allows the user to select… a non-protobuff implementation, so that they end up without protobuf in their dependency package. But, that's something I still need to investigate. In any case, I wanted to bring this here, hopefully, discuss this with Lucas. Lucas is not here, but in any case, if any one of you have questions or comments, I'll be glad to… Here upon them.
**Aaron Abbott (Google LLC)** 21:49 Yeah, I think… I think I mentioned this last time, but… I'm a little concerned about the maintenance burden of this thing, like… it sounds like, I was looking here, ultimately the goal is also to have a pure Python gRPC implementation. It just feels like a… Lot of custom code to maintain here, and… We could start with that, but I have some other thoughts as well, so… Well, yeah.
**Diego Hurtado (Dash0)** 22:20 This PR is only 15,000 lines, so it's not that much code to maintain. No, just kidding. Yeah, sorry, I think I said something… I said something wrong. My ultimate goal is not to have a pure Python implementation of Protogov here. My ultimate goal is to not have protogov as a dependency. So, if we implement this in Rust, or in C, or whatever other implementation that saves us.
From having to… Have all this bunch of code. I… I am open to that.
I don't see that as a problem, so I just want to clarify, because I think I gave the wrong impression that I strictly wanted a pure Python implementation as part of.
**Aaron Abbott (Google LLC)** 23:11 Yeah, I hear you.
like, so the other thing we discussed was, for the injector, the, like, this was the use case, and we're working on the JSON exporter as well.
I think there was some technical issue with the configuration that meant that it couldn't be used easily in the injector, but… Does that not also solve the goal of not having, protobuf as a dependency?
**Diego Hurtado (Dash0)** 23:35 it helps, but it doesn't solve the problem. What I mean is that the… a couple of things. First, I think the JSON implementation right now also carries a third-party library, which is urlib3.
Which may be less problematic than Protobuff, but, I mean, it's still a third-party library, right? The other thing is that, JSON by itself is, if I'm not wrong, Has, has a lower performance, because it's, it's, it's more stuff that you need to send, right?
the protobuf, has a more compact encoding, so it's, it's more performant. So, JSON is good, we still want JSON, we still want that, but we also like, To have this thing, right?
**Aaron Abbott (Google LLC)** 24:35 I guess so, but I don't know if that's… like, we could test that?
I do… I don't know if having… so is the goal to have no dependencies? Because your All Lib3 is, like, a pretty… common… common one that people are likely to already have, right?
**Diego Hurtado (Dash0)** 24:51 Yeah, I think the… your lib is less problematic, not because it is uncommon, but because the… the range of supported versions is wide, so we… It's… it's easy to satisfy.
It, the dependency tree of, end user.
with the requirements of your lead 3 that we have for JSON. That's what I mean when I say that it's less problematic.
**Aaron Abbott (Google LLC)** 25:25 Yeah, I mean, the same… the same thing is also true for Protobuff, right? You could… they have an N plus 1 rolling version support now?
I, I won't…
**Diego Hurtado (Dash0)** 25:33 Wow.
**Aaron Abbott (Google LLC)** 25:34 I won't say this has been painful in the past, but they did take steps to fix this. And I'm not trying to say I'm, like, opposed to this, I just want to make sure that we're solving the same issues with With whatever approach we choose.
**Diego Hurtado (Dash0)** 25:49 Yeah, the… That's true.
I guess my point will be that any of these approaches, JSON or this, they are not, opposed to each other, right? We can have them all, and the ideal situation I see is we… we get the ball. We… Jason is good, this… this is also good for us, So yeah, it's not one ordeal.
**Aaron Abbott (Google LLC)** 26:23 Okay. I feel like I've said a lot. Anybody else have some thoughts?
**Riccardo Magliocchetti** 26:32 Yeah, we just added a comment.
about an experiment I did in converting the OPMP client using another protocol of implementation.
And… like… Also, like myself, I'm not opposed to another exporter, not using Protob, but not so… Eager to… to merge, A protocol of implementation we have to maintain.
**Diego Hurtado (Dash0)** 27:06 Right, yeah, you seem… I… that's why I am so, so open to the idea of… Using an already… existing implementation in Rust or C that will allow us not to have another implementation we have to maintain. I hear you. I also don't want to maintain a Another protocol for implementation.
**Riccardo Magliocchetti** 27:28 and said that, I think that, I think, I think Iroh already pointed this out, but… I'm not sure, like, if the issue we have with Protob right now Also, like, another dependencies may have the very same one.
**Diego Hurtado (Dash0)** 27:49 Yes, I'm also working on trying to get rid of packaging.
But that's another topic.
**Riccardo Magliocchetti** 27:57 No, no, no, I mean, another part of implementation can have the same issue with, but, like, sometime in the future, there will be, like.
well became more strict about the… whatever, Version… We or our instrumented application may use.
So, like, what the same problem we have with Protoba Friend now, We can have maybe the same issue with other implementation.
And I'm not sure about that, but…
**Diego Hurtado (Dash0)** 28:38 You mean that, if we… Add an implementation in another language, we may also end up yes.
having the same dependency problem? I'm not sure, because, It'll be… it won't collide with… The… what the end user has in their virtual.
**Riccardo Magliocchetti** 29:04 What, Buster?
**Diego Hurtado (Dash0)** 29:04 The late…
**Riccardo Magliocchetti** 29:05 We may also use this diff… like, a different version of the very same one we switched to.
solo.
**Diego Hurtado (Dash0)** 29:13 Wondering about this.
**Riccardo Magliocchetti** 29:14 But, like, I…
**Diego Hurtado (Dash0)** 29:15 Yeah, yeah, good evening, a good point.
**Riccardo Magliocchetti** 29:19 I'm pretty sure I don't understand What?
**Diego Hurtado (Dash0)** 29:26 That's a good point, I will have to investigate it.
**Riccardo Magliocchetti** 29:28 Yeah. Okay.
**Diego Hurtado (Dash0)** 29:31 Yeah, yeah, but it's a… it's a good point.
**Aaron Abbott (Google LLC)** 29:39 Yeah, so maybe one more thought, because I think… I think we discussed this last time, but from my perspective, you know.
Write something down here.
From my perspective, there's kind of, like, two main problems, because… There's, like, a Hurt Abbott dependency.
And then the other issue that I've seen is that And I don't know if this applies to the injector, but it definitely applies to the CADS operator, but native code, Requires you to know… the AVI ahead of time. So, like.
The first one is solved with… using, like, not using the official protobuf, so I think like this PR that you opened, or using Post, or something like that. And this one seems to be solved, And only if you use pure Python, so…
**Diego Hurtado (Dash0)** 30:41 Yep.
**Aaron Abbott (Google LLC)** 30:42 From my perspective, that's why I like the JSON solution, because it solves both of these without having to re-implement, like, protobuf and gRPC.
so I… I agree we can, like, support multiple things, but I think… Keeping it limited would be good, as long as it solves the use cases that we have, and not just have, like.
You know, a bunch of different options available.
**Diego Hurtado (Dash0)** 31:06 Yeah.
That, it is true that, we… For any compile solution, we will have to support multiple architectures, yeah, that's… that's an issue.
Sorry, I think Leighton had a… Got a question?
**Leighton** 31:28 I don't know if this is, like, a dumb idea or anything, but In order to maybe address the maintenance burden, and also kind of, Maybe address the dependency?
Is it possible to have, like, a… separate, like, lightweight OTLP exporter, maybe?
Like, in which we don't take a dependency on protobuf, and we have some… like, generated… private OTLP wire encoder or something.
The downside would be we would have to maintain two different exporters.
But at least this… Kind of opt-in package.
If needed, it doesn't have to… You know, follow… Like, sorry, the normal exporter keeps, like, the mature protobuf and gRPC behavior.
While the other one kind of… like, still… sends via OTLP, but perhaps uses, like.
URL lib, or something like that.
**Diego Hurtado (Dash0)** 32:41 Write that down for me, please.
**Aaron Abbott (Google LLC)** 32:47 And Leighton, isn't that kind of what this proposal is?
**Leighton** 32:52 Well, isn't this proposing to rewrite the… rewrite the OTLP exporter completely.
**Diego Hurtado (Dash0)** 33:03 It is… no, it is, the proposal here is to rewrite Protobuf.
**Leighton** 33:13 No, no, I meant, like, instead of following, like, the generated classes with protobuf, like, create a separate OTLP exporter that doesn't conflict with the already existing, Next quarter.
**Diego Hurtado (Dash0)** 33:32 Yeah, but how is this new exporter going to… export in Protobuff without any protobuf implementation.
**Leighton** 33:51 Oh, sorry, I didn't know that was a… requirement, I thought we were just trying to serialize LTLP, Without the dependency.
**Diego Hurtado (Dash0)** 34:03 Yeah, but in order to do that, we need some implementation of Protob.
Either it's pure Python or something else, Rust or whatever.
**Aaron Abbott (Google LLC)** 34:16 Yeah, there's some non-trivial stuff, like, like, variant encoding and things like that, which… Or implemented here.
**Diego Hurtado (Dash0)** 34:27 Exactly, yeah.
**Aaron Abbott (Google LLC)** 34:32 Yeah, and I think… I think the Rust solution could solve that problem, but then it doesn't… it doesn't help with the other cases we're having, like a pure Python implementation would be helpful, so… you know, maybe these problems don't need to be solved together, but I do feel like the JSON exporter solves it, and we should, you know, like, look at benchmarks, and if there's really A huge cost to… JSON vs. Protobuff, I… I think… you know, you can always use compression, and I don't think that doing the encoding… I think the JSON encoding is probably a bit cheaper in general, like, in terms of time, than doing all this stuff for Protobook, but… It'd be good to have some numbers, I think.
**Diego Hurtado (Dash0)** 35:11 Yeah, if you can write that down in the issue, I'll… I'll take a look and I'll do the… the investigation.
**Aaron Abbott (Google LLC)** 35:19 Okay, yeah, I'll copy over what I put in the notes here.
And then we can take the discussion there. Sounds good?
**Diego Hurtado (Dash0)** 35:26 Perfect. Thank you very much.
**Aaron Abbott (Google LLC)** 35:28 Really?
Anybody else have thoughts on that one, or we'll go on to the next issue?
This one's you, Tammy.
There should be some columns.
**Tammy Baylis** 35:44 Yeah, thanks. Just, My mic sounds funny. Yeah, we've had this out for a little while, there was some back and forth. I think it's ready for reviewers.
Except… I'm… there's so many PRs for docs, I'm getting mixed up. Maybe there was a changelog fix, or maybe that was a different PR, but anyway, it would be good to get this, Yeah, that was the one, actually. Approved and merged, to add to each instrumenter's, read the docs about how to opt into the modern HTTP sendConv.
And yeah, there's, downstream PRs that kind of depend on this. One is for the database SEMConf opt-in, and then there's also an OTel.io update.
Waiting on these, so yeah, please, please have a look.
**Aaron Abbott (Google LLC)** 36:43 Awesome. Is there anything, like, in particular that… It's contentious, or you… we want to discuss?
**Tammy Baylis** 36:49 Yeah, sorry, I mumbled on my words. At the top, for the changelog.added entry, the bot's saying, oh, it should be Request Instrumenter, but it's not just that one, it's… it's multiple.
So, I don't know. Doesn't matter to me, but there should be…
**Aaron Abbott (Google LLC)** 37:07 Yeah.
I feel like we could also just skip changelog on this one, since it's just docs.
**Tammy Baylis** 37:13 Yeah.
**Aaron Abbott (Google LLC)** 37:17 Okay.
**Tammy Baylis** 37:17 Yeah, that was it. Thank you.
**Aaron Abbott (Google LLC)** 37:20 Cool.
Yeah, I can… I think, Riccardo, you already took a look? I don't know if…
**Riccardo Magliocchetti** 37:33 Yeah.
**Aaron Abbott (Google LLC)** 37:35 Yes, okay, so this would be addressed.
Okay.
Cool, looks good to me, I'll probably just approve it right after the call. But, yeah, thanks for raising this one.
Did you want to talk about these two also, Tammy? Or three?
2.
**Tammy Baylis** 37:52 Oh, yeah, just linking the DB opt-in I mentioned, and OTel.io option… er, option.
PR I mentioned, those can be looked at later.
Just some context.
**Aaron Abbott (Google LLC)** 38:06 Okay.
Awesome, next one is you, Dylan, are you around?
**Dylan Russell** 38:15 Yep, I'm here.
This one is just the change to the error message that we… log when… Either in instrumentation, like, isn't… Or, sorry, an instrumentation is installed, but the thing it's instrumenting isn't.
Or the thing it's instrumenting, like the library it's instrumenting, is installed, but it's not, like, the right version.
And then there's, like, the auto-instrumentation path, and the… Just, like, manual instrumentation path.
But it's just making the error message, like, a little better.
is…
**Aaron Abbott (Google LLC)** 39:08 This is what it looks like now, after the change.
**Dylan Russell** 39:12 That's one of… there's, like… yeah, so that's in the case where… Yeah, the installed version is outside the range.
**Aaron Abbott (Google LLC)** 39:22 This one was… Not installed.
**Dylan Russell** 39:26 Alright.
**Aaron Abbott (Google LLC)** 39:27 And… yeah, this looks awesome to me.
Yeah, I think this was smartly needed.
**Dylan Russell** 39:37 Yeah.
**Aaron Abbott (Google LLC)** 39:40 Cool.
Anybody else have some thoughts on this one? I'll probably approve this one after the call, too, looks great.
Alright.
Thanks, Dylan. Emidio Iran?
**Emídio Neto** 40:00 Hey, yeah, Yeah, we have this PR, which is sitting for a long time. It's basically to add a new package.
resource detector that repopulate the host ID attribute.
Right?
Java has a similar one.
And this is particularly useful on comprehensive infrastructure.
Where you have, the same… very same host ID.
For the same machine, so… On Linux, it used, the machine ID to get the… that information.
I don't have the knowledge about, on the windows, and… Request.
And we don't have, means to validate that on the CI. That's the only problem I can see on this PR. But overall, it looks good to me, so I just want to check if anyone is also interested.
In having this… Otherwise I can.
I can maintain as well.
**Aaron Abbott (Google LLC)** 41:09 No, Yeah, if it's in the… if it's in the spec and the implementation looks good, I… sounds great, should do it.
**Emídio Neto** 41:17 Yeah, it's, it's also been type-checked with Bright.
There is a review from Lucas. I'm not sure if he's here, but… Yeah, the only thing is we can't test the windows.
Excepting market now.
**Aaron Abbott (Google LLC)** 41:41 Yeah, I saw there was a comment there about that. Is it not… is it not possible, or is it just, like, not being done yet?
**Emídio Neto** 41:49 For the windows, it's a limitation from our CI. We don't have it right now. We can do.
Okay, do that, though, but we don't have it.
I just thought, like, we can do… Later, if needed, but… Ugh.
I don't think it's a hard blocker.
**Aaron Abbott (Google LLC)** 42:12 Yep, Riccardo?
**Riccardo Magliocchetti** 42:13 Yeah, but question about this, is this something that is also mentioned in the declarative config?
Or this is just, A random resource detector.
**Emídio Neto** 42:29 Marcelli is the… the leader, just a social actor.
Nope.
**Riccardo Magliocchetti** 42:38 Thanks.
**Emídio Neto** 42:40 Yeah, I also suggest the name to be Host80, or the other creator with the name host, but I think it can conflict with the built-in host detector from the SDK.
So I made a suggestion to use Host ID as an embedded package.
**Aaron Abbott (Google LLC)** 43:03 Cool.
Do I need to… should I probably go and reserve this one, then?
I'm not bye-bye.
**Emídio Neto** 43:13 Yeah, if I find out, it would be less.
**Aaron Abbott (Google LLC)** 43:16 It's not a new package, is it? Er… Yes.
**Emídio Neto** 43:19 Yeah, it's on a pec… it's on a package, yeah.
**Aaron Abbott (Google LLC)** 43:22 I can do that, yeah.
**Liudmila Molkova** 43:23 Wait, it shouldn't be the host ID detector, though. The host is the entity, right, and the source.
So the host ID is one required attribute on it, but there are others that describe the host.
**Emídio Neto** 43:37 Yes, exactly.
We set some attributes on the building close to the technical SDK, but this one is a different package.
Just for the ID. The similar way we do for the container ID.
**Liudmila Molkova** 43:51 Oh, wait, so we should have… The whole, like, the resources, this is the way that works now.
the… Next thing that will finally stabilize at some point is entities, and you… the whole entity should be one package, like the host entity, or the process, or container.
And… it… it sh… the ID is the thing called identifying attribute. It's the most important one on the host, the other are descriptive. But they come together, they don't come in different instrumentations, usually. Like, they shouldn't.
It's like… Go ahead.
**Emídio Neto** 44:37 I just think that you should concentrate everything on a reserve detector host.
**Liudmila Molkova** 44:44 Yeah, why not?
**Emídio Neto** 44:51 So, Israel may not need a new package.
We can leave it this on SDK.
**Liudmila Molkova** 45:01 That would be… my first thought, but for some reason you created a new package, and I'm curious what were the reasons.
**Emídio Neto** 45:11 it's because, the pattern… we're following the other languages. Like, in Java, it's a… We'll use a separate package.
**Liudmila Molkova** 45:23 It's a… oh, interesting.
Do you have a link?
**Emídio Neto** 45:28 Yeah, I can send it.
**Liudmila Molkova** 45:30 Yeah, dear.
**Emídio Neto** 45:31 I don't have it right now, but they're considering.
**Liudmila Molkova** 45:35 Cool. Oh, I can find it if you don't have it right now, no worries. I'll track things.
**Emídio Neto** 45:44 Right, yeah. If you can leave a comment, it would be nice as well, about that, stabilization you mentioned, the… about the entities.
**Liudmila Molkova** 45:54 So… the… entities… There, I don't think you folks have NTGC… the ATTS API and SDK are… I don't remember the status of the pages in the spec. It's just a long-term goal.
But even for resources, like.
I believe it's common to group a lot of things about the same resource into one package.
I'll check on Java, indeed, I… I… I don't know why they would split it, but it's… it's a good… Input.
And it's, like, it would be easier for us to maintain one package rate.
**Emídio Neto** 46:45 Yes, yeah. Not having a package for each attribute, but yeah.
**Liudmila Molkova** 46:54 Yeah, so let's check on this.
Thank you.
**Emídio Neto** 46:58 Alright, thank you.
**Aaron Abbott (Google LLC)** 47:03 Cool, yeah, and once we have, like, a decision Emidio, please reach out to me on Slack if we're ready to reserve, or I could just go and do it right now, but… Yeah.
**Emídio Neto** 47:13 Yeah, yeah, thank you.
**Aaron Abbott (Google LLC)** 47:16 Okay, cool, and last one's also you?
**Emídio Neto** 47:20 Yeah,
**Aaron Abbott (Google LLC)** 47:21 issue.
**Emídio Neto** 47:22 I was reviewing this PR.
It basically fix… A bug, for synchronous instruments, like, like a gouge.
When you call gouge.set, And the telemetry is exported.
When you cock in.
you don't get the value, you get none. So, this is not respecting the cumulative temporality, basically.
And that this PR is fixing that behavior.
I left a comment on Swisscardo a bit.
Explaining? Yeah.
**Aaron Abbott (Google LLC)** 48:09 This one?
**Emídio Neto** 48:10 Yeah.
This is mostly, behavior change.
Like, it's not changing the public APIs or something.
just internal, class, but, it's a behavior change, like… Yeah, use it, at least my understanding, this whole time it was that… After the… if the value doesn't change during the export for gouge, for example.
we won't get, like, the cumulative value. But, I was wrong, and the specification says the… Says that. So I think it's something we should fix.
**Aaron Abbott (Google LLC)** 48:54 Interesting. Does the specification say that for gauge, specifically? Because I think Gage is not… doesn't really have temporality, right? I think it's actually not even in the Protobus, if I remember correctly.
**Emídio Neto** 49:07 Not specifically for gate touch, but, for synchronous instruments.
Yeah, and we are using the… for… For gouge, and… yeah, mainly for gouge, we are using less valve aggregation.
**Aaron Abbott (Google LLC)** 49:26 Right.
**Emídio Neto** 49:27 Yeah, yeah, but this is not related to the aggregation itself, but mostly to the instrument.
**Aaron Abbott (Google LLC)** 49:33 Okay, I mean, it makes sense, but I don't know if… I don't know if the temporality matters for it.
per gauge, but I… I can… I mean, you said the spec matrix, is it… Certain entry for that format.
Yeah, maybe I can look over the… the bugs, but I'm… I don't know, I'm… Is it called out explicitly in the spec, or is this kind of up to interpretation?
**Emídio Neto** 50:03 is very explicit, and I never saw that, but yeah, if you open, it says exactly what you have on the description.
**Aaron Abbott (Google LLC)** 50:14 This one?
**Emídio Neto** 50:16 Yeah.
**Aaron Abbott (Google LLC)** 50:17 Okay.
**Emídio Neto** 50:23 Scroll down a bit… Yet, there's… no, next, next one.
**Aaron Abbott (Google LLC)** 50:30 Sorry.
**Emídio Neto** 50:32 Yeah.
the… The much greater selection, ta-da-da!
load up.
the one, before.
**Aaron Abbott (Google LLC)** 50:45 Okay.
**Emídio Neto** 50:46 Yeah, okay.
**Aaron Abbott (Google LLC)** 50:48 So I'm seeing the image of… Apply to all metrics, not just those who include aggregation, temporality. Okay, I see this part.
**Emídio Neto** 51:01 Yep.
**Aaron Abbott (Google LLC)** 51:03 Okay.
Cool. Yeah, sounds good. Thanks for raising this one. It sounds like a bug to me as well.
**Emídio Neto** 51:13 Fair enough.
**Aaron Abbott (Google LLC)** 51:16 Cool, looks like Leighton already approved also, so maybe we can… This one along.
**Emídio Neto** 51:21 Unless…
**Aaron Abbott (Google LLC)** 51:25 Alright, I think that was the end of the agenda.
Oops.
Unless anybody else had something else, we can get about 9 minutes back.
**Liudmila Molkova** 51:36 Medio, can you quickly answer my chat question before we park our ways? Is it the one that you referred to?
**Emídio Neto** 51:47 I have to check. I'm not the owner of the PR, but
**Liudmila Molkova** 51:51 Okay, yeah, no worries.
**Emídio Neto** 51:53 We're also using Slack, yeah.
**Liudmila Molkova** 51:56 Okay, cool. Thank you.
**Emídio Neto** 51:58 Cute.
**Aaron Abbott (Google LLC)** 52:02 Alright, later everyone.
**Liudmila Molkova** 52:05 Bye.
**Leighton** 52:06 Thanks, guys.
**Diego Hurtado (Dash0)** 52:08 by all…
