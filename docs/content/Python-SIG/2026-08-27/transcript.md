SIG: Python SIG
Date: 2026-08-27
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Riccardo Magliocchetti** 00:52 Hey, Tammy.
**Tammy Baylis** 00:59 Hey, Riccardo, how you doing?
**Riccardo Magliocchetti** 01:02 I'm doing good. How are you doing?
**Tammy Baylis** 01:05 I'm okay. August… August ended up being very busy for me.
Yeah, got sick, got better, just so much to catch up on.
That's weird, it's just us, too, and it's…
**Riccardo Magliocchetti** 01:26 Yeah.
**Tammy Baylis** 01:27 Two minutes in.
**Riccardo Magliocchetti** 01:31 Or maybe the… annoyed in the U.S?
**Tammy Baylis** 01:39 Yeah, I don't know. I guess it is the time of year when families usually Like, finish all their holiday stuff before people go back to school.
**Riccardo Magliocchetti** 01:51 Oh, yeah.
Maybe.
**Tammy Baylis** 01:59 Hey, Dylan, good to see you.
**Dylan Russell** 02:02 Hello.
**Riccardo Magliocchetti** 02:37 Yeah, so, like, welcome everyone to this… Weak, by the Sicor.
Please add yourself as an attendee, and if you want to discuss something, also, Please add any topic.
Because at the moment, we are… Empty?
Okay, one topping's coming, maybe?
**Carlos Alberto Cortez** 03:02 By the way, Anne, do you actually check the pull request dashboard?
That is automated.
like, did you check that usually in this call? I know that it was added probably two weeks ago, so I was wondering about that, because I think it could be useful to go and check that one.
If there's time.
**Riccardo Magliocchetti** 03:24 What do you mean, like, we have it… Since a couple of weeks.
And it's working fine, yes.
Like, do you mean, like, when we… Like, go…
**Carlos Alberto Cortez** 03:38 Yeah, correct. Go over the report, you know?
**Riccardo Magliocchetti** 03:41 Okay.
Yeah, but, yeah, but… Let me check.
We have plenty of stuff and wet dishes.
But let me… let me add it to the… Since the links are the same.
**Carlos Alberto Cortez** 03:57 I mean, yeah, especially that this week, there are not probably many topics to discuss, even if we're trying… by the way, I apologize, I am in a cafe, but there's some renovation in my flat, etc. Not my own flat, like, neighbor. So, let me know if it gets too noisy, by the way.
**Riccardo Magliocchetti** 04:15 I can't hear anyone.
Noise.
**Tammy Baylis** 04:20 Yeah, seems to cancel okay so far.
**Carlos Alberto Cortez** 04:25 Sweet.
**Riccardo Magliocchetti** 04:31 Okay, it's a 5, the time we start, usually. So, welcome again.
So please add yourself as an attendee, and feel free to add any… Topic you want to discuss?
Tammy, you want to do the triage?
**Tammy Baylis** 04:49 Yeah, sure, switch things up… Share my board window.
Yeah, we'll do 5 minutes, and… actually, I haven't really looked at this… PR dashboard before, but maybe… Maybe next time I can incorporate that into this, this 5-minute period, or… Maybe we'll have a look at this very quickly first, so… This is from the automation of the dashboard, and it gives… Gives a nice… summary of each PR.
Waiting on maintainers, waiting on reviewers.
Waiting on authors… That's cool. I, I wanna, on my own time later, I'm gonna compare this… With this method, and see if there's, like, a more effective way.
Any, any other opinions welcome.
This one I have open here… That's kind of disturbing. Samplers never receive the parent's trace state. This is the linked issue.
Yeah, what steps to reproduce… Anyway, this is the PR.
Link to the issue, that's fine.
We've had some reviews on him already.
That's just for the tests, but there are some things they should do.
I'll put this in need as fixes.
**Riccardo Magliocchetti** 06:41 Like, this is… Like, this user opened a series of, like, 10 issues and opened it at the same time, 10 PRs.
**Tammy Baylis** 06:52 Oh…
**Riccardo Magliocchetti** 06:53 I think it's a lot of automation involved.
But, yeah, like… I would like, like, to see if… Someone will take a look at the reviews, or this is just, like, Vitaly and… They won't care about.
**Dylan Russell** 07:13 I did look at a few of the ones they opened.
That were related to my, like, attributes stuff that I just submitted, and they looked pretty good.
And I, like, approved a few of them.
So they're using… whatever they're using, whatever model, I think is pretty good.
But I didn't look at the trace parent one.
**Tammy Baylis** 07:42 Exciting.
**Riccardo Magliocchetti** 07:44 Like, I think the issues are… are real.
I'm not sure if… The user will take a look at the comments or not.
**Dylan Russell** 07:54 Hmm…
**Riccardo Magliocchetti** 07:55 So, like, if the PI is fine, it's fine to approve a merge, but… We'll see.
**Tammy Baylis** 08:03 Okay… Thanks for that call-out, Yeah, well… well, let's see if they respond to the comments, because it does need a couple… at least small fixes for now.
Okay, wait, sorry, so… This next one is this… AWS Lambda 1, longer provider support with force flush for Lambda freeze handling.
This is an older PR.
And… there's no issue.
Hmm… Let's see… Oh, they've been, adding us individually.
I wonder… I guess it makes sense… It would be nice if there's an issue, but, it's just a small…
**Lukas Hering** 09:22 I haven't taken a look at this. I guess I didn't approve it. I can take a look again.
Yeah, this is, this is valid, this is needed.
**Tammy Baylis** 09:31 Okay.
Thank you. Lukas, is it okay if I add you on this VR, just to…
**Lukas Hering** 09:39 Yep.
**Tammy Baylis** 09:39 Or… okay.
Oh, I forgot your username.
**Lukas Hering** 09:47 H-E-R… just type in H-E-R-I-N.
**Tammy Baylis** 09:50 Thank you. Sorry, it's been a… it's been a month.
Cool.
Let's call it at that today.
And yeah, I'll take a look at the request dashboard for next week. Thank you. Back to you, Riccardo.
**Riccardo Magliocchetti** 10:14 Thank you.
Okay.
First topic from Dylan, about the bird rock.
Can I ask the one question.
**Dylan Russell** 10:25 Yeah, so I've… Started porting over this to the GenAI repo.
And… the plan is to, once we, like, reach parity in the other repo, and I think there's, like, just 4 methods that… Our monkey patched.
Once we get that done, then… basically do what is said here. So add, like, a deprecation warning, And… Potentially add this logic to, like, disable.
the contrib bedrock repo.
I'm not sure if that's really necessary or not, but… And then, yeah, just, like, update the README to, like, point at the other instrumentation.
I think that's it. I don't know if there's any way to, like, officially deprecate something on PyPi, or you just, like, say it's deprecated and stop doing releases.
**Riccardo Magliocchetti** 11:36 The problem with… Yeah, but in this case… We are just removing, The patching of the… an extension of the bottle core, not the whole instrumentation.
Because the…
**Dylan Russell** 11:50 Oh, that's right.
**Riccardo Magliocchetti** 11:51 dispatching.
**Dylan Russell** 11:52 do this.
**Riccardo Magliocchetti** 11:53 There's a lot of other components, so…
**Dylan Russell** 11:56 That's true, that's right.
Good point.
**Riccardo Magliocchetti** 12:01 What do you mean that?
**Liudmila Molkova** 12:03 Yeah, I think we cannot remove it, because… Well, it would be breaking, and even though it's experimental, People hate when we break.
But this instrumentation in Bottogo Core, we have, it emits all semantic conventions, it's… Basically uncompliant with all the new stuff.
And we can take two… options. The first one, the suppression.
Like, Dylan, you're working on suppression, we can leverage it here.
But then it would result in the border core.
Well, you could probably fight with each other, right? The order is unpredictable.
So we need to figure out some way for them to agree that in presence of the new instrumentation.
the old one.
turns off.
But… I don't know how Python Distro works, folks. I hope… like, how can we… if it enables both… can it enable both instrumentations at the same time, and how would it decide which one to enable?
**Diego Hurtado (Dash0)** 13:22 Sorry, what do you…
**Dylan Russell** 13:27 I think it is possible for both of them to be enabled.
And… I think it's… Like, if you look at the code back in the issue, I think you can detect if it's… Like, yeah, you can… Yeah.
**Liudmila Molkova** 13:50 You have the proposal, nice.
**Dylan Russell** 13:52 Yes.
So, yeah, I think we could do that, something like that, yeah.
**Liudmila Molkova** 14:02 How would… what would we do? What would be the criteria? Why we enable one versus another?
**Dylan Russell** 14:08 if… we see the new one in the GenAI repo is… Installed.
like… Then we disable the one in contribib.
If it's, you know, if it's installed and it's… it's active.
**Liudmila Molkova** 14:29 Maybe we… since it's an existing instrumentation, and we're keeping the rest of it, and we shouldn't degrade it, maybe we can do this. This check is awesome, but can it take the GenAI opt-in into account, like the NVAR we have with latest experimental?
And if it's enabled, Then… it would… Use the new instrumentation.
And whenever new instrumentation is activated on its own, no matter how, it would be on.
But we would only… Yeah, activate, like, instrument, call the instrument or instrument on it in the distro if the NVAR is set to latest experimental.
**Dylan Russell** 15:23 That, I think, is possible, but… I think in the new repo, we got rid of that NVAR.
And we just said.
**Liudmila Molkova** 15:31 Yeah.
**Dylan Russell** 15:33 So you're saying…
**Liudmila Molkova** 15:37 It will stay the same in the new repo?
Okay. But in the body core instrumentation, it would look into, like, in the distro.
**Dylan Russell** 15:45 Okay.
**Liudmila Molkova** 15:46 We would decide if the new one is active based on that one.
**Dylan Russell** 15:52 Okay.
So we add the NVAR to the… to the contrib repo.
**Liudmila Molkova** 15:59 It's already there.
**Dylan Russell** 16:00 Okay. It's already there, okay.
So we just check it.
Alright, and then… Eventually.
Like, way down the line, we remove it.
Or we just never remove it.
from Contrib.
**Liudmila Molkova** 16:28 If we plan to ship V1 of this instrumentation.
like, the stable one. I think that, like, the clean… Fresh V1 would need to ship without it.
**Diego Hurtado (Dash0)** 16:44 Right, let's just, keep in mind that, If, we could, end up in a situation where This one has a hard dependency on OpenTelemetry instrumentation, and… Stopping releases.
Can cause a problem for people who… Still have this.
installed and want to move.
forward and use newer versions of OpenTelemetry, right? So… Before we do that, let's make sure that we make a release.
That a dependency on another OpenTelemetry component with a… Carpent.
**Dylan Russell** 17:45 Okay, so keep doing releases of the old… the old Rio.
the, the one in Contrib, basically.
**Diego Hurtado (Dash0)** 17:55 I mean… Not necessarily, just make sure that it doesn't pin… hard… to, another OpenTelemetry component.
**Dylan Russell** 18:14 Okay.
I'm not sure I'm following it exactly, but…
**Diego Hurtado (Dash0)** 18:23 So, what happens is that every instrumentation depends on the OpenTelemetry instrumentation package, right?
**Dylan Russell** 18:30 Yeah.
**Diego Hurtado (Dash0)** 18:31 Okay, so… If an instrumentation says.
It depends on OpenTelemetry instrumentation with a hard pin that says exactly at version X, right?
then… If someone is using that version, right?
And, then we decided not to make another release.
Of, this instrumentation.
The other instrumentations, err.
gonna… Depend on the pentol limestone instrumentation, That uses a new version.
And this one will be… requiring… an old version of a mental limit implementation, so they're not going to work together. So the solution is that before you make, The solution is, you make a final release Of this instrumentation that… does not depend.
on a hard… specific version of OpenTool Limit instrumentation.
**Dylan Russell** 19:43 Okay, yeah, that makes sense.
I'm with you.
**Riccardo Magliocchetti** 19:52 But again, this is not the case where we are, dropping the whole instrumentation. This is just, unexcept…
**Dylan Russell** 19:59 Yeah.
**Riccardo Magliocchetti** 20:00 Extension of the bottle.
instrumentation.
**Dylan Russell** 20:05 Right.
**Riccardo Magliocchetti** 20:06 So, like, anyway, the… the problem, like… having… not having an art dependency, like Diego's plane, in this case, will let, an user to have, like, an older version of the system vision installed.
With the old semantic omission export.
Same issue, more or less, yeah.
Okay, any other comment?
Okay.
So… Maybe mute.
We want to take a look at the… Of the dashboard issues.
But they think about, like, a ton of stuff.
This one, Diego, do you know?
If you have any open comment…
**Diego Hurtado (Dash0)** 21:33 Just scroll down… no, I think I have the rest of everything there.
**Riccardo Magliocchetti** 21:41 Okay.
Funks.
Okay, meet the maintainer there.
I think he's, I have to update the review.
Yeah, this will need another look.
I've also probed this one.
Okay, we have this one, that requires another review.
this slide.
Changing the… The signimatur of the configure.
New function, new method.
Yeah.
In order to permit to have any target ones.
What else do we have?
Okay, we have a couple of issues with the OPRs, but… didn't already reviewed from the… Same user as before, so we need a second look.
Hong, please.
Yeah.
This is, like, really, like, issues that only, only most of the time, engineering model will be fine.
And then we have this one, yeah.
About… Optin for the… Logosomatic invention, I think.
And let me just take another look, please?
Good to meet you.
**Liudmila Molkova** 23:47 Can… yeah, can I stop here for a sec? I think I took a look at this PR at some point, and I… it's not a problem of the SPR, but it's something pre-existing. So, we have the start span decorator, right?
And… the decorator… Once… when we get an exception during span execution.
Python SDK today.
A report's a span event.
The exception, like, records exception event.
By default.
And this is extremely noisy.
And we cannot change it for the old world, because, well, people might rely on this.
Can we… Change it with this opt-in, and attach this breaking change to the opt-in, saying, okay, we stopped doing this by default.
Users decide when they record exception event.
And also, Python is pretty unique in the sense. I don't believe any other, well, at least not… many other SDKs record exceptions by default.
**Diego Hurtado (Dash0)** 25:15 I mean, I'm fine, something important is, to make sure that, This gets, An entry in the changelog that says.
Something like warning, we have changed this behavior.
So that people who update.
Nope.
This is happening.
**Liudmila Molkova** 25:43 nice. Did you folks receive any feedback on verbose span events for exceptions?
**Aaron Abbott (Google LLC)** 25:54 I think… so, so… Honestly, I think people kind of like this, from what I've seen.
The only thing that I've seen is that we recorded on all the spans that the exception bubbles up through, instead of.
**Liudmila Molkova** 26:09 Exactly.
**Aaron Abbott (Google LLC)** 26:10 Yeah.
So was… wait, so Lumila, were you talking about the fact that we recorded at all, or the fact that we recorded at all the levels?
**Liudmila Molkova** 26:19 The fact that we recorded at all the levels, like, eventually… somebody will look this exception, most likely. Web framework, something on the other side.
And all these additional recordings are just duplicative, and they are… Really expensive, because stack traces are a giant.
**Aaron Abbott (Google LLC)** 26:45 Yo.
I don't know, has anybody seen complaints about this? I feel like, honestly, I haven't seen anybody complaining about this behavior.
**Liudmila Molkova** 26:56 Okay.
**Aaron Abbott (Google LLC)** 26:59 But I agree, it's expensive, definitely.
**Liudmila Molkova** 27:05 Okay, I'll do my best, I'll try to leave a comment on this PR. I think it probably is a different… Change, though.
Just to keep things separate.
I'll try to find some, Reasoning, and some spec language, or some other precedents, around it.
Okay, it's good to know, and, like, if we make the change, It would not be possible to… attach a new breaking change in a different release, because nothing… I could just want to be honest with users and be, protect the stability guarantees we have, so once it's in, once it's released, we cannot bundle more changes to this opt-in.
And it would need to happen in the same release.
**Aaron Abbott (Google LLC)** 28:13 Yeah, that makes sense to me.
**Diego Hurtado (Dash0)** 28:17 Sorry, Liila, what do you mean by bundling other… Thanks to this opt-in.
**Liudmila Molkova** 28:25 I mean that I don't want to change the current behavior for users who get span events on every, exception as it bubbles up on every span, that's fine.
We don't want to break it. But this introduces opt-in to report this not as span events, but as logs.
And if we want to, change the frequency of… and the defaults of what we report.
then we should… Do it behind the same opt-in.
So users who start doing… start getting logs.
Won't be broken again in the future, and we will… Like, reduce their cost by not reporting the same exception multiple times.
**Diego Hurtado (Dash0)** 29:19 Right, okay, a couple of things, This is a new environment variable, right? Without semiconf exception signal opt-in.
Okay, first, just… I think we should not use opt-in, I mean, the… that is… the environment variable…
**Liudmila Molkova** 29:41 This is defined in SEMConf. This is the part of the onboarding into… logs. Okay. Yeah.
**Diego Hurtado (Dash0)** 29:49 Okay, wait, let's go back then, let's just forget about that, what I just said.
Is… so the… there is already a… A definition on what this empowerment variable should do, right?
Okay, so… I probably did not understand that. I thought you were asking if, in the future, we could add Similar behavior to be attached to this environment variable.
Is that what you're asking?
**Liudmila Molkova** 30:24 I'm just saying, there is… there's a bug. I… well, I personally treat it as bug, you can disagree with me, that Python records exceptions by default.
As events, on every span, as they bubble up.
and we cannot change this, because it's an existing behavior.
This opt-in, whatever it is, gives us an opportunity to start clean for logs.
**Diego Hurtado (Dash0)** 30:50 Okay.
**Liudmila Molkova** 30:51 We don't attach new behavior, but we effectively fix a bug, without breaking anybody.
**Diego Hurtado (Dash0)** 31:06 Aaron, you had your fundraiser.
**Aaron Abbott (Google LLC)** 31:10 Why don't you go ahead? I was gonna… Say something about… just… just clarifying something else, so… Please continue if you've got more questions.
**Diego Hurtado (Dash0)** 31:20 Yeah, I was just thinking that if this is a Python-specific thing, don't we need a hotel Python environment variable?
Instead.
**Liudmila Molkova** 31:33 What, what is Brighton's specific thing?
**Diego Hurtado (Dash0)** 31:38 Surya, I thought you said that… Only Python has this behavior.
And that behavior is… It's what we're trying to… Change here.
**Liudmila Molkova** 31:55 Yeah, I'm suggesting that we just start clean for logs.
For logs, we don't need to repeat the previous mistakes. Saying, okay, to… you need… To… like, it's already an opportunity to logs.
This is the way that looks.
would work. And I believe there is a language in semantic conventions already that says that you should not record it as exception bubbles up.
**Diego Hurtado (Dash0)** 32:25 Okay, okay.
Okay, Aaron, you can go ahead, please.
**Aaron Abbott (Google LLC)** 32:35 Yeah, so Ludmila, it sounds like you're gonna leave a comment, but I just want to make sure I understand the… you said something about other languages don't record exceptions by default. Did you mean, like, in general, or at all levels? Because that's… that is controlled by an option right now?
I think people like it, I think it behaves well for Python.
I just wanted to clarify that.
**Liudmila Molkova** 32:59 Yeah, so recording exceptions by default in instrumentations.
And for all spans, Results in this duplication problem.
And, languages in general don't do this.
they leave it up to the user, or to the instrumentation. So, for example, the HTTP instrumentation.
would record its own exceptions. Well, not its own, but the code, as log events.
The deliberate log events with a specific event name, rather than generic exception.
And this is the future for logs.
**Aaron Abbott (Google LLC)** 33:43 Okay. I was asking mostly about just… I understand about at every level, but just at the lowest level.
Is that behavior also wrong?
**Liudmila Molkova** 33:53 The ideal situation is that you record it at the highest, the outermost layer, because if it's… if it's handled, if it's swallowed, you don't care.
So, you don't record it, but then… And it's way beyond the current discussion, but, let's say you host a web service, and then your web framework would log it for you anyway, or your application can log something that didn't.
It, it may be processed. Whoever handles the exception decides How to log it, and if to log it, and what severity it should be.
**Aaron Abbott (Google LLC)** 34:31 Okay, I… yeah, maybe let's take it offline, but… Yeah, I'll check for the comment on this one, and we can discuss there.
**Liudmila Molkova** 34:41 Yeah, thanks.
And I don't mean to block this, I mean that I'd like to maybe contribute the change, but I want to coordinate it so that we can bundle two changes together.
Breaking changes together behind the same object.
Yeah, thanks, sorry for the tour.
**Riccardo Magliocchetti** 35:05 Thank you.
And by the way, related to this… We have this one.
That is trying to… Yeah.
Adding more use for the exception escaped attribute.
That, I think, is deprecated, right?
**Liudmila Molkova** 35:30 Yep.
**Riccardo Magliocchetti** 35:31 for.
**Liudmila Molkova** 35:31 Nobody knows what it means.
**Riccardo Magliocchetti** 35:35 Let's probably be sure to clean up, like, with this new opportunity, we should probably also stop to… To set these attributes.
So, a triple change for BC. Okay.
I'll put it here to the notes.
Okay… And then, okay.
We have, a renovate PR bumping some stuff for CI, I guess.
Okay, this is… okay.
So, this is updating workflows.
**Tammy Baylis** 36:39 Riccardo, there's another topic that's been added to the meeting minutes.
**Lukas Hering** 36:44 Oh, I added it last minute, we don't need to spend too much time, Yeah, I, I've just been using, I was using Valky at my employer, and I just realized there's no instrumentation for it.
I know that someone had squatted on the package name, and I think it actually might be gone now, I'm not sure if there's a status on that, if we can try claiming it, since I actually don't see it in PyPi anymore.
But another option would just be to… Add the, like, similar for… some of the other projects. I was wondering what we thought about maybe just… Making it so that the Redis instrumentation also instruments Falky, if it can find it.
Since there's, like… I'm pretty sure it would be, like, a few lines of changes, just… Removing some is instance object checks.
Or if we would prefer to have it be its own package.
**Riccardo Magliocchetti** 37:57 two things. First, I think, yeah, the package has been freed from the previous Owner, so it's free to use.
And the second thing is… I'm not sure, like, code-wise, maybe… could be a yes, like, to reuse the latest instrumentation. I'm not sure, given that one is the fork over another.
And probably when going to introduce… Breaking changes.
I guess.
I don't know.
**Lukas Hering** 38:36 Okay, yeah, we should probably claim the package if we, if it's available then at this point.
I don't really care if we… Make it its own package or not.
**Riccardo Magliocchetti** 38:50 Like, last time I looked at this, the problem was that they were implementing the… the very same radius, semantic convention, so not the stable one.
And since this is a new page package, it doesn't make any sense to implement, to something else than the stable semantic invasion, I guess.
**Lukas Hering** 39:14 Yeah, I see they also, like, added, I think, is that, like, a helper?
package for shared code, maybe we could maybe do that if it's… Yeah.
Okay, yeah, I think it sounds like maybe just make it its own package, then.
**Riccardo Magliocchetti** 39:31 Yeah, like, I remember also a comment from myself about this, but probably, like.
Yeah, they introduce, something shared, but we haven't updated the radius to use that.
Or something like that.
**Lukas Hering** 39:45 I… yeah, I think the reddest one is actually… There might not even be enough to warrant.
the co-chair, I'm not sure how much there actually is.
**Riccardo Magliocchetti** 39:57 Okay, so, yeah.
Like, I think we can reopen this one.
Maybe take another look.
And maybe take over on the branch.
or sulfine.
**Lukas Hering** 40:13 Okay. Yeah.
So yeah, I guess just to clarify for everyone else, like, we want to keep… assuming we're adopting Valky, we want to have it as its own package, then?
Like…
**Riccardo Magliocchetti** 40:30 I think it's a bet, like, we don't know if… Any… like, what direction the… any of the true code bases will take. So maybe in the future, like, they change the antennas and… Because sharing doesn't make sense anymore, like, I have no idea.
Also, I think, but right now, like, code sharing is not possible anymore between the two code bases, right?
Because I think… well, maybe not the client, like, I don't know if the client changed their license or something.
**Lukas Hering** 41:07 I think most of it… I mean, there might be, like, one or two cases that we could just special case.
In the library code, but… Yeah, it's probably cleaner to just have it… have it be its own package.
Yeah, depending on if whoever's contributing this is still active, I would maybe just start from scratch, I'm not sure, like… If this is just a… I'll take a look at it.
**Riccardo Magliocchetti** 41:50 Okay, thanks.
Their opinion or comment on this one?
Okay.
I depend some notes about the discussion.
**Lukas Hering** 42:37 Just as another comment for anyone that is using Valky.
I did also realize that there's a Valky Glide client that does have native OpenTelemetry, so I might end up just using that anyways, but… I think it would… I think this is still pretty… a lot… it seems like a lot of people are wanting this, and so…
**Riccardo Magliocchetti** 43:10 Hmm.
**Lukas Hering** 43:11 It's called Valky Glide. I think it's written in Rust.
**Riccardo Magliocchetti** 43:14 Cool.
**Lukas Hering** 43:16 And… I guess the only… I think it actually integrates correctly with the OTEL SDK. I'd have to look at it.
But I know that there's, like, always… it's a little tricky when you're crossing between, like, Python and native code, with OpenTelemetry.
**Riccardo Magliocchetti** 43:58 Okay, thank you.
Alright.
Went to the contrib… Lukas Dashboard… Okay, I think this is just a commentation.
So there were some comments… Okay.
We have some comments, I think, about new formatting.
Okay, with this one, I've… quote, Abbott Tayyad… Did this to the Magic Hill.
Yeah, but it failed.
Okay, now it's, like… In public.
maybe just me, but, like, I felt very hard to find what What best is fa… what job is failing at the arm?
Okay, I'm gonna do the fly.
And then… yeah, remember this one? This is changing the… the network transport for, a SIG PG.
from, pipe to Unix socket, I guess.
So, waiting for a second approval.
Okay, this one may be interesting to discuss.
I opened this one to see if we can maybe simplify the… template, I've started from country.
Like… The… the template will look like something like… this part.
Like, the description, of course, but… We lost, like, a couple of paragraphs. I don't remember which one.
Yeah, the one that requires, corrupt change, but is now, Are they entering a checklist?
And also, we removed the, like.
From the checklist, like, I added a changelook, I followed the style, I added tasks and stuff like that.
To be more, like, acceptable things that fails.
And… Yeah, I think we have, Enough approvers, but the more the merrier, I guess.
And Ben, what do we have?
Based on being, you know, attribute a thing to… Kafka?
Okay, so this is just looking for a maintainer to take a look.
Imagine?
Okay, maybe serious… OPRs… Not crashing when the… We have an empty comment.
I think we're trivial enough.
I approved, I think, all of them.
But I need another approval, please.
I think they did, the same… the same change, for the… for every instrumentation.
Which is just, like, not the referencing… not assuming there is something when we split the comment.
Oh, God.
Grab this one… I think… Alberto salary… Let me review it.
Do we have open comments? No?
So, yep.
Estates… I'll maintain a review and merge.
This is the very same 24. Okay, we are the rough one. I think, Aaron… You added some comments on the one in core?
But we are losing, like, using the default, Configuration, we are losing some checks.
**Aaron Abbott (Google LLC)** 49:01 Yeah.
I just put it… In the chat, but…
**Riccardo Magliocchetti** 49:07 Thank you.
**Aaron Abbott (Google LLC)** 49:10 So I… I don't know if Emidio's here, but… Oh, you are.
**Emídio Neto** 49:14 Yeah. Yeah, I'd say… Yep.
**Aaron Abbott (Google LLC)** 49:18 Mike… might be mistaken, you wanna…
**Emídio Neto** 49:21 Yeah, my initial understanding was… All those rules were there by default, but it seems not the case.
**Aaron Abbott (Google LLC)** 49:32 with…
**Emídio Neto** 49:32 should, ugh.
We should have the select block, in my opinion.
Should keep the select block.
**Dylan Russell** 49:41 Instead of the extend select?
Why?
**Emídio Neto** 49:56 Like, I prefer to have the results in, like, split away, exploit.
We can add and remove as we want, then rely under the photons.
**Dylan Russell** 50:08 But if we… There's so many default rules, so then it's like, you get, like, the huge list.
**Emídio Neto** 50:19 Yeah, but some of them are missing, right? So, TID is missing.
Some of them are missing.
**Dylan Russell** 50:29 But can we use the… I think there's, like, an extend select thing.
**Emídio Neto** 50:32 Yeah, I left a comment about that, but I'm unsure.
**Dylan Russell** 50:38 Yes.
**Emídio Neto** 50:39 I'm not sure if it's, like… Because, let's say in new version, they can add New rules on this list.
So…
**Dylan Russell** 50:49 Yes.
**Emídio Neto** 50:51 It's good.
**Dylan Russell** 50:52 Yeah, sorry, go ahead.
**Emídio Neto** 50:57 Yep. I think it's good, but can be… I'm thinking that… Every time they change this, the full list, we have to… To run roof again.
And deal with a lot of conflicts in our codebase.
But… Yeah, that's a decision you need to take.
**Dylan Russell** 51:24 Yeah.
I sort of think we should just do it that way, and every time we upgrade, we'll have to do a little bit of work.
Or decide if it's worth doing.
But… Yeah, I would… I think I prefer just to use Extend Select to add The… the ones we want to add back in.
**Aaron Abbott (Google LLC)** 52:00 So it sounds like, Dylan, you're saying it's intentional to… Always keep the default rules.
**Dylan Russell** 52:08 Yes, yeah, I… I think we should just use the default ruleset, and… If they add new rules to the default rule set, then, like.
I'll have to change the code a little bit, but… I think it's okay.
**Aaron Abbott (Google LLC)** 52:25 Yeah.
I mean, it makes sense to me, if… assuming Extend Select works like that, I don't know, Emidio, if… Do you have a specific concern besides just the…
**Emídio Neto** 52:39 No, just think about the maintenance burden, too.
I always have to deal with conflicts, but…
**Aaron Abbott (Google LLC)** 52:49 Yeah, Riccardo?
**Riccardo Magliocchetti** 52:51 Yeah, wondering if… Like, we'll renovate, also try to bump rough.
Right.
So we can catch any issue there.
**Emídio Neto** 53:04 Yeah, right.
**Riccardo Magliocchetti** 53:05 Like… like, if… like, I don't know, like, if we get all details, like.
I, like, I'm not sure we get, like, what is failing.
**Emídio Neto** 53:19 what the.
**Riccardo Magliocchetti** 53:19 Only the failure, maybe, from CI?
So, yeah.
**Emídio Neto** 53:23 Yeah.
**Riccardo Magliocchetti** 53:24 Yeah, yeah, so probably, like… I… when the CI will fail on a renovate bump, we should take a look.
Oh, yeah.
Like, we can try. If it doesn't work, and we can switch to select, back to select.
I guess, like…
**Emídio Neto** 53:43 Yeah, makes sense.
Yeah, let's try.
But indeed, some rules are missing.
**Dylan Russell** 53:51 Yeah.
**Emídio Neto** 53:51 Thanks for catching that, Tara.
**Aaron Abbott (Google LLC)** 53:54 Yeah.
Neapolitan.
Cool.
**Riccardo Magliocchetti** 54:03 Yeah, okay, the last… Two issues. This one is interesting. This is fixing the trading instrumentation.
sorry, the AICIO instrumentation.
Where, like, we are not… Measuring the… The real time of the, like, real time of, the future, but only, like.
Just like when we create the future.
And so if… Anyone who's more skilled than me, honestly, you can take a look.
Please do, but… Like, to me, it makes sense, you know.
It's trivial to see that right now we have an issue.
**Aaron Abbott (Google LLC)** 55:04 Yeah, I can take a look, that sounds… Sounds good.
**Riccardo Magliocchetti** 55:10 Thank you.
Whoa.
Okay, we're… For some reason, we have the old engineer group as a… Approver for Jungle Change?
Okay, let me clear it.
**Tammy Baylis** 55:34 Yeah, this PR's had a lot of, edits that shouldn't have been there, like.
**Riccardo Magliocchetti** 55:40 Oh, okay.
**Tammy Baylis** 55:41 Gen AI changes before, and… Yeah.
**Riccardo Magliocchetti** 55:48 Okay, so this is waiting for a second review.
Okay, it's touching there.
By the way, related to… well, mostly related to this, I don't know if you've ever seen, like, what has been, like.
An article… a blog post from… met… Dangan, or something similar.
But it's the news about, about telemetry, community working or not.
And on Acker News, there was, like, a comment about a user of the Java instrumentation.
And we were, like, complaining because we have a middleware that is not public, and so we couldn't use that.
Yeah, sorry, my brother, about… The job is to finish.
Yeah, I think it was just the last one.
And… You have 3 minutes back?
Thank you, everyone.
**Liudmila Molkova** 57:03 Thank you.
**Dylan Russell** 57:04 Stiggers.
**Lukas Hering** 57:06 Thanks.
