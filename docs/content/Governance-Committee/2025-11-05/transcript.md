SIG: Governance Committee
Date: 2025-11-05
Duration: 28 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 03:31 Hello, Marillia!
**MG Marylia Gutierrez** 03:33 Hello.
**Austin Parker** 03:35 Welcome.
**Trask Stalnaker** 03:35 Welcome!
**Austin Parker** 03:38 Did you see my, rask, did you see my message in the…
DC chat about the Google groups?
**Trask Stalnaker** 03:51 Yes, I don't know exactly what, you want to do there.
**Austin Parker** 03:57 Well, shouldn't… We could be able to…
use Terraform to manage groups, right?
**Trask Stalnaker** 04:06 I'm sure it's possible.
I'm not quite up for… I've got enough Terraform problems still on my plate.
**Austin Parker** 04:17 Okay.
**Trask Stalnaker** 04:18 To get through.
**Austin Parker** 04:19 I… I will take that, I will put that one on the inf… on my infinite backlog then, but I'm pretty sure there's a tariff… I'm pretty sure there's providers for…
Google… Google Workspace.
Is there a problem?
Something wrong? Little tiny fall in the well?
But I think there… yeah, I'm pretty sure there's a provider for G Suite, so what we should be able to do is just have…
Those groups… just add… people can add their email addresses to the…
do the thing, and then we can manage that through Terraform, and then that way, like…
Because I made, like, I made a comment on that doc, because I had a question, but because we're.
**Trask Stalnaker** 05:13 Oh, yeah, there's no…
**Austin Parker** 05:15 Right? There's no way to track who it is other than the Hunter system, which isn't great.
**Tedsuo** 05:19 Yeah. Also, I just… I got caught in a catch-22, where I need to use the Authenticator app to log in to the email that I need
Right, like, it's like… You need to use Authenticator to log in, two-step verification.
But in order to set that up, you need access to the email account.
And the only way to get that is, like, log in. I felt like I was just… I'm caught in some kind of bootstrapping process.
**Austin Parker** 05:54 Yeah.
**Trask Stalnaker** 05:57 That should be solvable, Ted. they're in the, in the 1Password account. I think that's the same problem Marilla just ran into.
Where, in the 1Password account, there's the… the 2FA is stored in password again.
**Tedsuo** 06:14 I see that. Okay, now I see that. I just didn't see it before. I was like, how did I do this in the past?
Okay, thanks.
**Trask Stalnaker** 06:29 Well, welcome, Marillia.
**Alolita Sharma** 06:32 Thank you. Yeah, welcome, welcome. Congratulations to have you. Good to see you.
It's very nice. Are you coming to, Atlanta?
**MG Marylia Gutierrez** 06:45 No, well, not.
**Alolita Sharma** 06:48 I see.
**MG Marylia Gutierrez** 06:50 Staying with me.
**Trask Stalnaker** 06:51 Somewhere much… you look like you're somewhere much better.
**MG Marylia Gutierrez** 06:53 Right now.
Yeah, currently in Brazil for a conference as well, so I'm just, like, at the hotel, so that's why there's a bunch of trees around me, but yeah.
**Alolita Sharma** 07:01 Alright, nice.
**Dan Gomez Blanco** 07:03 I was gonna say, she's got the… she wouldn't have the Zoom background, and that's not a virtual one.
**Alolita Sharma** 07:07 I know, I was like, wow. Very tropical.
**MG Marylia Gutierrez** 07:12 And I don't know if you can hear, but, like, there is a piano at the lobby playing as well, so just, like, I have a whole background here.
**Alolita Sharma** 07:20 Very cool.
Nice place to be.
**Trask Stalnaker** 07:26 So we… Chat, SIG liaison handover?
**Dan Gomez Blanco** 07:33 Yep.
**Alolita Sharma** 07:34 Yeah? So…
**Dan Gomez Blanco** 07:36 Yeah, so I guess, you know, those are the ones, I mean, in the document.
the ones that, I'm currently a liaison for,
So I guess my question was, before I left, is if, you know…
If those should… if Marillia, you know, if you're happy with those, or like, you know, you want to do some reassignment of,
With any of them.
If anyone wants to pick something else.
We can take that offline as well, but I just wanted to bring it up.
**Trask Stalnaker** 08:06 Any… Yeah, the only thought I would have there would be,
the client instrumentation and browser, if Ted…
Wanted, since he's embedded in that already.
**Tedsuo** 08:21 Yeah.
**Alolita Sharma** 08:23 I, I can, Trask and Dan definitely help with the end user, sake, for sure.
**MG Marylia Gutierrez** 08:31 Yeah, the end user, I can take it. I normally talk with People from there often, so…
**Tedsuo** 08:37 If I take… if I take, the client SIG, I might…
I might trade that for one of mine. Let me think about it.
**Alolita Sharma** 08:47 Which ones do you add to? Yeah, yeah, no, no, the proposal wasn't that you just add more. I know.
**Austin Parker** 08:54 Probably… If someone else wanted Erlang, I could take declarative config.
**MG Marylia Gutierrez** 09:02 Well, I was gonna say that I can continue with the Clarity Confed, because I've been joining those calls.
**Austin Parker** 09:06 If you're already doing it, then that's fine, you can…
**MG Marylia Gutierrez** 09:08 Yeah.
**Trask Stalnaker** 09:09 Yeah, basically, Maria, if there's any that you…
would prefer to hand off to somebody, just speak up in the GC channel.
**Alolita Sharma** 09:22 Yeah, yeah.
**Dan Gomez Blanco** 09:22 There's another thing which is, like, meeting times. I mean, these ones are…
are all EU friendly, in general, so.
**Alolita Sharma** 09:30 Yeah, GC meetings are all at this time, so… Should be fine.
But I think, Marillia, you're not in the EU, right? You're in…
**MG Marylia Gutierrez** 09:40 No, I'm Toronto.
**Alolita Sharma** 09:41 Yeah.
**Tedsuo** 09:43 And, and just…
**MG Marylia Gutierrez** 09:44 I'll take a look at it.
**Tedsuo** 09:45 I have a hard stop, at, like, a couple minutes before 5.30. I gotta jet out of here, so apologies for that.
**Trask Stalnaker** 09:57 Cool, we can probably finish that topic up just in chat.
**Alolita Sharma** 10:02 Yeah, Trask, maybe we can look at these…
SIG assignments, you know, again, maybe even if we meet, I'll meet at KubeCon, or right after, and we can figure out, you know, if there's any…
Trading that folks want to do, or anything else, then kind of rebalance.
**MG Marylia Gutierrez** 10:22 Is there a list already somewhere showing the assignments?
**Alolita Sharma** 10:25 Yeah, yeah, there is a list.
**MG Marylia Gutierrez** 10:27 It's…
**Trask Stalnaker** 10:28 In the community repo, in the sigs.yaml.
**MG Marylia Gutierrez** 10:32 Okay.
**Juraci Paixão Kröhling** 10:34 And, go ahead, Trask.
**Trask Stalnaker** 10:39 I was just gonna say that, for rebalancing, like, I would say just everybody look at, you know, if…
**Alolita Sharma** 10:46 I've…
**Trask Stalnaker** 10:47 I've done this before, where, like, I had something that, like, I wanted to trade with Ted or, you know, somebody else, and I just, you know, reached out to them, and I'm like, hey, you know, does this make sense to trade?
**Alolita Sharma** 11:00 Yeah, yeah, makes sense.
**Trask Stalnaker** 11:03 Or if anybody ends up with too many…
Then we can definitely just speak up and chat.
**Juraci Paixão Kröhling** 11:12 Yeah, and, we… for the…
Being a liaison means doing monthly check-ins. You've probably seen my check-ins with the GC, the end user.
I have my way of doing… everybody has their own way, so perhaps, you know, ask Dan, how he typically did the monthly check-ins, but if you are interested, I can check… I can… I can share the way that I do.
Which is…
**MG Marylia Gutierrez** 11:39 Well, I know the way that you do, because you do with me.
**Juraci Paixão Kröhling** 11:42 Exactly.
**MG Marylia Gutierrez** 11:43 the ones that I do, so yeah.
**Juraci Paixão Kröhling** 11:44 Exactly, but then I keep a Google Doc somewhere that is very private to me, so I don't share that with anyone. There, I store all of the comments that you've made for the past, like, year.
Or so. So, I keep track of everything that people said, but I don't keep, mentions to any names. Like, it's very private.
So, and I might anonymize a little bit, and so on. The point is really just to provide the GC with information from the SIG without implicating people there.
But every month, there's a check-in, within all… with all of the Sikhs. And with that, I… we know how healthy it might be.
**Dan Gomez Blanco** 12:26 Yep. In my case, I think, you know, and I think that's been working quite well with the CICD SIG, having a private chat with the…
with the SIG leads, and the TC sponsor there. I've done that with a few of these, and I'll… whoever is picking those up, just let me know, and I'll add you to that. I think, Adriel, for example, from CICD said, like, that he would like to keep his…
I can't… that, you know, that basically the context of that thread and the conversations that happened there.
With whoever is picking this up again, so… Yeah.
I'll… just let me know, and I'll… Oh.
**MG Marylia Gutierrez** 13:02 I don't normally do with just maintainers, or also include, like, approvers?
**Dan Gomez Blanco** 13:08 Normally, I just…
**Trask Stalnaker** 13:09 Maintainers…
**Dan Gomez Blanco** 13:10 Sainers, yeah.
**Alolita Sharma** 13:11 Maintainers, yeah.
**Juraci Paixão Kröhling** 13:14 Same for the check-in channels that we have on Slack. So, again, everyone has their own way of doing things.
I have private channels, which you know, and on those private channels, only the maintainers are there. So, nobody else, and it auto-remes the history after 30 days or so, so it cleans up the history after 30 days. The idea being, we don't want new maintainers to know
To see the previous conversation. Perhaps they were the subject of something before, right? So we… we clean up after 30 days or so.
**Dan Gomez Blanco** 13:48 Makes sense.
Cool.
So I guess, you know, in terms of, like, reassignments and all that, and whatever, like, seg…
you know, check-ins or anything, just… whoever's picking these up, just let me know, and I'll…
loop in. And the other thing that I wanted to raise before I…
Farewell, is, the recent roadmap, changes, that, you know, there was this, basically how everything synced from those,
from the project boards to the issues in the roadmap repo and all that. If you've got any questions about that, be around as well.
But I don't know if, I mean, that's working already. I think the only thing that was missing was…
some dates.
For target dates for some of the projects that are on that board.
If anyone wanted to…
follow up on that, but I guess that's… that's already work in progress anyway. So I don't think there is…
I want you to do that. It should be working.
Cool.
**Trask Stalnaker** 14:56 Alright, should we move on, to Austin's… Topic.
**Austin Parker** 15:04 Yeah, I just… I… Would really appreciate if we could just get approvals on the stability blog.
Even if we're not 100%… I, I, we have gone… I've gone through… Everyone's quite…
sometimes divergent feedback, and I do not think that more time in PR land is going to meaningfully help this. I think the best thing for us to do is to publish it as a statement of intent, and get people talking about it in a discussion that we can turn into OTEPs.
I've really, you know, I think we need to get it out, like, today.
If there are… Absolute drop-dead things that you do not want to go out, then speak your peace, otherwise…
Smash.
**Juraci Paixão Kröhling** 15:56 What?
**Austin Parker** 15:57 Like…
**Juraci Paixão Kröhling** 15:57 I'm a bit I am a bit concerned about, you know, the amount of feedback.
I haven't seen the latest version of the blog, so… so if the blog is significantly different than the version that I reviewed a week or so ago.
Then…
**Austin Parker** 16:12 He's had a lot of changes in the past week.
**Alolita Sharma** 16:13 Yeah, there were a lot of changes. I think Austin's been making them.
**Tedsuo** 16:17 Yeah.
I, I think.
**Juraci Paixão Kröhling** 16:18 the concern?
**Tedsuo** 16:19 We're doing a good job with it, Austin. Yeah. But we are, as we're seeing maintainers and stuff look at it and get kind of spooked at some of the things, like, I do think it's very valuable to get that feedback and, like, nip it in the bud a little bit, even if it is a bunch of paper cuts that I apologize for.
**Austin Parker** 16:37 No, I'm not disagreeing with that. I mean, that's why we are doing it this way, by getting the feedback early, but…
I feel like, at this point, it is…
**Tedsuo** 16:48 Like…
**Austin Parker** 16:48 Unspecific enough about the actual mechanism of some of these changes?
**Alolita Sharma** 16:53 Yeah. That…
**Austin Parker** 16:54 like… I don't know, like, Pavel,
someone found it, or someone… I showed it to someone that was asking about, like, starting a new SIG, and I was just like, well, you know, hey, we're gonna be publishing this thing that kind of says, hey, we should have less new SIGs and focus more on, like, shipping what we already have, and then his immediate thing is like, well, what about, you know.
Like.
If we let it… the longer we let it sit, the, like, worse this is gonna get, so I…
You know, would really appreciate if people could today take, you know, take some time after this call, read through the current version.
If there's stuff that is, like, absolute drop-dead, no, we do not want to say this, then let's fix that.
But otherwise, I think we should…
move it, you know, keep… keep going through the process, because I don't want us to get stuck on this forever.
**Alolita Sharma** 17:52 Yep.
**Juraci Paixão Kröhling** 17:53 So, I'm gonna take a look after this call here. Yeah.
But, I… even without seeing the last version.
the one feeling that I have is, there's been a lot of comments from a lot of people, and I think that's an indication that there is controversy there.
What I think is not controversial is the direction that we are going.
So perhaps a blog post, very short.
Basically saying, we want to get stable. We are going to start new, new efforts, or we're gonna start a…
Which is basically what I said, like, we're gonna start something new so that we don't start anything new, but we are starting a discussion about that. And if you want to join that, here it is. And that's it, like, a very simple blog post, no… not controversial, like, basically saying what we all… what we all can agree on, on the basic words.
I think it is… the problem with the blog post that I reviewed a couple of weeks ago, it's too long.
And it has… it tries to do a lot of things, and because it tries to do a lot of things, it has multiple audiences at the same time, and people who are in conflict with one specific part, like, one technicality of what you've written.
Now, that concern has to be addressed. And I think that's not the point of the blog post. The point is to communicate that we want to get serious about stability.
And and this is it. Like, we are… we are serious now, and that's it. And look at this issue here for a further discussion, and then the discussion can happen there, and then the blog is out.
**Austin Parker** 19:30 Yeah, so… so, respectfully, like, I think having a effectively content-free blog post that says, hey, we're doing something, is not… does not demonstrate a sufficient commitment to doing something. Like…
I think… I don't know about you, but I know, like.
if I go at my job, and I go and say, hey, we should do something about the problems, like, I get a lot of people that are like, yes, we should, and then nothing happens.
And… versus if I go and say, hey, we should submit the problems, and here, like, here's the goals, here's, like, what we're trying… here's why we have the problem, here's my analysis of why we have the problems, here's…
the things that I think we should focus on, and here's, like, specific criteria that we should
used to guide our thinking about it. That, like, that has substance, right? That has meat.
I'm not disagreeing with you that people are going to read this and say, like, oh, I don't like this specific thing. That's great, that's why this is the… starting a discussion, not we're…
Putting all this stuff and saying, this must be how it's done, and, you know.
The thing that I have done over the past week is really edit out a lot of the, hey, here's specifics. It's a much… it is much more…
gauzy in some areas. And it's… there's a lot of changes around, like, being very specific about, like, hey, this… hey, if you're a maintainer, here's the part that's important. If you're an end user, here's the part that's important.
But I…
I can tell, you know, again, the evidence that I have is that if we just put the discussion, if we take all of the stuff that is…
opinionated, and we shove it into a GitHub issue or a discussion, nobody's gonna read it. Except maintainers.
And we will not get the kind of feedback that we need. Like, stuff that exists only in GitHub does not exist for 90% of our end users.
**Alolita Sharma** 21:30 Yeah, that's…
**Austin Parker** 21:31 log in.
**Alolita Sharma** 21:31 That is true.
**Austin Parker** 21:32 we have to reach them.
**Alolita Sharma** 21:34 Yep.
**Juraci Paixão Kröhling** 21:40 I don't think the blog's the right media for that, but I think we're past that point now. I do see the bias-to-action side. I mean, I had a…
a post somewhere, and I was gonna joke that you had the same manager that I had, Tomas Huite, in the past, because he had the same, like.
we don't do anything, like, people do concrete things. When we say we should be doing something, it's never gonna happen.
But it's not what I… what I think this blog post should be. If it's not blog post… I mean, if it's not GitHub, that's fine. It can be somewhere else. But it's not the way that we typically do, which is fine, but,
What I'm not comfortable with is people saying that they have concerns, and then we just say, well, I heard enough, I'm just gonna click the merge button.
I mean, I guess that's not the way.
**Austin Parker** 22:30 I don't… I don't reasonably think you could characterize this…
as that. Like, there's been quite a bit of edits and adjustments based on
the feedback that we've gotten, both directly in the PR, and then also through back channels. So…
Like, I, again…
I'm not saying people can't have complaints or want things changed. What I'm asking for from this group is, let's, you know.
collapse on a decision here. Let's, you know…
We've had this open for 2 weeks.
We need to, you know.
ship the blog post. We need to… we need this to go to the next level of, like, okay.
Everyone that, you know, has had their opportunity to read it, to give feedback, we've made adjustments based on that feedback.
You know, we can't just… Try to build consensus with all 700 people in the org.
in a PR, we have to keep moving forward.
And I'm not saying that we shouldn't keep trying to build consensus, I'm saying that we need to get it into a… we need to continue the process. We need to be able to, like…
Especially given the circumstances.
We need to be able to show that we, as a project, are capable of, you know, hearing feedback.
**Alolita Sharma** 23:59 Yeah, getting feedback.
**Austin Parker** 24:00 Doing things to address that feedback.
**Alolita Sharma** 24:02 Yep.
**Morgan McLean** 24:04 Jurassi, are there specific concerns in the comments that are still active? Like, I was just going through it, I don't see a whole lot of detraction.
**Juraci Paixão Kröhling** 24:12 I don't know. I mean, the last time that I saw, there were some comments that I thought.
**Morgan McLean** 24:16 Okay, I think most of this has been resolved. Yeah, okay.
**Tedsuo** 24:18 This has clean… gotten, cleaned up significantly.
**Juraci Paixão Kröhling** 24:21 Yeah. Okay.
Yeah, I'm gonna take a look.
**Tedsuo** 24:24 Yeah, do another review.
**Morgan McLean** 24:27 I think it might be different than.
**Austin Parker** 24:29 I did just make it one… can we do Trask and then jump to the private topic? Because I assume, Ted, you want to be here for that?
**Tedsuo** 24:38 If… yeah, we better do it right now if we're gonna do that, so… Okay.
**Trask Stalnaker** 24:43 I'll review again. My only concern is that, as others have said, this is, like, it does feel a bit like the GC, like.
setting this, which is not how we've built this community, and not how we've, done hard things. We have done hard things. We've done, you know, the event work, for example, that…
Took a lot of consensus building, and we did eventually say, you know, okay, we're gonna hit the merge button, but we took it slow and brought people along.
And so that's my only concern, but I will… I will read
through it and provide specific feedback today on the… again, another round of reviews, because I've left
several things previously that you have addressed. Thank you.
**Austin Parker** 25:31 Yeah, okay, I will, end and start a Zoom and post it in the…
**Dan Gomez Blanco** 25:38 Yeah, I don't think I'll be joining that one, but okay.
**Alolita Sharma** 25:41 Bye there. Lovely.
**Trask Stalnaker** 25:42 having you on the GC, and we will see you around the community, obviously.
**Alolita Sharma** 25:47 Yes.
Take care, Dan. See you.
**Juraci Paixão Kröhling** 25:50 Thank you.
