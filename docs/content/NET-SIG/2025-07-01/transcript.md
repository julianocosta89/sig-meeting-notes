SIG: .NET SIG
Date: 2025-07-01
Duration: 50 minutes
Zoom Recording URL: https://zoom.us/rec/share/vtVErYUROuZ-NfjXIzA0zp6O8UcqJg7iAX9O_zzm5LbTRmYkcQgTwQgED5Xo2JUx.gnMY9ftdGqAvqmlu
============================================================

## Zoom Recording Transcript

**Alan West** 01:55 Hey! Martin.
**Martin Costello** 01:58 And how you doing.
**Alan West** 02:01 Doing well, how are you.
**Martin Costello** 02:04 Very warm not to be very British and talk about the weather, but it's exceptionally hot here at the moment.
**Alan West** 02:11 Yeah, it's been warm where I am as well.
It was nearly a hundred degrees yesterday.
**Martin Costello** 02:25 Yeah, it's too much for me.
**Alan West** 02:29 I agree, I agree.
Let's see.
go ahead and share my screen.
What do we want to talk about today?
How about we start with your Pr.
**Martin Costello** 03:02 Yeah, so we don't. We don't necessarily have to go into this in great detail right now. I just wanted to sort of nudge it a little bit because I did the start at the beginning.
So we were trying to update the hotel libraries in our Grafana distribution of open telemetry cause. We're at libraries on like something like 1.9 at the moment.
and bring it up to 1.12, and then that exposed the fact that the use of.net 9 forces everything to go to.net, even if users wants to use Lts don't.
So I remembered that I'd seen an issue about it.
So I went away and dug around into that with the proposal that we talked about previous time. We discussed this, which was to sort of go.
if possible, go backwards and sort of have everything match.
but when I actually looked into it, the wrinkle with that is, there's actually new Apis added in the.net 9 package that the have been used in the code.
So unless you we wanted to break, make a breaking change, or to sort of remove it from the.net. 8 target. I don't think there's a neat way to sort of resolve the problem for ships that have sailed.
There was a suggestion in by a comment of the person who opened the original Pr about versions who suggested Polyfills. But I I haven't looked into that. But if my gut feel feels that that's probably too complicated, there's probably too much lurking in the libraries to actually make that workable, if if at all.
but it could be looked into if necessary.
And then the thing that's made me bring it up today to sort of poke on it again, is there was a it? We had an like an internal customer question at Grafana, and it was related to a.net framework customer.
who, for various complicated reasons and binding redirects, is finding using the open telemetry libraries difficult.
I don't know if it's impossible, but they preach to sort of a limit of how much effort they wanted to put into trying to get the binding redirects to work right now.
and I pointed them in the direction of this issue. It was like, Oh, that's something we're aware of.
So I figured I'd bring it up to, maybe try and get a bit of a bit more movement.
not necessarily resolution, but movement on the issue.
So I could potentially get back to that customer and just say, Yep, yep, wheels are moving, even if they're slow. But I think the way things have gone so far is.
if we did want to fix it the way it was originally proposed, we'd only be able to do that going forwards because new Apis have already been used.
And also there would need to be like a future facing sort of, hey? If there's a new feature in the runtime.
then you have to use the version of the runtime that introduced it.
which is potentially a a contentious viewpoint, because that might be why.
the nines were introduced, in the 1st place, to bring new features to old run times, but there's lots of competing viewpoints on this.
So this sort of there's a there's a little bit of what is the position to go forwards, because my original proposal resolve things for users of.net.
But the original proposal wouldn't have resolved the problem this customer had with done it framework, because that would have been just use latest as well, so they still would have had binding redirect issues.
So I think that's a restatement of where we are.
**Alan West** 07:26 Yeah, help me understand a little bit more. What? The what?
What solution would make things easier for that.net framework customer.
**Martin Costello** 07:37 I think, with the the lens of hindsight it would have been this, the the ideal solution would have been that 9 wasn't added to 8, and the and the net net effects would have stayed on 8 2. But I don't know if anyone would have reasonably reach that conclusion with data at the time. I think the the obvious reason, as say, obvious obvious in quotes the obvious reason to have not got into the situation in the 1st place would have been to always match the runtime versions. But I don't think anyone would have reached that conclusion with a view to donate framework at the same time.
**Alan West** 08:21 Yeah, if we'd been able to go back in time and make these decisions again.
what? I guess, what version of these packages would have been appropriate for the.net framework builds.
To avoid as many of these issues requiring, you know, binding redirects and whatnot.
What what version would we have chosen for these extension packages.
**Martin Costello** 08:49 Yeah, it's a good. It's a good question that I don't necessarily know the answer to like my my knee jerk reaction is to say the most conservative version possible.
but that's colored by me. Having read this customer question.
**Alan West** 09:03 Yeah, yeah, yeah. And you know, that was, that was kind of my position as we were, you know, in the last year or 2, as we've been adopting this practice of using latest of all these packages.
my position, which I didn't push on super strongly, but my position was that we we use the most conservative But you know the point that you brought up the limiting factor there is that eventually there's going to be an Api that we're going to want to leverage from a later version.
And that creates an issue.
I mean, you know, we could just say, well, you gotta like, as you said, in order to use this new Api in order to to benefit from it, then you need to upgrade to the latest, you know, version of the framework, but that's probably not going to fly, for you know specifically these.net framework users who are probably on.net framework for life.
**Martin Costello** 10:19 Yeah, cause it. The the customer did like call out in things they tried. Was that all read about that like they realized that they could have avoided the problem in its entirety by moving to.net over dot net framework. But that wasn't something that they could do at this point in time. So but then I guess this, the sort of the weird, not the messaging, is like.net framework supported Brother effectively.
Yeah, there's the reading between the lines is, but you should move to the new one.
So it's like it sort of implies that if you really want to use the greatest, latest, best things. Then you're not going to get those on donnet framework. Obviously, we're a community project. We're not Microsoft who own donnet framework.
So.
**Alan West** 11:15 Right.
**Martin Costello** 11:15 Different different sets of priorities, and then biases.
**Alan West** 11:20 Yeah, well, yeah, we can't make a breaking change, as you know, you've suggested, but we could still entertain what we do going forward. So you know, ournet a target and ournet 9 target will have to remain the same until you know they're basically end of life. And we remove those targets from our builds.
So, moving forward with.net 10, which I think is an Lts release.
we'll carry forward what we've been doing.
I guess right. That's that this is an option. Just kind of talking it out. We'll carry forward with what we're doing and adopt the latest version of the extensions packages.
And then, and Whennet 11 comes out we'll leave the.net. 10. Build alone.
**Martin Costello** 12:25 Yeah, yeah. So I think I think, like the outcome. I think this Pr is because we can't make breaking changes and need 9 stuff has been depended on in 8. I think this Pr. In terms of merging is probably stuck where it is until November. Now for Donnet 10.
But I think, for then it would be good, and I ideally sooner rather than later, to get a a steer on what the accepted stance is at that point, so that when 11 comes around it's a no brainer.
**Alan West** 13:04 Yeah.
**Martin Costello** 13:05 Because I yeah, I think there's the there's the keep for.net. 10 gets 1011 gets 1112 gets 12, etcetera. But then there's also an open question, of what do we do with.net framework? Does it continue to float to latest? And then that creates undefined forever ongoing issues, fornet framework users?
Do we move it to 10 and then keep it at 10 forever? Or do we like map it to Lts's and donnet framework gets 10, and then it gets 12, and then it gets 14 etc.
**Alan West** 13:42 Right?
Yeah. And there doesn't really seem to be like a great answer fornet framework. I think one of the questions we asked when we talked about this last time was whether the support lifecycle of the framework matches, the support lifecycle of all these extension packages.
You know, if we if we made the decision to PIN dot net framework, to say the extension, the 10.0 extension packages for all of eternity?
Do the do those extension packages have the same, you know, support life, cycle, and.
**Martin Costello** 14:33 Yeah, I think without going and looking up, I think they match they would. The ones for 10 would match.net. 10, because I think the net framework is more that libraries for 10, but they're compatible with framework, but they're not supported in step with.net framework, because otherwise, if that were true, then Microsoft would have to patch 6 indefinitely because of framework with it, which they're not doing.
**Alan West** 15:03 Yeah, I think that makes sense which kind of drives the point home that we we probably made a mistake@leastwith.net framework in in adopting the the latest, I imagine that there's probably a version I just don't know what it would be a version of the extensions packages that are our supported because of dotnet framework.
**Martin Costello** 15:30 Hmm, that's a good question. They're like.
it's potentially, there's some 2.3 versions around for dot asp netcode 2 1. That's now 2 3, which is there indefinitely supported.
Asp net. Call flavor for donnet framework, but 2.3 is a much lower number than 9.
**Alan West** 15:54 Yeah, yeah, for sure, Blanche. Do you know who might have any insight on some of these questions?
They're at Microsoft.
**Mike "Blanch" Blanchard** 16:11 What question?
**Alan West** 16:14 Well, specifically on this, on this note of.net framework like, I guess I guess one of my questions is a little more just theoretical, not maybe something that we can act on, but like. If we had had all of this to do over again what version of the extension packages would be ideal for referencing fornet framework. For now, until basically eternity. If if we were to take kind of that kind of an approach.
**Mike "Blanch" Blanchard** 16:50 I mean, we have our sync with the.net team Wednesdays, so I can ask.
I doubt Noah or Tarek.
We'll have the answer, but they can go chase it down, I will say, though, the current policy where we're just always bumping to latest that was discussed with the.net team.
and they didn't have any concerns with it.
So I'm going to have to try to walk that back and explain it.
It all goes back to this backwards compatibility, guarantee that we're getting from Noah that these packages are all safe to always be on latest. That's sort of the running.
I don't know agreement.
So that's why sort of Riley and whoever was around at the time put the policy in place because there was a lot of discussion with the runtime team, and they're like, yep, you should always be on latest. It's good to be on latest. We should push the community the latest, and that's that's where we are.
So what I'll need from you, Alan, is like what I need to present to them, as far as the friction this is creating, and get them convinced that we should change the stance, and then part of that will be what the stance should be for.net framework.
**Martin Costello** 18:31 Another sorry. Another thing I noticed as well when I was checking up on this is this, I someone had linked to the open telemetry issue about this from the library brighter, and someone had gone to them going, hey, we're having trouble with using this because we're using it was either, or donnet framework. I can't remember which one. And then they were like, Oh, yeah, we can't help you, because we depend on the open telemetry libraries and the open telemetry libraries depend on 9. So you're stuck on 9 because we're stuck on 9. So there's like they sort of extended effects of the ripple effect as well. This is having.
**Mike "Blanch" Blanchard** 19:15 Some of it, I think, is just perspective, like the.net team they're really only ever focused on like the net. Next version of runtime. Right? They're heads down on 10. They'll be on 11.
I feel like I don't know. I'm not part of that team. I'm not privy to these conversations, but I feel like they always ship the next one.
and people can upgrade whenever they sort of force people to upgrade by. You know, having things go out of support, but it's just a different concern for them, because they're not in this sort of general library business.
They have libraries like they ship diagnostic source, you know, there'll be a 10 version. Their solution is, it just has all these targets so you can use it on anything supported and like it's it's done as far as they're concerned. But I think we just have a different use case users. Our users aren't tied to like a Runtime version. You know, they want to use open telemetry. They don't necessarily want to upgrade their whole application. So we just need to kind of do a good job of presenting the case, and why it's a little bit different, and why? It's a problem.
**Alan West** 20:38 Since they were just.
**Mike "Blanch" Blanchard** 20:39 This is really, I mean, this is really for Raj. I mean, if we could wait till he's back.
my vote would be let him pick up this fight, but I'm I'm happy to do it if we don't want to wait till the end of the month.
**Alan West** 20:57 Yeah. In some sense, I think that the they were the wrong advisors on this issue kind of all along.
for the reasons that you've just stated.
I think, though, that it's worthwhile.
And I'm sure that I mean, I know that we have various issues.
That have come up basically articulating the friction that has occurred. If we can maybe in in one issue, consolidate some of these stories of where the friction has occurred that could be helpful to drive the conversation further, like when Raj comes back and and whatnot.
**Mike "Blanch" Blanchard** 21:48 Absolutely.
I think there's a real compelling case to be made, because, if I remember correctly, aspire had the same problem, and they switched to something along the lines of what we're considering.
**Martin Costello** 22:03 Yeah, I think they got linked to this issue because, some of the reactions on the comment I made about potential solutions like Damien Edwards has reacted to it.
So I think there's like, it's always like, use. Several several teams have the same problem.
and they're all gonna see who go who moves first.st
**Mike "Blanch" Blanchard** 22:25 We work pretty closely with some of the aspired people like David Fowler and James Newton King.
I don't know if they're actively still in there, but I could loop them in to sort of provide their perspective on what they went through and why they needed to make a change.
But it. It would help if we had a nice write up to.
you know, like, before we have the discussion I can give to Noah and Tarek and say, Hey, can you go check this out, talk to whoever you need to, and then we can discuss it, you know, at whatever date.
**Martin Costello** 23:06 Yeah, I'm happy to try and distill all the data points I I brought up so far in this meeting into like a short, into a short, snappy document. I don't think I want to go into too much detail. I'll just leave links to other issues. As for people to go off and read the full tome of themselves like this one and the aspire issue, and the the brighter issue I mentioned.
**Mike "Blanch" Blanchard** 23:31 It. It doesn't have to be an internal conversation either. If we get this all in a nice issue.
you know, I can just ping people to go and look at the issue. And we can have a discussion, you know, on the issue.
I can push it along in our, you know our weekly sync meetings and stuff, but.
**Martin Costello** 23:51 I can, I can potentially add it to the the issue that the Pr is linked to exactly the original.
**Mike "Blanch" Blanchard** 23:59 If it was a public issue, and there was a lot of customer feedback on there that's always helpful to get things moving along.
There might already be. I don't know. I don't typically look at the issues very often anymore.
Thank you.
**Martin Costello** 24:17 Yeah, cause I I think, as far as the sort of me bringing this up as sort of via an internal customer we have.
It's like I could I, if if nothing else, I could get back to them with just the response. This was discussed.
Conversation is ongoing, but it's there's no immediate solution going to be happening anytime soon, but it's at least showing that we are understanding their concerns and moving forwards.
even if it's slowly.
**Mike "Blanch" Blanchard** 24:50 Yeah, I think if we if we just get ready. But I think Raj is back at the end of the month.
That gives us couple months to get it in shape before we need to release for.net. 10. I think there's there's still enough runway.
**Martin Costello** 25:13 Yeah, I think that makes sense. I can look to write something up tomorrow, and I can put it into this issue.
**Mike "Blanch" Blanchard** 25:20 The only reason I'm putting it on Raj is of the Microsoft people. Raj is like in charge of our open telemetry. SDK work.
**Martin Costello** 25:31 That's.
**Mike "Blanch" Blanchard** 25:32 I'm like I'm supposed to be working on like the hotel arrow stuff. I'm not supposed to really be working on.net.
**Martin Costello** 25:41 Oh, no, no, that that's that's fine. It's it's better to get the right person than a person.
**Mike "Blanch" Blanchard** 25:49 Yeah, Raj would definitely be the right person to lead this from the Microsoft side.
**Martin Costello** 25:58 Yeah, I think I think ultimately the out, the outcome. We want to get ideally. I don't know. Septem, September. The latest is, what should we do for 10 and 11, and possibly 12, as a vague plan, and then that can be prepared to be executed for 10 in November.
and then we've got like a a record of what we're gonna do for 11 and 12. So then we don't necessarily have a have an issue in 6 months, or sorry in like a year. Going, hey? You don't use 11 in hotel, but I need you to use 11, and then just have, and then just flip flop between the 2 approaches, depending on. If it's an Sts year and an Lts year.
**Mike "Blanch" Blanchard** 26:46 Are we? Considering the diagnostic source package? In the same way, we're considering the extensions package.
**Martin Costello** 26:56 I think, for the Pr. I was looking at. Yes, because that's that's where the Apis that mean we can't go backwards, came in.
So I guess then there's like an adjunct question to that which is like which is tied into what version to start a framework use. It's just sort of like where do you cause for.net if you keep to the position that the packages should match the runtime? Then, by definition, to use a new feature in 11. You need to run.net. 11.
But we don't have an answer on what we should do aboutnet framework, and I think the answer for that question will then color whether dotnet framework gets to play with new toys or not.
**Mike "Blanch" Blanchard** 27:41 Yeah. Diagnostic source, I think, is the tricky one, because that's like the Api package for open telemetry.
And long before we started bumping the extensions. We always bumped diagnostic source. That was just like fundamental.
Why do we do that? And how it's like.
I mean, a lot of the spec stuff ends up in diagnostic source, you know, new.
And to think of something that's coming in 10 like I don't know.
Schema URL is out there.
**Alan West** 28:20 This is where, understanding the friction a little bit better. Some of these, some of these anecdotes that we've we've gotten over time, because where the friction is coming from is important. If the friction is not or has not been with the diagnostic source package.
then maybe it's okay to proceed in the way that we've been proceeding, at least for that one.
My understanding and it could be wrong is that most of the friction was with the Microsoft Extension packages, which we have also been pumping.
**Mike "Blanch" Blanchard** 28:59 Yeah, those ones.
I mean, they pull in a lot of stuff. So it's just more likely you run into problems.
I have seen problems with just diagnostic source. Because I think it pulls in like compiler unsafe like I've I've run into issues with even that. But they're they're smaller. It's just. It has a tire graph of dependencies.
**Alan West** 29:21 Yeah.
Do you have a sense of that, Martin, for at least the the anecdotes that you've you've come across is the pain coming from diagnostic source?
**Martin Costello** 29:33 I I think my initial hunch on it is. It's coming from the extensions, I think. When I did this Pr, I just looked at everything equally. I didn't treat diagnostic, especially until I discovered that that's where the new Apis had crept in. Not crept, put in. So it it it potentially could be that that one's exempted. And that's like that's always latest. But the others stay in lockstep because I think the average application developers probably doesn't care about the system libraries because they will ship with the runtime that comes with the SDK. And it's the library is the extension stuff that they see cause. That's where you know, like your json config and your dependency injection, and all those things come from.
**Alan West** 30:31 Right.
So if it turns out that the instances where you found that we're using a new Api all stem from diagnostic source, then maybe we. Maybe there still is something useful that we could do in kind of a retroactive sense.
You know, leaving diagnostic source alone, you know, at latest. But see if retroactively we can decrease the version.
Dependency on the extension packages.
**Martin Costello** 31:12 Yeah, I think I think that would maybe even be I have. I have a hunch that if we could could do that.
that would probably make the majority of the people complaining about it happy in my mind.
**Alan West** 31:29 Actually be like a good kind of litmus test for all of this to give us an idea like if it makes.
If we do. This makes people happy. Then I think that would actually lend some confidence in our forward-looking plans.
**Martin Costello** 31:49 Yes, that makes sense. Yes.
**Alan West** 32:03 Yeah, I'd be interested in seeing if that's that's something that is actually feasible in pursuing.
**Martin Costello** 32:11 Okay. What I'll try and do tomorrow, then is I'll try and summarize the the data points and cross references and put them in a comment in the issue that's linked to on that Pr, and then I'll have a go at updating that Pr to undo the change, to tweak, to lower.
I hate confusing myself to like update the Pr on the basis of system. Diagnostics is allowed to always be latest, but the others get pinned and then see what happens.
**Alan West** 32:51 Cool.
Sounds good.
Alright. Well, if we're good on that issue moving on is there?
I can just quickly look over the the Prs with. Y'all, if there's nothing else that folks have that they want to discuss.
Okay.
let's take a quick peek. I actually don't think that there's a lot to discuss that we haven't already kind of talked about or we talked about some of your peers, you know. I'm just kind of sitting on this artifacts output. If that's cool with you.
**Martin Costello** 33:43 Yep, that's fine.
**Alan West** 33:44 For for a little bit.
I know you talked with Raj a little bit, and he had some thoughts or concerns about like the the Ci. I just haven't had. I still haven't had much of a chance to like.
Pay attention to it.
**Martin Costello** 33:57 That's cool.
**Alan West** 34:01 I think most of this other stuff we've talked about. I know there's this. Pr. Thank you, Martin, for jumping in and and reviewing. I I know this person wants a review. My time has been relatively limited.
I will just kind of do a courtesy kind of like, hey? We're here. Sorry.
I'll I'll leave a message on this Pr. Today.
**Martin Costello** 34:32 I was. I was just trying to diffuse their I wanna review. I wanna review. I wanna review.
**Alan West** 34:37 Yeah, yeah, yeah, I appreciate that.
One thing that I noted, though, that I again I have not yet. I still haven't yet looked at this super closely, at one thing that I think may have come or stemmed from potentially some feedback that you provided on this Pr. Martin.
what do I want to bring up like if we pull up these options?
They've added a number of options that like this password option. And maybe this keypad.
These are options that aren't really in. Well, they're not in the spec.
**Martin Costello** 35:26 He has a. This person has it documented here, like the.
**Alan West** 35:30 These these environment variables.
**Martin Costello** 35:34 Oh, yes, sorry. That's yeah. It's my fault. I've forgotten that those are specifically spec driven rather than just convention things to to tweak.
**Alan West** 35:47 Right? So I think I think maybe these top ones are from the spec. I guess we could just pull it up real quick, but like basically the the just. Quickly glancing over this, my feedback to this person is, we need to stay.
We need to stay in the boundaries within the boundaries of the spec. Here the exporter. So so any any of the environment variables that are articulated in this document here are the only ones that we can basically service. So there's like this client certificate.
Option.
Where's the Mtls ones?
Nice? Oh, here it's above.
Oh, it's these 3, basically, these 3 are the ones that this Pr is, I think, meant to address.
So the certificate one, the client key, and the client certificate.
**Martin Costello** 36:55 Yeah, I think for some of those comments I just spoke from knowing that there's related Apis that deal with different formats.
And I was just like, Oh, what about those without.
**Alan West** 37:05 Referring to the spec.
Yeah. Gotcha, yeah, that makes sense.
So I'll probably leave that comment just like, yeah, these are potentially good ideas, but they need to be driven through the spec before we can before we can introduce them.
Beyond that, yeah, I'll I'll I'll try to find the time to to give this Pr. A more proper review.
But it might be a little bit before I can.
Anyways, thanks for thanks for hopping on that, though.
**Martin Costello** 37:43 That's okay.
**Alan West** 37:49 I think that's then most of what to talk about there. If we pop over to the issues looks like maybe there was a couple more open in the last week.
Oh, Martin, this is yours, Github. Attestations.
**Martin Costello** 38:06 This. This is just an idea of of mine. I've done it in other repos, and it's not used here. And I just suggest, like is one of those things that if it's deemed to be a good idea, I'm happy to do it myself.
but I didn't want to just steamroll her in and go, hey? We should use the thing.
**Alan West** 38:26 What is it? What is it?
**Martin Costello** 38:29 Essentially, it's a github built in feature that you can trace where a file, a file you have to where it came from.
So if we're building in Github actions and the files are going from Github actions to Nuget.
you can then get the file out of the new, get packages, the cut as the like. The consumer and go did. Is this file that file?
And then cryptographic stuff in big quotes means you can verify that the file you have in your file. Downloads is the file that was in the build that purports to be where that release came from.
So it's like a sort of a software. Providence supply chain thing.
**Alan West** 39:19 Does it like add data to the individual Dlls, or like metadata.
**Martin Costello** 39:23 No, it the dates is held on Github side.
So you add something to the workflow that builds the artifact to like. Do the attestation, and that goes into Github, and then the tooling is you generate a digest of the file you have, and then you ask, Github, hey, do you know about this digest in this repo? And it'll go. Yeah, sure. It came from here.
**Alan West** 39:48 Gotcha I mean it. It sounds like it's it's pretty non invasive. It sounds like, you know, it could be useful to someone. I don't know if anybody currently desires this, but I certainly not be opposed to the idea.
If it's something that you felt passionate about, or like you or you, or if you know if you have customers that are that are looking for this.
**Martin Costello** 40:24 Not not specifically. It's just something I've sort of been adopting in open source projects is like a sort of I don't wanna say defense in depth. But you you know the sort of the thing I mean, and because I've used it in other places.
and these libraries are starting to come into my sphere of stuff I work on.
I just thought I would suggest the the usage.
**Alan West** 40:50 Sure. Okay, yeah.
Seems okay to me.
**Martin Costello** 41:04 Well in that. In that case, at at some point I will put a Pr together as proof of concept for it, and we can see see from there.
**Alan West** 41:13 Okay, yeah. Sounds good.
See? It looks like this is the other new one.
Anybody responded. No dot net assembly count.
So what are they complaining about that? The service.
the service, name, resource attribute isn't getting dot net assembly account. That must be one of the ones from the instrumentation in the contribury bow, I guess.
**Martin Costello** 42:20 Yeah, I'm not familiar with this one. Specifically.
**Alan West** 42:26 Yeah, sorry I'm looking at this real time with y'all.
I haven't looked at this one myself. They.
in theory it looks like they have things configured correctly.
Looks like they're implementing their own resource detector.
Do you see anything, Wonky? With this usage, Blanche? It's it's not a usage that I'm like that I've personally deployed, but it looks legit.
**Martin Costello** 43:16 It's it says they're using.net 9. And yeah, you're right. This is contrip thing. But for.net 9, it just defers to the runtime.
so either it's a bug on their side, or there's something missing to tell it what the label should be.
Maybe.
**Alan West** 43:39 Yeah.
**Mike "Blanch" Blanchard** 43:42 What is the ask here? They don't want to do this for metrics.
**Alan West** 43:48 Now I think what they're saying.
and maybe maybe maybe we need to clarify with the person. But I think what they're saying based off of the the title of the issue is that.
oh, no, maybe you're right. My 1st interpretation was that service that for whatever reason, service name was not getting injected. But maybe maybe you're right. Maybe they're saying we want to exclude service name or something. Goofy.
**Martin Costello** 44:14 I think I think they want it because the expect the expected result says there's a service name label, but the actual result has no service name, label.
**Mike "Blanch" Blanchard** 44:25 Also they've they've made their own resource detector which set service name to the Assembly name.
But the issue is they've configured that detector at the root.
If they just rewrote that Bootstrap code where they call configure resource for just tracing.
So if they just move that into the with tracing block, then it would.
It would work fine.
So with that top one that's highlighted when you call that.
it essentially just dispatches 3 calls. It just configures the resource for all signals.
That's what the root level one does, but you can call it for the individual signals as well.
Does that make sense.
**Alan West** 45:21 Yeah, I know you can do that.
but I think the thing that I don't quite understand yet is why this, why this method is not working.
**Matthew Hensley / Grafana Labs** 45:35 Looking through this code, it looks like they are wanting Prometheus labels to be promoted. So some resource attributes to be promoted to Prometheus labels.
looking through it correctly.
That might be.
**Alan West** 45:55 Using Prometheus.
**Matthew Hensley / Grafana Labs** 45:57 Yeah. So in that case, Prometheus doesn't promote resource attributes to labels by default. I believe.
That's a Prometheus config setting when ingesting otop.
**Alan West** 46:15 Yeah, I forget if that if that's a configuration option on the exporter itself, or how that's configured.
**Matthew Hensley / Grafana Labs** 46:26 It's configured in Prometheus. Typically cause they're using the otop exporter.
not any of the Prometheus ones. So I'm trying to find this link.
It's been a minute.
**Alan West** 46:40 Actually looks like in this code. They're using a Prometheus exporter for metrics. At least there.
**Mike "Blanch" Blanchard** 46:47 Don't we add resource? If you do like a certain, if you do like the open metrics format.
I seem to recall like there's 2 different formats that Prometheus has based on, like the content type or something. And then one of them, there's no spot for resource.
**Alan West** 47:20 Yeah, that might be right. I'm I'm not.
I don't remember. And also I've never really been super knowledgeable about the the different formats.
**Mike "Blanch" Blanchard** 47:32 That could be an option for this user. If they just switch to the open metrics.
then they'll get resource efficiently like it won't be flattened onto all the records. It has its own spot or something.
It's been a while since I looked at it.
We could go and add an option on the Prometheus exporter to do that flattening.
But do we want that?
So we have a solution with the open metrics, and if I'm not mistaken, the long term Prometheus solution is, it will just receive Otlp.
**Alan West** 48:26 Yeah. And I think Prometheus actually does receive Otlp now it might still be like an experimental like flag that you have to enable or something. But yeah, that's to my knowledge. That's where they're heading.
**Mike "Blanch" Blanchard** 48:40 To me. It doesn't make sense to like.
put in that feature and maintain it forever.
**Alan West** 48:51 Great.
Well, anyways, I think I think this specific issue would. I'd need to repage into my mind.
**Mike "Blanch" Blanchard** 49:01 Stuff about Prometheus.
**Alan West** 49:10 Anyways, I'll probably sit on that issue for for the time being.
**Mike "Blanch" Blanchard** 49:17 Okay, it comes later.
But you know.
**Alan West** 49:25 Jumping over to contribute. I think I think things are relatively quiet there. Peter's back.
it seems, and he's been kind of on top of things here. So I think we're doing all right there and then. I don't normally spend a whole lot of time looking at issues over here in hopes that the the owners are kind of on top of it.
Okay, well, last call anything else any folks want to talk about sounds good.
Talk to you all soon.
