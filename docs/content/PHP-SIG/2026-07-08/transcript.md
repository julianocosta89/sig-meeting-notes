SIG: PHP SIG
Date: 2026-07-08
Duration: 22 minutes
============================================================

## Zoom Recording Transcript

**Pawel Filipczak** 00:38 Hey.
**Chris Lightfoot-Wild** 00:41 Hello.
**Pawel Filipczak** 00:43 How are you doing?
**Chris Lightfoot-Wild** 00:45 I'm not sure I can hear out of his mind Can you hear me?
**Pawel Filipczak** 00:55 Yes, I can.
**Chris Lightfoot-Wild** 00:56 Well, there you go. Sorry.
Bye-bye. You all right.
**Pawel Filipczak** 01:02 Hey, Bob.
**Bob Strecansky** 01:10 Hello, gentlemen.
**Chris Lightfoot-Wild** 01:12 Hey, how you doing?
**Bob Strecansky** 01:15 Pretty good.
**Chris Lightfoot-Wild** 01:16 Very smart in a shirt.
**Bob Strecansky** 01:18 Well, thank you. It was a birthday gift.
**Chris Lightfoot-Wild** 01:22 Did you have a good or did you enjoy your brother's wedding?
**Bob Strecansky** 01:26 Yeah, it was really good. Well, it was mostly good.
We had… the wedding went out… went off without a hitch beautifully, and then one of… My, one of our family members got, had a stroke, so it was good and bad.
**Chris Lightfoot-Wild** 01:39 Laura.
**Bob Strecansky** 01:40 All right, well.
She's recovering. She's recovering. At least my brother and now sister-in-law get to go on their honeymoon. They're going to Fiji. They'.
**Chris Lightfoot-Wild** 01:50 Bye.
**Pawel Filipczak** 01:51 Yeah, okay.
**Chris Lightfoot-Wild** 01:53 Okay, let's close and draw.
**Bob Strecansky** 01:55 I was like, man, can I go with you? I just want to… I'll go.
**Chris Lightfoot-Wild** 01:59 Curve the bugs. Okay.
**Pawel Filipczak** 02:01 Okay.
**Bob Strecansky** 02:02 I'll drive the car. I'll do whatever.
**Chris Lightfoot-Wild** 02:05 Okay.
**Bob Strecansky** 02:06 Yeah, did I miss anything good last week?
**Chris Lightfoot-Wild** 02:10 It's pretty quiet, just the two of us.
**Bob Strecansky** 02:13 Woohoo!
**Chris Lightfoot-Wild** 02:16 Yeah. Nice. Not much.
**Bob Strecansky** 02:18 I'm pulling up the Agenda for today.
Day is the 7. Day is 7, 8.
How did anybody, I know Elastic had some pretty big shuffles recently. How are things going in your org?
**Pawel Filipczak** 02:41 Yeah.
What can I say? I'm still inelastic.
**Bob Strecansky** 02:47 That's right. That's what I had there. I was like, I'm still getting paid. I'm still showing up.
Did you have a lot of co-workers that departed?
**Pawel Filipczak** 02:57 So few people from Poland, but from From our department, there was… Bunch of people who left, yeah, unfortunately.
**Bob Strecansky** 03:08 Come on.
So true.
**Pawel Filipczak** 03:15 What can I say?
Business is business.
**Bob Strecansky** 03:19 Business is business, that's All right. I know we have a couple of agenda topics today, but they're not yet on the board. Do you all have things you want to talk about? Or I can throw some agenda stuff on the board, too.
**Chris Lightfoot-Wild** 03:34 Happy to see what yours are first, I guess. Oh, so…
**Bob Strecansky** 03:38 I was going to, sure, I was gonna talk first about, Jerry's, PHP Auto Instrumentation… Document? Yeah.
**Chris Lightfoot-Wild** 03:49 All right. Yep.
Oh, and that probably actually falls on for the action that I didn't do last week, so I can ask you that here as well.
**Bob Strecansky** 04:00 that… Oh, the, split.
**Chris Lightfoot-Wild** 04:05 Yeah. Well, I did the split, just if it was the right way.
**Bob Strecansky** 04:10 Okay, so I'll talk through the release.
Yes, that's how you spell release, that's correct OK. So let's talk about the Jira's PHP auto instrumentation Docker image. That's this Slack thread.
Here…
**Pawel Filipczak** 04:26 You know.
**Bob Strecansky** 04:28 I think y'all have definitely seen that, but… So… So, yeah.
Jerry mentioned that He had a Docker file in Composer JSON and Telemetry INI.
So are we — yeah, Chris, you had mentioned that they were going to use the instrumentation — we could use the instrumentation repo already for that.
**Chris Lightfoot-Wild** 04:54 Yeah, well, I don't know what, How much overlap there was with.
I guess what Sergey had done in the past.
Okay.
**Bob Strecansky** 05:02 Yes.
Yeah, and also, like, there… we also have other things published in the OTEL PHP repositories, right? For the Git split or whatever. That's… I don't know. To me, I feel like this is, like, the auto-instrumentation is a natural selection fit for that, but…
**Chris Lightfoot-Wild** 05:23 I mean, I couldn't tell if there was some kind of overlap as well, though, with the distro, with the way it injects itself and what it's trying to achieve. But maybe I'm lacking some information about that or understanding.
Mmhm.
**Pawel Filipczak** 05:39 I will ping Sergey to contact him, and maybe they will together figure out how to… How to manage that.
So… It's the… the easiest… The way is to just add the distro there, add the package, and it will just start, right?
You know.
**Chris Lightfoot-Wild** 06:00 So the point of it is to, if you're using Kubernetes, the operator just wires it all up magically, and you don't have to change your own sort of runtime, is that… And is that the spirit of what the distro's supposed to do anyway? So, is that what you're suggesting, I guess?
Hook into the existing distro functionality.
**Pawel Filipczak** 06:21 -H.
**Chris Lightfoot-Wild** 06:22 Cool.
**Bob Strecansky** 06:26 Wonderbar. Okay, so it sounds like we have a path forward there. I tagged Sergey and Palin that I just said.
**Pawel Filipczak** 06:32 No.
**Bob Strecansky** 06:33 Sure.
from Chris, you wanted to talk through your task from last week.
**Chris Lightfoot-Wild** 06:40 Yes, sorry. The Magento stuff, it failed the pipeline on the Git split because the repo didn't exist.
So, I created the repo, But then on packagist, obviously it's not kind of wired up and I didn't know if there was, I didn't know if there was like a process to follow for this or it's supposed to be automatic or because I'm not part of the packagist.
**Bob Strecansky** 07:04 Yeah. Unfortunately, I'm not either. Red is the only one that is. So that's problematic. I emailed them a couple months ago and still have not heard back. I can probably follow up.
**Chris Lightfoot-Wild** 07:17 So does that mean… I guess if it's not auto-wired, we can't make new packages yet, until…
**Bob Strecansky** 07:23 Yeah.
**Chris Lightfoot-Wild** 07:24 Good.
**Bob Strecansky** 07:31 Yeah, so that's what I… I'm surprised that they haven't emailed me back, but I'm also not surpr.
**Chris Lightfoot-Wild** 07:38 Yeah, they've been chasing down those, supplier chain attacks, so, yeah, you're busy.
**Bob Strecansky** 07:44 They are busy.
**Chris Lightfoot-Wild** 07:46 So.
No, I guess that that could lead on for, I don't know if you were wanting to discuss, What's everyone had put in the chat as well with.
That could lead into this kind of thing about, obviously, our lower numbers.
Boom.
**Bob Strecansky** 08:03 Talking about the hotel check-in PHP thing that he talked about today.
**Chris Lightfoot-Wild** 08:08 Yeah, I'd seen the Slack thread, sorry, I didn't know if you wanted to talk about it in here as well, because I think Powell's in that thread as well. Anyway.
**Bob Strecansky** 08:16 Are you talking about the thread in OTEL check in PHP or something else?
**Chris Lightfoot-Wild** 08:20 Yeah, yeah, that one, sorry.
**Bob Strecansky** 08:22 Yeah.
Yeah, we've tried putting out a call for contributors before, and it doesn't work because there are very few people that are interested in both PHP and telemetry and are willing and able to help.
**Chris Lightfoot-Wild** 08:34 Well, I guess it was more, well, certainly trying to get myself and maybe Powell or others.
**Bob Strecansky** 08:41 Oh.
**Chris Lightfoot-Wild** 08:41 It's the packages thing to try and help out with some of that. Obviously not trying to speak on Paul's behalf, but.
**Bob Strecansky** 08:47 Yeah, I've said it before and I'll say it again. You've definitely proven, both of you have proven yourselves as maintainer worthy if you're interested. If you are, that's great. If not, then that's also great.
**Chris Lightfoot-Wild** 08:57 I personally had said previously, I've said to be a contrib maintainer, but I don't mind doing the extra bit, just releasing API SDK, et cetera, if it's just down to you at the second.
**Bob Strecansky** 09:11 Yes.
**Chris Lightfoot-Wild** 09:12 Even if it's a temporary thing until Brett's back, I don.
**Bob Strecansky** 09:15 Sounds like a plan to me.
**Chris Lightfoot-Wild** 09:18 And then I was trying to, Checking with yourself, Powell, on the instrumentation, obviously that's written in C, right? And… There was a PR that we looked at last week, And you seem like the natural sort of candidate to, maybe.
I don't know, sorry, I'm not trying to put words in your mouth, I don'.
**Pawel Filipczak** 09:40 So I was taking a look into one of the PRs from the instrumentation.
And so it was related to the crash with the with span attributes.
And it looks good, but I… I'm still analyzing the code.
**Chris Lightfoot-Wild** 10:01 Mmhm.
**Pawel Filipczak** 10:02 I'm not sure if it if it's If if it can produce any memorabilia.
And… Of course, it will be only limited to the request time, because then the pull is being freed by the PHP, by the Zent engine.
But it will be better not to leak. But in a way, it looks good and it solves the issue. But I have to take a look a bit more deeper.
into that.
**Chris Lightfoot-Wild** 10:29 Yeah, that's obviously cool. And thanks. Thanks for looking. I just wondered if We should.
Follow the other, sort of, repos, and have, like, the approvers group, or whatnot, so if you're part… at least part of that.
**Pawel Filipczak** 10:42 You know.
**Chris Lightfoot-Wild** 10:42 be able to tick and, you know, the green tick rather than the grey tick.
**Pawel Filipczak** 10:46 You know.
**Chris Lightfoot-Wild** 10:46 And.
I don't know.
**Pawel Filipczak** 10:48 I can just do a review and just let you know that, but I don't have any approvals, too.
My word is just… a note is not nothing… it's not meaningful.
So, yeah.
**Chris Lightfoot-Wild** 11:03 Well, I think like Bob said, the more the merrier at the moment. There's sort of only a handful of us.
We keep hitting these bottlenecks, and it feels like recently there's been quite a lot of people coming to Contrib and, you know, throwing, sort of.
Commits forward and.
So staying on top of that is obviously harder, isn't it, when fewer fewer numbers.
**Bob Strecansky** 11:25 Yeah, one is, one is the loneliest number, that's right, for The famous song about that.
**Chris Lightfoot-Wild** 11:33 Yeah, so what do you want to do around that then, Bob? Do you want to obviously continue that discussion in that thread? I mean, I'm happy to obviously say I could…
**Bob Strecansky** 11:40 Yes.
**Chris Lightfoot-Wild** 11:40 Help if necessary, but…
**Bob Strecansky** 11:43 Yeah, that's… I.
**Chris Lightfoot-Wild** 11:44 I don't know the step either.
**Bob Strecansky** 11:46 I have a… I have a note to respond to Severin later. I'll do that.
**Chris Lightfoot-Wild** 11:51 Cool, okay.
**Bob Strecansky** 11:54 Release! I'm planning on doing the release today, hopefully. So, I will get your runtime metrics PR in here, pal, if we can before that, and then we'll release today.
**Pawel Filipczak** 12:04 Mmm.
**Bob Strecansky** 12:04 Do you want to talk to me about runtime metrics P.
**Pawel Filipczak** 12:08 So I created a pull request, and I'm just waiting for the review. Chris and Ivan already get me… gave me a lot of… a lot of faults, and I fixed, so… Oh, I see you, you understand?
**Chris Lightfoot-Wild** 12:23 Sorry, I did one more, sorry.
**Pawel Filipczak** 12:25 Yeah, don't worry, I will take a look.
And, yeah, so… If it will be okay, then it will be ready, I guess, soon for merging.
Yeah, it will lead to the same problem with the split, I guess.
of the of the repo and packages issues.
**Chris Lightfoot-Wild** 12:47 Well, yes, we can create the repository, but… Bob, are you actually able to… so you said Brett's… Brett's, like, the owner of the org, is he? Can you create new packages?
Without Bob, you're Bob, without Brett, or do you have to… Rely on Brett to do that.
**Bob Strecansky** 13:06 Good.
I think, if I remember correctly, I'm looking.
Oh.
Okay.
Let's see if my, packages here… Oh, I must have gotten out of it because I'm a maintainer now. That's good.
That must be a new thing.
Let's see… What did you want? You wanted me to create a new one, Chris?
**Chris Lightfoot-Wild** 13:51 Whatever the Magento 2 one was.
**Bob Strecansky** 13:55 Okay, let's see.
Open to laundry, PG…
**Chris Lightfoot-Wild** 14:01 But equally, I don't Obviously, you want me to be part of that or not, I'm happy not being again, but I don't know what.
**Bob Strecansky** 14:09 Yeah, let.
**Chris Lightfoot-Wild** 14:09 I don't know what remit that sits within, So I'm sure about.
**Bob Strecansky** 14:13 Okay, let's take a look at it really quick Just so that we… where can I… I can find that in the, in .github.
**Chris Lightfoot-Wild** 14:20 Yeah, that's it, yeah.
**Bob Strecansky** 14:22 Oh.
composer, Dodge's song… Talking about, what was it, Magento, you said?
**Chris Lightfoot-Wild** 14:30 Yeah, we're in Well, in that path there'll be another Virtual package name will be in that.
off.
**Bob Strecansky** 14:38 This one.
**Chris Lightfoot-Wild** 14:38 book.
Yeah, yeah, that'll be it.
**Bob Strecansky** 14:42 Let's see if I can create a new one.
Let's see…
**Chris Lightfoot-Wild** 14:50 Oh, after all that, he actually wants the GitHub UI. Yeah.
**Bob Strecansky** 14:54 That would be hotel.php.
Nope, that's not it. What is it? I always forget this. It's.
**Chris Lightfoot-Wild** 15:09 I mean, I guess, did you used to have that then? Is Was that something else.
**Bob Strecansky** 15:12 Oh, this is So, there's a… there's a repo here.
**Chris Lightfoot-Wild** 15:18 Yeah, I managed to make that, and then I could do the git split to fix the pipeline, but I couldn't.
**Bob Strecansky** 15:23 Mmhm.
**Chris Lightfoot-Wild** 15:25 Plug this URL into something else, I guess.
**Bob Strecansky** 15:27 Oh, I see, okay, so you're saying, let's see if I There you go.
**Chris Lightfoot-Wild** 15:45 And then this is about setting up a GitHub. Does that…
**Bob Strecansky** 15:50 Yeah, let's see Let's look at one for another.
And… Let's see… I don't see a GitHub can hear it, y'.
**Chris Lightfoot-Wild** 16:12 Well, on the right under maintainer actions, there's three. Was there only two on the other one? Oh, I just imagined that. Oh, I just imagined it.
**Bob Strecansky** 16:21 Oh, there's two here.
**Chris Lightfoot-Wild** 16:22 It's just where it says set up the GitHub hook. Sorry, I can't get my words up. There was a link on the other package.
**Bob Strecansky** 16:30 Let'.
**Chris Lightfoot-Wild** 16:30 Paste that in.
**Bob Strecansky** 16:33 Package application, package list… Let's see, we must have to set something up in the Magento 2 repo.
**Chris Lightfoot-Wild** 16:51 No.
**Bob Strecansky** 16:52 Oh, it looks like it's… maybe it just doesn't do it on, like, the initial bit or whatever.
Yeah, there we go.
**Chris Lightfoot-Wild** 17:01 Oh, yes, thank you.
**Bob Strecansky** 17:03 -H So, that should be available. So, we can probably try and run that.
We could probably try, and when we publish this, it should publish. We'll try… when I do that, release later, it should work, I would think.
**Chris Lightfoot-Wild** 17:21 Mmhm.
**Bob Strecansky** 17:24 All right.
Cool.
All right. Do y'all want to walk through the board now? Are there other topics that we need to bring up?
**Chris Lightfoot-Wild** 17:49 On the board, huh.
**Bob Strecansky** 17:50 To the board, there was a bunch of new things. And here I saw these two people are blacking away.
So I'll have to look at… these 1, 2, 3, 4, 5 later, and then what I gotta do, I renovate.
Merge at some point here, too.
Look at the… And then control, yeah.
So… A couple in here.
These 3.
So, should we review… I guess we should review these two.
I'm wondering, like, what do y'all think should we get all these Prs that are open now in before we do the release, I guess.
**Chris Lightfoot-Wild** 18:38 When you say they're really, are you doing, what, API and SDK, or are you doing… Because I don'.
**Bob Strecansky** 18:43 Clarity.
**Chris Lightfoot-Wild** 18:44 Entry bonds as well, if necessary.
**Bob Strecansky** 18:46 Yeah, I'll do the API and SDK, and then you can do the contrib ones if you want, Chris.
**Chris Lightfoot-Wild** 18:50 I just don't mind picking them off one by one as I'm, like, trying to get them in, because on some of them as well It's a bit slower, but trying to make sure that the pipeline is not obviously more broken than before.
**Bob Strecansky** 19:02 Yeah.
**Chris Lightfoot-Wild** 19:03 So obviously that would be an amazing thing to still try and have a goal, I guess, to work toward it being green and reliable.
**Bob Strecansky** 19:10 Yeah, we definitely need to…
**Chris Lightfoot-Wild** 19:12 Was it.
**Bob Strecansky** 19:14 Yeah. Are you in this repo, too, or no?
**Chris Lightfoot-Wild** 19:18 Yeah, I'm in.
**Bob Strecansky** 19:20 Okay.
So what we need to do is the, where is that?
Oh.
I guess this is probably gonna be the last thing in here.
Oh, it's in the… Where's that build documentation? One second, let me find it.
There it is.
So in DevTools… We'll do… I'll do this.
So… Yeah, well, I'll coordinate with you on that, Chris, and we can do this release.
**Chris Lightfoot-Wild** 20:24 Mmhm.
**Bob Strecansky** 20:25 I'm gonna make sure that we have all these other PRs merged in first before we do the release, too.
**Chris Lightfoot-Wild** 20:33 Okay.
**Bob Strecansky** 20:36 All right.
Anything else, gents?
**Chris Lightfoot-Wild** 20:40 Yeah, there was a PR in instrumentation as well.
**Bob Strecansky** 20:44 It was, yeah.
**Chris Lightfoot-Wild** 20:45 Did you see that one already? Sorry. I did what?
**Bob Strecansky** 20:48 Which one?
**Chris Lightfoot-Wild** 20:49 Well, I did want… I'd like, maybe, this one's green now, just by adding in that, you know.
The Windows tests are passing the pipeline. If you're okay with that, you can merge that and ask the other author to rebase against it. If it's green, it seems like a legit use case. I think that's the one Powell had checked.
**Bob Strecansky** 21:11 You're talking about this one.
**Pawel Filipczak** 21:12 Tennes.
**Chris Lightfoot-Wild** 21:13 Yeah, so…
**Pawel Filipczak** 21:14 You can approve it.
**Bob Strecansky** 21:20 Wonder.
**Chris Lightfoot-Wild** 21:23 But yeah, if you could I guess if if you won't mind rebasing them.
**Bob Strecansky** 21:38 I don't know Okay.
**Chris Lightfoot-Wild** 21:45 And I guess that if that one goes in… I'm not sure about doing a release for that as well. Bob, if you're able to.
**Pawel Filipczak** 21:54 Yep, yep. So I didn't have enough time to take a look deeper into that, but I will do that today, maybe tomorrow.
**Bob Strecansky** 22:04 Okay. Sounds good.
**Chris Lightfoot-Wild** 22:06 Thank you very much.
**Bob Strecansky** 22:09 No, I can do that, that's fine.
Alright.
Cool.
Other thoughts or feelings.
**Chris Lightfoot-Wild** 22:24 No, I think we'.
**Bob Strecansky** 22:26 All right. Well, I'll catch you all on the Internet.
**Chris Lightfoot-Wild** 22:29 Thanks, Rich. See you later.
**Bob Strecansky** 22:31 Hello.
