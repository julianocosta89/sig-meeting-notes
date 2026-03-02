SIG: Android SIG
Date: 2026-01-06
Duration: 32 minutes
============================================================

## Zoom Recording Transcript

**Mustafa Haddara** 00:41 Good morning.
**Jason Plumb** 00:44 Hey, good morning, Mustafa, how are you?
**Mustafa Haddara** 00:48 I'm good, how are you?
**Jason Plumb** 00:49 And Happy New Year!
**Mustafa Haddara** 00:51 Yeah, Happy New Year. How was your break?
**Jason Plumb** 00:54 It was nice, it's the… I think it's the most consecutive time off I've had in a number of years, which is great.
**Mustafa Haddara** 01:00 Nice.
Nice.
**Jason Plumb** 01:09 Yeah, it'll be interesting to see who shows up today.
we'll figure it out, it's still that, like, half holiday, half not.
Yeah, maybe some people took this week, too, or, you know, even if you didn't take it, there's this thing where you gotta settle back into it, you know?
I feel like yesterday was just a lot of catching up, and…
**Mustafa Haddara** 01:33 Yeah, I joked that I need… I joked that I needed to pull my brain out of deep freeze yesterday.
**Jason Plumb** 01:38 Yeah.
And I didn't finish that catching up, so…
Yeah, I'm behind on reviews, for sure. I see that Jamie has been doing some.
Let's see…
**Mustafa Haddara** 01:54 I have been really bad about that.
Not gonna lie.
**Jason Plumb** 01:59 Yeah, we're backed up. Yeah, I mean, we could always use the help, but I know everyone's busy, so…
**Mustafa Haddara** 02:04 Yeah.
**Jason Plumb** 02:06 Yeah, it would be great to get you or, you know,
Cleverchuck, other people who have been showing up and helping out, you know, on the SIG calls to, like, get in there and do reviews and…
Leave comments, and, you know, it'd be great to get more approvers and triagers even in the mix.
But yeah.
**Mustafa Haddara** 02:27 Absolutely.
**Jason Plumb** 02:29 Okay, so yeah, you can see all the blue here, I haven't even finished these PRs yet…
And it's not… I mean, there's a couple of Dependabot things, but it's mostly just a renovated box.
**Mustafa Haddara** 02:40 mostly extra people.
**Jason Plumb** 02:42 content, oh my gosh. So, it's gonna take some… some time. Hopefully I can do some of that today.
Yeah, this one went stale, but…
Looks like there was new activity on it, let's see.
Unless the stale itself was the new activity, which it was. Okay, cool.
Yeah, anyway,
The only thing that's really on my mind is the 1.0 release, you know, we've been talking about this for months now, and we've had an RC out there, we have that feedback issue, I don't think there's anything new on it, but let's double check.
Swim.
It does not look like it, so…
I think we're pretty much fr… I think we're pretty much good to go. The one thing that is sort of blocking… Hey, good morning, Embrace folks!
**Hanson Ho** 03:42 Hey.
**Jason Plumb** 03:44 The one thing that's blocking is just me not getting around to it in December and needing to circle back on,
creating the…
CI, integration, to be able to publish from a… to be able to do a patch release, basically, from a branch, we don't have that set up yet, we never have done a patch release in Android.
So…
the… the automation, the GitHub actions that, like, check the code out, and do the build, and do the release, that,
expect to just work off of a… a tag. I think there's some additional work that will have to happen when I remove that RC.
to call it 1-0, but I haven't… I haven't looked at it, honestly. So, that's the next step, but I think there's been no additional feedback. I don't see why we wouldn't cut 10 from RC1.
And then move on from there, and then the next release, then, will be 1.1.0, and there's gonna be a ton of changes in that.
So, fun.
**Hanson Ho** 04:45 Thank you.
**Jason Plumb** 04:45 At least we don't have stuff in, like, some…
our C branch that we have to merge back to main. We're just gonna call main…
1-1, because I think there have not been any breaking changes, and keep me honest there, but I haven't seen any yet.
But, as I was saying before you guys joined.
I'm behind, as you can tell. I haven't looked at anything. Like, I looked at a few things yesterday, but it was, like, late, and so…
Hopefully, spend some time today getting caught back up on Android specifically.
**Hanson Ho** 05:16 Yeah, me too. I mean, even Serbi's review, I didn't take a look at. I fully mean to, but I didn't, so…
Back to 3 weeks ago, basically.
**Jason Plumb** 05:26 Yeah, same. And yesterday was my first day back, I don't know about you, but… Yeah. Behind.
And I do see that Jamie has scratched at a few things, that's great, I appreciate that as always, but yeah, we'll ramp back up. I didn't have anything else on the agenda, other than this is what I'm thinking about, and I'm pretty sure there's still some work to be done there, so…
expect a PR from me, and I'm, you know, we might just sit… I'm… I'm… I probably won't.
look at a lot of this honestly until I do the 1-0 work, because I think we just needed to pull that Band-Aid off and do it, so…
Alright, what else is new? I saw… go ahead.
**Hanson Ho** 06:06 Well, do we, do we have the update on whether we want to put in the, the AI, war, not warning, but the, the template to, to basically declare, AI-ness, or, or…
basically tell people, you know, if you're gonna use AI, make sure you filter all the crap, and don't just, like, you know, submit what Claude tells you to, or whatever.
**Jason Plumb** 06:27 Yeah, so I know we talked about it. Did I…
again, it's 3 weeks ago, so I'm fuzzy on this. Did someone do that work? Did you do that work?
Did you finally… No.
**Hanson Ho** 06:39 I also am fuzzy. I might have committed to doing it and not done it, or it could have just not been done.
I have not done it, for sure. I can say that. I'd be surprised if I did.
**Jason Plumb** 06:55 I want to do it, I think,
Do we talk about it here?
**Hanson Ho** 07:03 It doesn't have to be heavy. Like, if we're worried about having, like, 8 sections, 4 of which are required, that requires people filling out, we don't need that. I think it's just, like, here's the blob that you're gonna put there anyway, and here's a small section saying, hey, did you do AI stuff? Or whatever.
**Jason Plumb** 07:18 Yeah, I think I… yeah, we can… we can, bike-shadow what the content should be like. In my brain, it's just like…
It's two boxes, like, did you use…
a generative AI to create this PR. Checkbox, yes. Second box is, did you thoroughly review the output, and are you comfortable submitting this as your own work output?
Or something along those lines. And then, is there anything else you want to tell us about your use of… like, you know, just, like, a third, like.
Please be sure that this is really, like, you're confident this is not…
I don't… I don't want to be mean, but, like, it's not a waste of maintainer time, you know?
**Hanson Ho** 08:00 Well, I mean, just using the last couple that we saw.
**Jason Plumb** 08:04 Yeah.
**Hanson Ho** 08:04 like, don't be like that, and I think… I think.
**Jason Plumb** 08:09 Yeah, I don't know if instrumentation has this yet, let's see…
**Hanson Ho** 08:15 somebody must have something like this, right? This day and age.
**Jason Plumb** 08:20 But even then, it doesn't mean that you…
And find one that's, like, not a normal contributor.
Yeah, this may not. I think Contrib might.
And I could actually look in the GitHub folder, I think that's where it lives.
My issue. PR template, right?
This one.
Yeah.
I thought this had it.
Maybe it didn't get merged yet.
I can find it in my community issue.
No, I can do this. Sorry, I'm still waking up. It's gonna be in here…
It's gonna be in here.
**Hanson Ho** 09:09 Perfect.
30 comments, excellent.
**Jason Plumb** 09:15 Yeah, you know… I think that conversation's closed, but it does link to it, I think.
Let's see…
**Hanson Ho** 09:27 Like, I'd rather go with something, that other repos have done, even if I don't fully agree with it, just for
consistency.
**Jason Plumb** 09:34 Agreed.
the hearer… Yeah, maybe this one.
Okay, it just hadn't been merged yet. Okay, so the one that they're looking… and this is in instrumentation, it basically says…
**Hanson Ho** 09:57 A assistant closure…
**Jason Plumb** 10:02 Yeah, so this is… this is all new. I mean, this is also, like, a little… like…
Yeah, whatever, there was, like, basically no template, and now there's this template, and… here's the checkboxes.
Yes, no, yes.
K… So it's, like, minimal… A lot. I barely used it, or I use it a lot, okay?
That might be confusing.
But I also understand that, like, there's a spectrum of, like, using AI, and what does that mean anymore? Like, it's confusing.
So, I think that's what this is trying to address, which I think it's fine.
**Hanson Ho** 10:37 18 and 19, for me, is almost indistinguishable at this point. I don't really care.
**Jason Plumb** 10:42 Seriously.
**Hanson Ho** 10:42 It's early 20.
**Jason Plumb** 10:45 like, 18, you're like, are you sure? You might have without knowing it.
**Hanson Ho** 10:49 Every… autocomplete is… You know, there's a similar…
**Jason Plumb** 10:55 If yes, have you thoroughly reviewed and understood all of the code?
Yes.
**Hanson Ho** 11:02 This is completely fine with me.
**Jason Plumb** 11:04 Yeah, this is pretty good. I don't know that we need all of this yet, but…
**Hanson Ho** 11:08 No, no, no.
**Jason Plumb** 11:09 But this part, yeah. Okay.
Let me just link to this.
Oops.
**Hanson Ho** 11:15 So, this was added.
**Mustafa Haddara** 11:16 What if we…
like you said, 18 and 19 are basically indistinguishable. What if we reframe the question as, like, did…
AI write substantial parts of this template, or this PR.
Yes, no.
**Hanson Ho** 11:34 Yeah, something like… I mean, I'd go with whatever the, the… in the instrumentation repo, whatever they take, I… I would just, like, directly…
**Mustafa Haddara** 11:45 copy-paste it.
**Hanson Ho** 11:45 Yeah, like, I don't want to diverge from them. I think I prefer what you said, but if they choose to go with this, I'm fine, because the people looking at this, I think, have much more experience dealing with this stuff than I do, so I don't mind deferring.
**Jason Plumb** 12:03 It might be nice to have that consistency between repos, but honestly, like, how many contributors are contributing to lots of hotel repos? I don't know. Like, most people are probably 1 or 2 or 3, and…
Then it's like… You can probably deal with the differences, like…
like, Semantic Conventions is its own beast anyway, and, like, the beast anyway, if you submit PRs there, like, it's not gonna be the same ever.
**Hanson Ho** 12:27 Oh, right, I don't mean consistency as in the same as everything, but more, like, content-wise.
research than me, so…
**Jason Plumb** 12:33 Yeah, I'm totally fine with this.
**Hanson Ho** 12:36 I'm, I'm, I'm…
**Mustafa Haddara** 12:38 Yeah.
**Hanson Ho** 12:38 Subway.
**Jason Plumb** 12:39 As a reviewer, I'd be stoked to see this. It's better than what we have now, which is nothing.
**Hanson Ho** 12:43 Yep.
**Mustafa Haddara** 12:44 Yep.
**Jason Plumb** 12:51 Cool.
I'm sure the, Kotlin donation is still in the brain. It's probably taking up time and energy.
**Hanson Ho** 13:00 Wanna give an update, Jamie?
**Jamie Lynch** 13:03 Yeah, so…
I submitted an issue to create a new repo for that, and I think we selected two initial maintainers and a couple of approvers.
So, if anyone is interested, I will drop the link in the meeting notes.
**Jason Plumb** 13:25 Cool. Thanks.
**Jamie Lynch** 13:27 Yeah.
**Jason Plumb** 13:35 So there were a couple… this one was opened last week, so add location instrumentation. This person's not new.
They've contributed before.
**Hanson Ho** 13:47 Didn't we look at this already for another person to propose this? That requires, additional permission?
Is this an issue, or is this a PR?
**Jason Plumb** 13:59 It's a… it's an issue.
**Hanson Ho** 14:00 Okay.
Feels like a dupe.
**Jason Plumb** 14:04 Yeah, maybe. Do we… do we have another issue around geo?
Oops.
Like, we don't currently provide it, I don't think.
**Hanson Ho** 14:18 No.
**Jason Plumb** 14:20 So I just want to mark this as an enhancement.
And yeah, we would totally need to give some consideration to the additional permissions and what that looks like.
I don't think we would turn that on by default.
that instrumentation.
**Hanson Ho** 14:36 Like, do they want, like, auto instrumentation as an attribute? Geotag everything?
**Jason Plumb** 14:41 They didn't say, but, you know, there's semantic inventions for it.
I don't know that we can get all of this, but we can probably get… Some of it.
**Hanson Ho** 14:52 The problem with this with mobile is that mobile devices move.
so, this becomes… not immutable.
And it's a long…
**Jason Plumb** 15:04 It cannot be on the resource, obviously, but they're talking about tagging telemetry with it.
**Hanson Ho** 15:09 Okay?
**Jason Plumb** 15:11 Which, you know, another approach would be to generate events, right? Like, periodic events when the geo changes or something, right?
**Hanson Ho** 15:19 Yep.
**Jason Plumb** 15:20 Yeah.
**Hanson Ho** 15:21 Something to think about, yeah, cool.
**Jason Plumb** 15:30 Alright, what else is new?
Not much.
Crashed a Java crash. Oh, I didn't see this yet. Same person.
No. This person has two accounts. Oh, they keep doing this. Okay, I've tried to let them know this before, like, they…
They've submitted,
like, PRs from both accounts, and only one of them is signed the CLA, and it's really confusing.
So they want to rename it to Java Crash.
Huh.
**Hanson Ho** 16:02 So, I'm finally, finally getting back on the crash semantic conventions thing. So, when that happens,
This will be a bit more fleshed out, whether they ought to or not to.
be the same thing, or differentiate by metadata. So.
**Jason Plumb** 16:23 Like, I don't think the name should change.
**Hanson Ho** 16:26 I mean.
**Jason Plumb** 16:27 Well, they just want to rename the instrumentation. I see.
**Hanson Ho** 16:31 Oh.
**Jason Plumb** 16:31 Whatever, I don't… that's not important to me.
**Hanson Ho** 16:33 Wait, the module, or…
**Jason Plumb** 16:35 I mean, that's what they're saying, is, like, the name of the instrumentation.
**Hanson Ho** 16:38 Oh, mmm. Okay.
Sure.
Is that even part of the API?
**Jason Plumb** 16:46 I don't… it's not.
**Hanson Ho** 16:47 If we…
**Jason Plumb** 16:49 if and when we build the C++ crash, like the native crash handler, then…
I mean, one option is to build it under the same instrumentation, and have it be a feature of that, or you build it as a separate one with a different name, and maybe that one has a name? Native Crash. I don't… I mean, this seems silly. I don't want to do this.
**Hanson Ho** 17:11 Jamie's comment makes sense, from 3 weeks ago. Yeah.
**Jason Plumb** 17:15 I don't wanna do this.
I'll try and find a nice way of saying I don't want to do this.
Anyway. Okay, well, you know, there's a few issues to go through.
If you have opinions on that, please provide them. Thanks, Jamie, again.
Cool, and then PR is, yeah, I'm super behind.
We all are.
Cool.
Well…
What do you want to do? Do you want to go through these? Do you want to cut it short?
**Hanson Ho** 17:53 Let's cut it short and assume this is, like, catch-up week. We all have reviews to look at, and… Oh, yeah.
**Jason Plumb** 18:01 I'm completely fine with that, like, not dragging it on, if that's cool with everyone else.
**Jamie Lynch** 18:06 Yep, sounds good.
**Hanson Ho** 18:07 Now we've got more AI than ever!
**Jason Plumb** 18:11 So I, you know, I… sorry, so this is my… this is a snarky label that I added, because…
There have been a couple of PRs,
**Hanson Ho** 18:21 Oh, I remember them.
**Jason Plumb** 18:23 Yeah, and they're all very large, and I'm like, I just… I want some way to identify that these…
are created, like, with AI tooling in kind of a…
slop way that doesn't maybe command that much attention until it's really made better, so I just wanted something that calls these out, and…
Yes, it's intentionally snarky.
**Hanson Ho** 18:45 I almost don't care that it's AI. I care that somebody thinks it's a good idea to submit these, whether they created with AI or not, because this is so obviously a person… a people issue who decided to think, hey, this is a good idea, with things that don't… APIs that don't work, instrumentation that does nothing.
**Jason Plumb** 19:03 Yeah.
**Hanson Ho** 19:03 that is… is… that documents nothing. And, like, 2,000 lines of shit, so…
**Jason Plumb** 19:11 Yeah, it's a way to… I don't know, it's a way to easily just roam around GitHub finding stuff to bang on with a big hammer.
So…
**Hanson Ho** 19:20 Who do you think we are that we would merge this? This is… this is incredible. Like, the two I remember is just incredible, like, incredible.
**Jason Plumb** 19:29 I think this one wasn't too bad, this one's ridiculous.
**Hanson Ho** 19:32 Yeah, well, yeah, it's that first one, I don't remember the second one.
**Jason Plumb** 19:35 Yeah, this one is, like, un… Untouchable, really.
**Hanson Ho** 19:38 8,000, goddammit!
**Jason Plumb** 19:41 I know. And we just did some new guidelines, I think we put into the contributing, which was, like, 500, maybe?
But, this one, I think, was not as bad, if I remember it.
Still not tiny.
**Hanson Ho** 19:59 Oof.
Better be tests.
**Jason Plumb** 20:03 Yeah, I don't think…
**Hanson Ho** 20:04 Oh…
**Jason Plumb** 20:07 Yeah, this kind of, like, just being pushy, too, is like, I mean, yeah.
Yeah, here we are again.
Anyway, please leave comments if you have them. Yeah. It's taking some time, you know, as… as we expect.
So hopefully, you know, I like that people are giving the repo attention, they're trying to help, but I think there's a little bit of…
Temperance that might need to be administered by those people?
**Jamie Lynch** 20:42 Is it worth maybe… I, I haven't really…
like, decided to, like, close down those PRs, or be more, like, kind of, like.
a little less forgiving, I guess. Is there a case to be made for doing that, rather than…
Like, pointing out… Smaller things go wrong in hearing feedback.
**Jason Plumb** 21:08 Yeah, that's kind of where I left this one. I…
I… I think I put a block on it…
**Hanson Ho** 21:15 I put a block on it, this is the one I commented on, it's like, this is, like, I can find 3 fatal flaws, this is not, as you said,
There's… this one is, like, trash. This one should be closed completely. I haven't looked at the other one.
**Jason Plumb** 21:32 Yeah, so, I put the block on it when, like, back in early December.
And I was like, this is too big. And then there was a little bit of conversation, and then they came back and they said.
Oh, I didn't see this yet, but they said, hey, is there anything else to change to implement? And I'm like, you know, is there a way that we can move this forward? And I didn't see this yet, but…
**Hanson Ho** 21:55 This is not a big feature, this doesn't work.
The API they're trying to build on does not exist. It's not possible.
To detect data usage via network APIs, there are no network APIs for Android that tells you data usage. It depends on the library you're using. And you can also not detect, usage from other processes. Both of those are fatal flaws for this.
**Jason Plumb** 22:22 Yeah, yeah. So, I mean, to Jamie's question, I'm… like, I'm hesitant to just…
Not hesitant. My instinct is to close this and be like, this is ridiculous. I'm trying to be extra nice about it, because I like the idea of people giving the repo attention and wanting to contribute, and I don't want to give the impression that we're just, like.
a mean, close-knit group of people who don't like outsiders coming in and helping. So, I'm careful about this, but in this particular case, what I'm hoping might happen is that it stalls out and sort of goes away, like, it gets auto-closed.
In a few weeks, but this person still is commenting, so…
**Hanson Ho** 23:08 I'll…
**Jason Plumb** 23:09 They may not see the air of their ways.
**Hanson Ho** 23:13 I will…
**Jason Plumb** 23:14 You know, it's a little more concerning.
**Hanson Ho** 23:16 I will reiterate my comment early… I didn't know that he was gonna update the comments, because I think my… I was trying to be pointed and short with what I said. I will do it again, specifically say, this is impossible. How do you plan to address this?
**Jason Plumb** 23:33 That's good, that would help. And then, you know, it… we can…
I don't mind leaving stuff like this out there for a little while. I mean, I think eventually it will sort of…
Figure itself out. But, you know, if they really do want to keep coming back, and they're very, like, active and excited about it, then yeah, they need to work with us.
And the way that we've suggested to work on this is to do it in smaller chunks, and they're just like, yeah, it'll break system. I don't know what that means.
**Hanson Ho** 23:58 Oh, it doesn't!
**Jason Plumb** 24:00 I don't know what braking system means, but… .
**Hanson Ho** 24:06 They need to work with us on it. I will comment on this today. Ugh, I say this. I will 60%.
Comment on this today.
**Jason Plumb** 24:14 So there's… there's nothing stopping us from closing these, but I just want… collectively, I hope we're just at least giving the impression that we're… we're…
We're nice enough to… at least…
Try and understand what you're doing and help with it.
**Jamie Lynch** 24:28 Yeah.
**Jason Plumb** 24:29 But in this case.
**Jamie Lynch** 24:30 Good.
**Jason Plumb** 24:30 You know, it's kind of a non-starter, probably.
**Jamie Lynch** 24:34 Okay, yeah, that sounds like a good approach to me.
**Jason Plumb** 24:37 Okay.
**Hanson Ho** 24:41 I think if we get more of this in higher volume, frequency, and insistence, I think we're gonna have to pull that lever,
sooner. If it's just this person right now with these two, then maybe we could be a bit more patient. And then we can point back and say, hey, we were patient initially, and then after months of going back and forth.
fundamental points, you know. There's a documented history. If we… if we decide to close that, like, now, I think there's a… there's a documented history of us trying to understand, so…
**Jason Plumb** 25:10 Yeah, let's see. There was another… there's someone else who, like, had a pretty large PR that I think we did end up merging that was AI-generated.
Oh, it was on the…
It was a Docs one, I think. I can find it maybe through… Was it in here?
**Hanson Ho** 25:28 Oh, is it the, yeah, yeah.
**Jason Plumb** 25:32 Yeah.
Yeah, so this was considerably larger than I expected.
**Hanson Ho** 25:44 It's a lot of information on something that doesn't require this much.
**Jason Plumb** 25:46 Yeah, like, this was just… it was kinda too much.
And we can whittle that down, but, like, it was… I think it was pretty clear. There was some back and forth that was like, this is like AI.
At least I thought this was the one.
**Hanson Ho** 26:04 No, there's this one, there's the other one. There's three things in there. Two are written by, I believe, AI, and then the other is written by me, which is…
Very not AI.
**Jason Plumb** 26:15 Okay.
**Hanson Ho** 26:16 So…
**Jason Plumb** 26:21 Was it strict mode?
**Hanson Ho** 26:22 Yeah.
I think, I think…
**Jason Plumb** 26:26 the same.
Yeah, yeah, okay.
**Hanson Ho** 26:27 Yeah, I think it's just one…
**Jason Plumb** 26:33 Yeah, I think that's,
I think they were like, yeah, I use AI, like, they're like, I'm just trying to, like, you know… let's see. They're like, oh yeah, because a non-native English speaker…
**Hanson Ho** 26:46 I'm…
**Jason Plumb** 26:46 you know, tackling a docs issue. Well, first of all.
Is that really what you want to be doing? Which, you know, cool, and you have your friend ChatGPT to help you with this, but this is, like, what we get as output, you know? We just have to know that there's often slop there.
**Hanson Ho** 27:04 I would say, given the state of our documentation, this is… I'm okay with it, as long as the quality gets… as long as what gets generated the other side is reviewed and looks okay, even if a bit verbose and stylistically kind of awkward.
**Jason Plumb** 27:18 Yeah, so we all collectively talked about strict mode a bunch, and we basically said.
you know, we care about… if I can summarize from memory, we care about it, we don't want to intentionally, like, violate strict mode, but if you find strict mode violations, you need to be very careful about filing issues or submitting PRs, because they're not a priority for us.
Like, and this is what we ended up getting, right, is like, you know, a wall of text.
I think what I summarized in hopefully just a few sentences is more concise than what this did.
And I'm just like, I don't know that users or contributors
will read this and understand what our policy and strict mode is. I think that we'll read half of it and get bored and go do something else.
So that's the downside of these kinds of, like, lengthy… Ultra verbose.
Approaches to documentation.
**Hanson Ho** 28:14 Yeah. If you want to look up how to fix strict mode issues, there's plenty of sources online that are more up-to-date.
This… this is gonna…
**Jason Plumb** 28:23 But our stance, right, like, our main thing is, like, Let's see… Yeah, avoidable, optional, acceptable. So…
Yeah, I mean, it's kind of like… Ugh, yeah.
**Hanson Ho** 28:39 See, AI does this… I know. It used to take me 5 hours to write the verbose nonsense that no one reads. Now people can do Jamber in 5 minutes. I mean, I'm offended.
**Jason Plumb** 28:50 Yeah…
**Hanson Ho** 28:54 This is… this is not… this is not a substitute for policy, but it's not, you know… or… to have a proper readable policy, but… whatever. We can always… we can all… all… always trim this down if we… if we feel up to it, so…
**Jason Plumb** 29:09 Yeah.
Yeah, true. I'm curious, just, I don't know, randomly, and again, feel free to drop off. We're not gonna really get… accomplish anything else on this call today.
I just wondered if we have any additional usages, because it seems like people have been paying the repo more attention, at least up to December. I was gonna see if,
If this gives us any data, I think it does it.
Like this, maybe?
Does it have, like… I don't think it gives you any metrics anymore.
**Hanson Ho** 29:50 No.
**Jason Plumb** 29:52 Yeah.
**Hanson Ho** 29:53 It never did, at least not… not useful ones.
**Jason Plumb** 29:56 Well, there's the… There's this thing, right? No. This one.
**Hanson Ho** 30:03 Yeah.
**Jason Plumb** 30:03 Data from this one.
**Hanson Ho** 30:06 Is this about usage, or is this about references, though?
**Jason Plumb** 30:10 Let's find out.
**Hanson Ho** 30:11 Okay, it does say usage, so…
26 usage? How do you count usage?
**Jason Plumb** 30:16 is.
Oh, Google, duh.
Where's our bomb?
I should just pick core and then substitute it for bone.
Right.
Except it's probably spelled OpenTelemetry Android Bomb or something.
Android bomb?
Do I even work here?
whatever, like, core…
**Hanson Ho** 30:50 Yeah.
**Jason Plumb** 30:50 That's what that bomb depends on it, right?
But even then, are there any useful, meaningful numbers in this?
**Hanson Ho** 30:59 Like, what's 3 usage mean?
**Jason Plumb** 31:01 the artifacts.
Used by the.
**Hanson Ho** 31:05 use… usage is, I think, a reference, not actual.
**Jason Plumb** 31:11 Totally.
**Hanson Ho** 31:11 Totally.
**Jason Plumb** 31:13 But, like, even in that list, you see that, like, the Splunk one comes up here.
I was just curious if there are others for, like.
This one? Like, AWS is using it. Okay, that's cool.
Apparently, CoreLogix is also using it. Like, this is Honeycomb's using it.
Right? That's the kind of… interesting data that I don't fully have my head around.
Move, whoever that is.
Tap to pay on Android via Move, that's probably a payment provider.
Anyway, that's… that's, like, cool info, right? Like, I didn't… I didn't know that.
Alright, welcome back. Happy New Year.
**Hanson Ho** 32:01 See you next week when we're all caught up.
**Jason Plumb** 32:03 Yeah, I think it might even be a client SIG week, is it?
**Hanson Ho** 32:08 Oh, I don't know.
**Jason Plumb** 32:10 I have it on my calendar.
Alright, I might see you at 9, otherwise… have a great day!
**Hanson Ho** 32:16 Right.
**Jason Plumb** 32:17 Bye.
