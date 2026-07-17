SIG: Python SIG
Date: 2026-07-16
Duration: 56 minutes
============================================================

## Zoom Recording Transcript

**Riccardo Magliocchetti** 00:09 Hello.
**shuwpan** 00:14 Oh, boy.
**Riccardo Magliocchetti** 01:48 I think we are in the wrong meeting.
Because, like, we updated the… Plot 4.
And I think this is not the right one.
Or maybe it's the correct one.
Like, now the URL should be, like, Zoom LFX… something, and I don't see it in this one.
Yep.
**Lukas** 02:37 Do you do you have the.
**Riccardo Magliocchetti** 02:40 Yeah, the… into the notes.
And I shared it in the chat here.
**Lukas** 02:54 Yeah, for some reason, my Google Calendar didn't update.
**Riccardo Magliocchetti** 03:00 Okay.
**Lukas** 03:01 Yeah, okay.
**Riccardo Magliocchetti** 03:02 See you on the other side.
**diego** 05:24 Hello.
**Riccardo Magliocchetti** 05:25 Hello. Like, at least this one works.
**Tammy Baylis** 05:29 Thank you, Ricardo.
**Riccardo Magliocchetti** 05:33 Because, like, I joined this one because I have the bookmark on my browser.
And I forgot what it was changed.
No.
Okay, may fix the other one, but… I guess we can just use this one for this week.
I think we are split between… okay, Anna.
What do you want to see?
**Leighton Chen** 07:03 Hey, everyone.
**Riccardo Magliocchetti** 07:05 Okay.
**diego** 07:10 P.
**Riccardo Magliocchetti** 07:31 Let me share… Tammy, do you want to do the triage?
**Tammy Baylis** 07:55 Yeah, I'll start with that. Thank you. Situating myself.
Right.
**Riccardo Magliocchetti** 08:07 And welcome everyone to this week's Python SQL.
**Tammy Baylis** 08:11 Yes.
**Riccardo Magliocchetti** 08:12 Sorry for the… The troubles for… with those new links.
We'll sort it out.
Sorry. Tell me. Go ahead, please. Thanks.
**Tammy Baylis** 08:23 Yeah, thank you. I'll go till 9 15 for today. This is our Triage board, No status, ignore chores and builds, but we'll look at… Handle encoding exceptions in OTLP exporters.
June 10th… There's been some review already.
Okay, we are holding on this Pr. For now.
So I'll keep it in no status.
Next, fix metrics, convert list attribute values to tuples for aggregation key.
Yes.
open for now.
Right. Okay. So I believe this Pr. Has dependency.
Okay.
on this one which has been approved. So I'll keep this in no status for now.
and it'll either get marked as stale or marked as closed automatically.
or OP can come back to it if this one doesn't get merged.
Another fix, fast API preserve.
Hotel context from sync route handlers to background tasks.
a linked issue, which is great from last year.
probably still relevant, or Aaron commented.
**Riccardo Magliocchetti** 10:38 Fellowship of it include X.
On this one, since he maintains… So you come to contributor to the past. Yes.
**Tammy Baylis** 10:47 Yeah, sounds good.
**Riccardo Magliocchetti** 10:50 Yeah, it goes back.
**Tammy Baylis** 10:58 We'll keep the issue in no status as well until we Get an answer for that.
Feature for Kafka… Add message in Kafka cluster id to spans.
Oh, nice to add.
these… And this is in the Semcarf.
Believe.
what was it called messaging Kafka cluster Id.
Yeah.
in development.
seems legit.
Yeah, I'd say this is ready.
Nice.
Fix support sequence metric attributes and view aggregation keys.
From 2 years ago, 2024 was 2 years ago.
Mmhm.
So well described issue.
Okay, so GRV has decided to Take a crack at it. Always welcome.
Oh.
Does this Pr address this already?
We were just looking at this.
Okay, we've got a trail now.
Thanks for contributing. Going to keep this in no status for now, while the other 2 Prs get sorted.
Docs clarify view aggregation precedence.
document the spec behavior if we haven't already.
Okay, this is being reviewed already. So it's ready.
Okay, it's 9 15. We'll stop there.
And I'll pass it back to you, Ricardo. Thanks, everyone.
**Riccardo Magliocchetti** 14:22 Thank you, Tom.
Okay… well, the other is topic because I made you find out what.
We forgot to update, the little script we used to build, And publish the packages, and so we missed the build, publication of the… OpenTelemetry Config, I think it's called, like, the one that is used, But contains the declarative config, Implementation, so I'm taking a look if we can run the script.
Or else we need to bump.
And do a new patch release.
Diego?
**diego** 15:18 Yeah, I was just going to ask you if you could make a release.
With that, it's an important feature for us.
**Riccardo Magliocchetti** 15:30 Yep.
I'm trying to fix this one since there will be no changes to the code.
But, yeah.
Let's see.
Again, sorry for the trouble, but we missed this one.
Well, Hugo, you're next.
**diego** 15:53 Right, okay, so… We discussed this last week about a proposal for new process to submit PRs.
A couple of, Points the people mentioned was that, it will be… Important, also.
To have a mechanism to unassign issues.
Oh, maybe I should… give a little summary first. So, I'm proposing here, a new… process.
To submit PRs, which involves first submitting an issue.
Discussing the… What's, what do they want to do there? And then they get Whoever wants to work on that issue, they get assigned to that issue, and… Only the person who gets assigned to that issue can open a PR.
if this process is not followed, if someone opens a PR just like that.
that PR gets automatically closed. Something that was mentioned in the previous meeting was that we would also need Something that will… Unassigned people, if no progress is made in… There are sign issues.
Certain amount of time so that other people can take their work.
And you're saying that, some people mentioned was that, for… certain, situations.
There is, it's sometimes necessary to open a PR without an issue for.
Urgent things or something like that. So.
I updated the GitHub action including this PR to support both scenarios in the second case.
People who… Pretty much approvers and maintainers can add a tag, a label, sorry.
That says, do not close this PR.
So that the action gets ignored.
Yeah, there's something I wanted to share with you, so if I may share my screen.
Thank you.
So… I made this chart. Everyone can see my screen.
**Tammy Baylis** 18:29 No, not yet.
**diego** 18:32 Nope.
No?
**Tammy Baylis** 18:37 Yes, thank you.
**diego** 18:39 Right, so, from the beginning of time, Until today, this is our… chart, With pull requests, so the yellow line is cumulative.
The blue line is… The ones that get open, remain open, right? So… So far, we have had, like, just… 3,001 PRs opened.
And I wanted you to take a look at this.
So, here it is, January 2026, just, Right there, or maybe a few everywhere.
There is a spike, you can see how the The slope of this, curve.
Who's higher?
So, I checked this out, and this is roughly a 3… Three-fold increase.
in… In PR, in the rate of PRs that are being opened, right? So.
This definitely looks like, We're also getting… More PRs, probably AI generated.
I just want to point out that This can continue, right?
this rate, or… increase, I don't know, but, we're definitely getting more PRs than before. It's a three-fold increase, so… And then… So, yeah, I do think, let me just stop sharing… That, This is important.
to, safeguard the sanity of… The approver of maintainer teams.
So, so yeah.
That's what I wanted to show you guys today.
Anyone?
Something to say?
**Riccardo Magliocchetti** 21:07 I think the notes with the color nails.
And… Yeah, like we feel the increased number for sure.
Okay.
But, yeah, like, yeah, me, like, personally, I haven't done it.
Time to spend thinking on this this week.
And so, like, I don't have, nothing to… Continue with the discussion.
Anyone else?
**Lukas** 21:47 I would say I'm Mostly in favor.
of what Diego's put forward. I don't have anything else to add, really.
**Riccardo Magliocchetti** 22:19 Okay, any other comment?
Okay, so next one.
It's also from you, Diego.
**diego** 22:39 Right, yeah, this is just a request.
To get, hopefully another approval.
For this PR, we're pretty close. This is a very cool feature. Thank you, Lucas, for implementing this. Early reviewed and gave a symbolic.
Great check approval.
But it has one green check already. So if we could get this merged, it will definitely help.
With, The situations were… We… We're proud of Office, It's an issue, right? It's a dependency.
Yeah, so… If we could get more around this.
Awesome.
**Leighton Chen** 23:28 Yeah, I'm taking a look at this today.
**diego** 23:30 Thank you, Layden.
**Riccardo Magliocchetti** 23:39 What's that?
Next one is from Carlos.
**carlosalberto** 23:47 Yeah, this is just like a pair of PRs first, and then I forgot to add the last one, but this one probably can close. This is for implementing their environment propagator, and instead of this.
like support to carriers through a sorry carriers through a gather was implemented.
This was also like having a specific propagator for this was mostly discarded, the specification, so probably can be closed, you know.
I would say, not probably like most likely.
**Riccardo Magliocchetti** 24:24 Okay, thanks.
Yeah, I guess we can close this.
Thank you. Okay.
But it doesn't come.
Thanks.
Okay, I'll, read the duration and close it.
Let me do it.
Thank you.
Then, back to Diego.
No protobuf?
**diego** 24:49 Yeah.
Okay, so… we at Dash Zero have been working on… Implementing, No DLP exporter that doesn't use, protobuf. The reason why it's, painfully… known to everybody here. Python only supports, One, two… Dependency per virtual environment, so… Same thing, same problem that we have had a bootstrap and probably some instrumentations as well, right, where The application code has, A dependency A… Version X, and then… Our libraries, try to use dependency A version Y and there can be conflicts, right? So, protograph is a very popular Library, so it's, quite likely that, Application code, we'll be using it. So, here in this branch, we have implemented The exporter… for HTTP.
So that it doesn't use… Protobuf, which means, we implemented, Protobuf ourselves.
Python, and we made sure that it's byte by byte.
Byte for byte, Equivalent, right? Something else, something that's also important to notice here is that, This exporter also had requests as a dependency, and requests are very popular, right? So, This exporter also replaces requests with your lib.
It's not perfectly compatible, because actually, our SDK… Specifically says, and I'm not sure that's right, but it specifically says that.
We will use a request subject.
So… So, yeah, we cannot shake that, now… Anyways, I just wanted to show you this, this approach, I just came from another call.
Injector Cole, Jack Berg, You know, Jack, from Java was there. He told us that, that this, approach of implementing Python themselves is also something that they do in Java.
So… Nothing new here. Now, the, it is true that, in very simple terms, Java is faster than Python, and, we may need to implement this Not in Python, but in… I don't know, C, ROS, or something, but that's also a possibility. The main thing here is, getting saving ourselves from the product dependency. So I wanted to show you this. It'll be ideal, I guess, if we could introduce this.
And, as a solution for the exporter that we have right now, And remove the protobuf dependency.
So yeah, your thoughts?
please.
**Riccardo Magliocchetti** 28:45 Well, I think that the Lucas.
As opinion and he did the same, I guess.
Like you proposed the same and export using the Rust implementation of automatic.
And that's a thing.
Lucas, you worked on… Abstracting the HTTP export, backends.
What was it, something else?
**Lukas** 29:10 Yeah, so we should, Yeah, so Diego mentioned that the constructor for the HTTP exporter accepts a request object. But I actually have a PR open that — We'll change the implementation to use URL lib3 if… But only if the user does not pass in a request object. So that shouldn't be a breaking change.
I'm.
**diego** 29:38 Question Lucas is URL three also a third party library? Wouldn't we end up?
**Lukas** 29:43 Yeah, it is, but at least the, at least the version range that it's using is like, basically covers every single version. So you basically have your very low chance of like, having a version collision, but you could even switch out for like a pure or pure URL implementation if you wanted.
With…
**diego** 30:08 Right.
**Lukas** 30:08 Yeah.
I'm not sure, like, how relevant that is, but… I'm… I guess, yeah, one comment looking at that branch. I see you have a gRPC one, but that uses… I don't know if, like, you were planning on addressing it for gRPC, but I see gRPC IO is in there, which is another kind of toxic dependency.
**diego** 30:32 Right.
Yeah, that's… that's a next step for us, to also take care of your VC.
**Lukas** 30:40 Yeah, personally, like my view on this, like the easiest way in my eyes, I like, I guess the other concern with writing it in Python is probably mostly performance.
**diego** 30:51 So.
**Lukas** 30:52 So like what I thought, or yeah, one thought is to like kind of extend the whole Rust.
base exporter thing, and you could just bake in both gRPC and HTTP exporters directly in that.
**diego** 31:06 Yeah, I, yeah, I have definitely, considered that, At some point, I mean, we need to think about performance and probably Rust.
It's a… it's a… it's a good carrier, right, to help us.
**Lukas** 31:26 Plus, yeah, the effort there would probably lower though, even because you could just use existing. There's already like Rust native implementations for protobuf, like Prost.
**diego** 31:36 No.
Okay, cool.
**Lukas** 31:38 But I think, Yeah, I would be fine, like, if we want to, like, host a contrib package or something for this.
I guess we just don't want to make it, like, super confusing for users having a bunch of different options to choose from for exporters.
Right? Hmm.
And I'm not sure, I guess, like, we could also maybe discuss, like, Performing a V2 release?
and… and switching… he… are gRPC and Protobuf.
Dependencies.
I don't know, there's a lot of options here, and I don't really know, like, what the best one is, but…
**diego** 32:21 Yeah, but it's a great way of starting this conversation, I think.
**Lukas** 32:25 Yeah, the other thing is, like, if you are going with a pure Python approach, I'm not sure, did you use a… you could write a ProtoC plugin to do the code generation, I'm not sure if you did that, but that would be a little more reasonable in my mind.
**diego** 32:40 No, this is really raw Python in the sense that we're making the bytes ourselves. But again.
It's not like we want a Python implementation. What we want is to get rid of the dependency, right? And there's probably better ways to implement this that are more performant than Python.
This is a first step.
**Lukas** 33:07 Yeah, and I think last point.
one thing I mentioned… another way to get around this, actually, is just to vendor the entire Protobuf package, just so we can make a distribution that just… includes it.
Okay.
**diego** 33:21 Yeah. So.
**Lukas** 33:22 install, you can have whatever else you want installed, and it'll still function correctly. But yeah, it's… I mean, vendoring is a pretty frowned upon thing in the Python ecosystem, so… but that would effectively solve the same issue.
**diego** 33:37 Yeah, we considered several approaches. Vendoring was one of them.
I was also thinking about… I don't know if you remember this conversation about, having a separate process and make, Make an inter-process communication for the… product bytes, and so on.
So yeah, this approach has proven feasible.
So we'll definitely explore.
better implementations that are more performant, right?
And definitely, again, Rust is a very strong candidate here.
**Riccardo Magliocchetti** 34:20 I'm a guest vendoring, because it would be, like, probably painful if we need to handle security issues.
**diego** 34:30 Yeah, and also, I don't know how feasible it is, because the import paths in the vendor package will need to…
**Riccardo Magliocchetti** 34:42 Oh, we probably just rename the name of the modules. Yeah.
**diego** 34:45 Yeah, so… We also need to… Deal with that. Anyways.
Yeah, I just wanted to present this to you, get your opinions.
Thank you for that.
Oh.
**Riccardo Magliocchetti** 35:07 Yeah, thanks.
Can I do that, Coleman?
Nope. And then next is Lucas.
Okay, expecting bias.
**Lukas** 35:26 Yeah, this is a small one, but I have this PR open just to update the spec compliance for Python.
And if you scroll down on this discussion, there is a discussion about whether we should mark things that are internally implemented as, like.
as us implementing the spec.
And I guess the consensus… the consensus was… was no, that we shouldn't… so, like, for example, this, yeah, spam processor on ending is a developmental thing.
That we have implemented, but it is private.
So, we're gonna leave that as unmarked, so… This kind of brings up a question, though, like… How do we expect users to be able to play with experimental functionality?
If like, it's private like this, right? So, like, I guess… so the… the issue I want to avoid is that If we can never mark it as implemented in the spec compliance matrix, then… you know, we can never get to stable, right? If… if, like, we need, like, a certain number of language implementations to actually implement it for it to go stable, so… I'm not sure if I'm kind of articulating the point correctly, but… Just kind of curious what… People's thoughts are like.
**diego** 37:00 The version, it's how they do this, right? People install a version that says beta or development or something, right?
**Lukas** 37:09 I guess, yeah, the issue is, though, is that a lot of these developmental stuff is in the SDK, which is already stable. So, like, we can't spin it off into its own package, necessarily.
So, like, the traditional, like, semcom versioning semantics kind of break down here.
**diego** 37:29 Sorry, what, what?
What do you mean? We can make a branch?
And make a release.
We can make a branch where we.
Make those things public and make a release.
Named… Beta, right? So that's how it gets exposed.
**Riccardo Magliocchetti** 38:04 Hey, Tom.
**diego** 38:04 It's.
**Leighton Chen** 38:08 Lucas, is your question more about discovery?
or, like, I might have missed that part.
**Lukas** 38:19 It's more of like, so for example, this span processor on ending function is developmental, so it may break.
So currently we have it, you know, it's prefixed with the underscore to mark as private on the span processor.
But… I'm just trying to think, like, is there any way we could better expose this to users without making it internal? Because technically, like, the convention is that, you know, users should not be relying on internal… functions, right, or… So even though we have implemented this developmental functionality, there really isn't a proper way for users to use it, right?
If that… am I kind of making sense here? I mean, you can obviously go ahead… Go ahead and do it, but, like… It's, yeah, it's not the best user experience.
**diego** 39:18 Yeah, well.
**Leighton Chen** 39:19 Right, right.
**diego** 39:19 That's how release versions work, right? You remove the underscore. You create a branch.
Remove the underscores there, and make a release from the branch.
That says this is a beta version.
And people install the beta version, and then… and they get public things.
**Lukas** 39:40 Okay, so do we… so you're suggesting that we have two different, like, SDKs published? Like, one that is a beta?
Okay.
**diego** 39:47 Yeah, exactly. I think that's what other packages do as well. I don't think this is… This is new.
Oh.
**Leighton Chen** 39:56 Hey, Lucas, how does this differ from, like, us using, like, incubating semantic attributes? Is this, like, similar?
**Lukas** 40:03 Yeah, it's the same Like, that's kind of… yeah, with the private… Accesses.
**Leighton Chen** 40:12 proceed.
**Lukas** 40:13 See, there's other, I guess, I don't know who raised their hand first, Ricardo or Carlos, but.
**Riccardo Magliocchetti** 40:20 I have a question, and my question is, like, Do you think that this This is only about discovery.
Maybe just… Proposing under a symbol to use in this matrix that says we have a prototype will be enough.
**Lukas** 40:41 Yeah, that's another option.
And.
So maybe, yeah, maybe that's just the answer.
**Riccardo Magliocchetti** 40:49 Carlos?
**carlosalberto** 40:52 Yeah, I'm trying to look for that in the specification, but long story short, the idea is that you can choose as a SIG any way to expose this, but basically the user has to be able to fetch that functionality. And for example, the way how configuration was exposed, or it is still exposed, because I don't know whether Mike MyXPR has been merged. It's like, you export the SDK, and then you do something extra, so you can go as an user and try that.
understanding that this is an experimental thing. And I could suggest that maintainers review what's the general approach to that, because I don't think there's even general agreement on this point.
I think that what you were doing with the declarative configuration support was a very acceptable thing. Alternatives that other languages have done in the past, like, for example, Java, they actually have child classes.
or, for example, tracer provider.
which actually have that experimental part, and they are coming as child classes in a separate package.
That's, however, very problematic, you know, when it comes to deploying, for some people at least. But anyway, there's no perfect solution, but the idea is that you have something that is super clear when it comes to the fact that it's experimental, and users can test that out, because that's the thing. It's like, we don't want us like, hotel people to try it out, but also we want… it's more like users have to be able to try it out themselves.
**diego** 42:27 Yeah, actually, sorry, now that I think about it, I think using… This underscores it's a bad approach.
I think what we should do… When we want to introduce a test, a feature like that, is to have a separate branch named development, right, where we're developing that.
And, make releases, better releases out of that branch.
And then when that's, consider stable, we merge the branching domain Because, what we're doing here is we are introducing a bunch of private stuff into Maine.
And there's really no… No point in doing that, it's like, because we're not.
We're adding stuff in our release packages that's not yet supposed to be used by By users, right? So… It'll be much cleaner to just keep it in a separate branch.
And then merge.
So we never get… Stuff in the release.
Packages, that's not supposed to be… used.
by our end users.
**Riccardo Magliocchetti** 43:56 Maintaining different branches for every experimental stuff would be like.
Painful for us, like, we don't have enough resources to maintain, like we do right now.
But, and like, my point of view is this, like, as Carlos said, like, we don't have a perfect solution with a trade-off.
And the trade-off here is that, you want to try experimental stuff, you must be aware, but you may break.
Because it's private, so we don't guarantee anything, any compatibility.
And, like, given that we are not probably, like, the… The fastest sig in implementing experimental stuff.
I don't think we, like, a lot of people rely on us on implementing stuff, forgetting what I invented.
Then made stable, so.
**diego** 44:52 we don't need multiple branches, we only need one for development. We can… Put everything that's under development there.
**Riccardo Magliocchetti** 45:02 Yeah, but like, how will we handle, like, dependencies?
We, we know what dependencies of the very same version of, A name, like… Of, you know.
We have, like, version 1.44, depends on something else, 1.44.
Of us.
Of a specific version and a specific name.
If we have another… Branch, where we release stuff.
Like, we have to… Like.
Also keep track of this.
**diego** 45:47 Yeah, what I mean is that the second branch, the development branch, Releases everything as beta.
We don't mix them up, so we have… completely different packages, right? So there is no depend… no dependency.
Conflicts, because the… The packages in the main branch.
depend on the normal release packages, and the packages in the beta branch all use the beta versions, right? So… Anyways, we can discuss this offline.
Just want…
**Riccardo Magliocchetti** 46:28 Right.
**Lukas** 46:32 I think for now I can, I can just, maybe we can think of adding another, like, entry marker for, like.
The spec compliance matrix, like you recommended, Ricardo?
**Riccardo Magliocchetti** 46:46 But Carlos could have an answer.
**carlosalberto** 46:49 By the way, what was the problem with declarative configuration, the way it was exposed? Like, a user had to actually go and grab something.
Maybe it wouldn't work for everything, but for some things it may. Like, for new components, you can just keep them under, like, a separate package or something, like, experimental, like, yeah.
or, for example, let's say, for for the unending method is that you just create child class… of the spam processor, like, expanded the spam processor, and it's the SDK that we are releasing, but it's under, experimental package which may be hidden but once you get that the method is public.
and all that.
Was there a problem with that approach, with declarative configuration as a preview?
**Leighton Chen** 47:40 Carlos, did you, did you mean a separate, like, module or folder, or do you mean.
**carlosalberto** 47:45 Yeah.
**Leighton Chen** 47:46 Yeah, it's a…
**carlosalberto** 47:48 Yes.
Like, separate submodule.
**Leighton Chen** 47:54 Right.
**carlosalberto** 48:00 It's possible. : Yeah, I just wanted to ask in case, you know, like in case somebody knows, we don't have to discuss that here. I agree with the media that we we have, and with Diego we have to open anyway, and an issue.
and disclose that.
But yeah, there are a few options and nothing is perfect.
But maintainers will have to choose what's the perfect trade off.
**Riccardo Magliocchetti** 48:30 All right, let's open discussion.
Well, Carlos, you're.
**carlosalberto** 48:37 Well yeah just like last eyes on this PR it's a it's actually a very simple thing from specification but of course it requires some details to be fixed from the maintainer side in case you know I'm not that familiar with the code base.
anymore but I think that the last issue there is from the fact that whether the fact that I am not exposing or adding this always record sampler to the list of known samplers and I realized that not only, this is not covered in the declarative config specification, but also it's not even covered in the environment variable section. So we don't have to do that part now. As you may know.
We are not updating environment variables.
We haven't been able to do that for some time now unless there's a strong reason. Yeah but anyway either way I can drive that part from the specification. Otherwise I think it's ready to go. There are some minor details including the naming like whether I should include the sampler suffix there or not because for example parent base I think it's only parent base not parent base sampler. So minor details so please take a look.
That's all from Messiah.
**diego** 49:54 Yeah, also, I think I already approved. Thank you for… Getting this done, Carlos.
**Riccardo Magliocchetti** 50:03 Yeah, like Mali issue is that.
If, like, if we don't add it to the, you know, samples dict.
I'm not sure we are able to use it without instrumentation, and so you can only set up this with a manual instrumentation.
And the other thing is that.
This is like, if we don't do this now, I think we'll forget about that. We'll never address.
**carlosalberto** 50:29 Oh, yeah, actually, probably makes sense to have an issue for the specification first, and then I will link this PR to that place so we don't forget, you know, something like that. It's a good call, yeah. Otherwise, yes.
There are so many things happening, and I may forget myself about that. So maybe let's call that. I will create an issue in the specification.
First… Because this has to be done anyway. And then we can, once that is not done, but accepted as an issue in the specification, we can decide whether this is good to go. Yeah, let's do that. In the meantime, as maintainers or approvers, please take a look at the minor details.
**Lukas** 51:16 Sorry if I missed it. Why can't we just add an entry point?
Then it can be used as auto instrumentation, right?
**Riccardo Magliocchetti** 51:29 Yeah, but it takes a parameter.
It's, it takes in, it's required to pass an argument, another sampler as a parent sampler.
**Lukas** 51:43 Oh, right, right.
**Riccardo Magliocchetti** 51:44 So we need the environment handling as well.
At least for a minute.
**Lukas** 51:51 Yeah, it makes sense.
**Riccardo Magliocchetti** 52:04 Okay, this was the last topic for today.
Hey!
You don't have anyone… anything else?
Thanks, everyone.
Bye bye.
**Leighton Chen** 52:18 Thanks, everyone.
**Riccardo Magliocchetti** 52:19 Thanks.
