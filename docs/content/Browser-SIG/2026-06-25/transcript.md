SIG: Browser SIG
Date: 2026-06-25
Duration: 19 minutes
============================================================

## Zoom Recording Transcript

**Joaquín Díaz** 02:17 Who knows?
**Maxime Quentin** 02:22 Nope.
**Joaquín Díaz** 03:04 I think Martin is out today, I'll… I got on this one.
Share the screen.
Can you see my screen?
**Hugo Levy** 03:23 Yes.
**Joaquín Díaz** 03:25 Cool.
Alright, going through the agenda, first topic is from Maxine.
Do you want to share?
**Maxime Quentin** 03:33 Yes, I mean, first quickly, following the issue of, duplicating, webcommon. I've, opened, like, two small PRs. I've seen your reviews, David, and, updated it, so… I think I probably need a second review, and then I'll be able to match.
Otherwise, like, so far so good. The CSN processor is live in the sandbox, and works pretty well, so… just to see how it works and how we population for the time being. You can just go to the sandbox and check by yourself.
And yep, that's pretty much it.
**Joaquín Díaz** 04:19 Yeah, Alex, that's the way. Yeah.
Next one is from… You are, This one… do you want to share what you did?
**Hugo Levy** 04:34 Yes, I mean, you can… it's just a really tiny PR. It's just about the sandbox. I just wanted to add it, like, one small button, actually, like, triggering, an exception, so that we can send this type of events. Because, like, looking at all of the existing buttons, none of them were actually, sending exceptions.
So I just wanted to add one in the sandbox, plus, like, tiny contributions, but at least two… The very first steps into contributing.
**Joaquín Díaz** 04:59 Yeah, yeah, thank you for that.
**Hugo Levy** 05:01 Oh, do you.
From David, thanks.
**Joaquín Díaz** 05:06 Yeah, just one small question, like, why did you use timeout to throw the exception?
**Hugo Levy** 05:12 At that, when I didn't have timeout, the log was sometimes, not sent.
But yeah, I can, I can dig into that.
**Joaquín Díaz** 05:22 Okay. Yeah, weird. Yeah, it should… shouldn't matter.
Yeah, if you can take a look and see if it was something else. I'm just curious, like, I think it's fine, it's a demo anyway, so… Just curiosity.
**David Luna Bistuer** 05:40 Question I have, Hugo, if you go to the PR, now that they have a couple of, approvals, do you see the merge button? Or maybe it's the permissions are not…
**Hugo Levy** 05:51 Let me check. I mean, the first issue I had is that when I had the commit, I couldn't… I didn't see the CI jobs running. Did you run the…
**David Luna Bistuer** 05:59 Yeah, we need to approve. We need to prove that, yeah. Okay.
**Hugo Levy** 06:03 Are we looking at the PR, if I can find it again. Sorry, I don't have it, just behind… in front of me.
So asking me if I can see the merge button?
No, I don't see any…
**David Luna Bistuer** 06:19 Okay.
**Hugo Levy** 06:19 I don't have the permissions.
**David Luna Bistuer** 06:21 That's a bit different from the country and core packet repositories of JavaScript. So, I don't know, maybe I'll open up PR and maybe try to align that. So.
I don't know, maybe it's just a… Thinking a lot here is that if you already have approvals from a couple of maintainers, you should be able to manage yourself.
**Hugo Levy** 06:42 You can stick it.
**David Luna Bistuer** 06:42 Right? I don't know.
**Hugo Levy** 06:43 I want to take another screenshot really quick, like, so that you can see what I see on the… on the PR?
**David Luna Bistuer** 06:49 Yeah, so usually, so for me, it's all the workflow that I follow in country is like that, so I do the PR, I get the review, and then I get the approval then, you know, so the interested part is actually merging, so I don't need to, you know, maybe someone, someone else wants to… There's something about you have the option to merge yourself. If not, I have to come back a second time to the PR and merge it myself, or if someone else is already debil, so I don't know, I'll check the… I'll put this on my list, and I'll check the permissions. Maybe I'll have a conversation with the other maintainers about that.
**Joaquín Díaz** 07:27 Yeah, that makes sense to me, like, you should be able to merge your own PRs if they are broke.
**David Luna Bistuer** 07:33 No.
**Joaquín Díaz** 07:34 I don't know, probably we just need to… to our pull requests into the, like, the DevOps repo.
Manishisola.
Yeah, that makes sense.
Okay, the next one is… From you, David, the… context for you.
**David Luna Bistuer** 07:55 So, So, basically, kind of an idea to actually move forward without, having, so then kind of have a delay or give the final decision on… on… on… you know, if we wanted to expose this API to publicly, kind of the idea… well, the idea right now is, like, we are going to use it internally between the Feds, XHR, and resource damage implementation, okay? So, maybe we don't need to expose the API yet to Manager and the… all the configurations. And also, I think that the… On the other side, I think that we are kind of having two conversations at the same time. The first is about, you know, coordination between these instrumentations, and the other one is about the configuration itself. We know that we have configurations that are shared between instrumentations, like ignore URLs.
So, yeah.
I think configuration is a different topic that we need to tackle at some point, or have a discussion at some point.
So, if we have this, let's say, private or internal in the instrumentations package, we use it internally, we have this API, and when we are confident and we are already solved the configuration, problem, the complexity of the configurations, then we can expose that later in a new release.
So… Long story short, TLDR is that… that is my proposal. So we can move on, and then actually, you know, move forward on the implementations on fetch instrumentation and resource timings.
**Joaquín Díaz** 09:22 Yeah, I agree. I replied here on your proposal.
I think that makes sense. Like, originally, I was trying to avoid having, like, things depending on each other, but I think it's… as long as it's internal, I think it's fine.
I also created a draft PR.
Based on this, which is just… You know, having the network context manager as, like, an internal package in instrumentation, and then add it on top of master, so we don't have the fetch instrumentation, but it will be something like that, like, the resource time instrumentation just… Drafts a manager, and tries to get… get context from the manager.
And that's it. Like, then we will have the flash instrumentation doing the opposite, like, getting the manager and setting the context.
And then the manager will be just a singleton that lives on this file, like, no need to instantiate it, like, the user now doesn't need to do anything.
And, I think… as long as it's internal, I think it works. It's simple.
And then in the future, if we get someone saying that they want to use their own network context manager, we can figure out a way of them, like, setting that without an API external, I guess, external API is not available for now.
I think it works, and they fixed it. They fixed the issue, and yeah, as you say, it allowed us to move forward with this.
Mostly the fetch instrumentations that are the ones that are… we are really trying to move forward with.
**David Luna Bistuer** 11:00 Yeah. Well, there is also document load instrumentation that actually is using also Span Events, so maybe you can… Use that. So, okay, ping me when it's ready.
So we can review, and then we decide, which… we have a couple of PRs on fetch Instrumentation, so let's close one in favor of the other, so let's have that conversation offline.
Yeah. And… yeah, and once it's done, then we can, move on to other resources as well.
So maybe I'll…
**Joaquín Díaz** 11:28 Yep.
I will clean this up, I'll add a few tests, but I don't think there is… more to add to it. Anyone, feel free to take a look.
And then, yeah, we can merge it. Maybe I wouldn't do the risk assignment change until both are merged, and then we can make it work. But for now, just add the, like, the manager on its own, doing nothing, and then we can add it to instrumentations.
**David Luna Bistuer** 11:59 Okay.
**Joaquín Díaz** 12:01 Cool.
Ted, you're next.
**Ted Young** 12:14 Hey!
Just wanted to raise awareness. There's a Dart Flutter proposal that's been around for a long time, but it's getting legs, and I'm just curious who from this group is, like, interested in Flutter.
Because we want to make sure this thing is successful.
**Joaquín Díaz** 12:37 I barely played with Flutter a few years ago, but I'll share this with the Embrace team. We have, DART. I think we have a DART library, so I'll share with them to see if they're curious about it.
**Ted Young** 12:52 Yeah.
Sorry, go ahead.
**Cleo Schneider** 12:55 I was gonna say, I'll also, send a note around, because we certainly have some Flutter folks over in our neck of the woods, so…
**Ted Young** 13:03 Awesome, thank you.
**Hugo Levy** 13:06 Yeah, same with the Padoga as well.
**Ted Young** 13:09 It's one of those things where it's kind of, like, adjacent, but it also makes me think about kind of rebooting. You know, we had a sort of, like, client SIG, which was where we sort of coordinated across things, and when we spun out the browser SIG into its own fully formed group.
the client SIG went a little dormant because we felt like, you know, things were cool, but I feel like, you know, when this thing pops back up, it might be a good reason to… to maybe resurrect that, or otherwise find a way to… to start coordinating around again, just because it's… you know, there's a lot of overlap between, I think, Flutter and Dart and browser and everything else.
So, just raising awareness, that's all.
**Joaquín Díaz** 14:01 Thanks.
All right, we don't have any more topics. Does anyone… something to discuss, or something that I want to raise?
Okay.
Yeah, I, I think… Next step for us, most importantly, we have to try to merge these instrumentations, the ones that are missing, and the big ones that fetch.
And etc.
So, yeah, let's try to review this PR. I'll try to clean this up today.
And then, David, let's talk offline to decide. I… I don't… I don't care if it's yours or my PR. I will close mine and give you feedback on how I approach… I approach mine, so we can just merge some ideas together.
But yeah, let's try to move it forward.
**David Luna Bistuer** 15:00 I'm kidding.
**Joaquín Díaz** 15:01 Alright.
That's it.
Thank you, everyone.
**David Luna Bistuer** 15:05 Have a good day. Bye.
