SIG: Security Governance SIG
Date: 2025-06-23
Duration: 32 minutes
Zoom Recording URL: https://zoom.us/rec/share/Xfjdey7DvZqKsTGDO1T_PNvmPh4e00YGSr7JemJzyBY9pc7T8tI-zrzqkrWUZeFP.dIMD65FEAq0LZE8c
============================================================

## Zoom Recording Transcript

**Reiley Yang** 01:00 Hey, Jeremy.
**Jeremy Corley** 01:03 Hey! Hello!
**Reiley Yang** 02:41 Oh, trust!
**Trask Stalnaker** 02:44 Ping!
How are y'all.
**Jeremy Corley** 02:52 Good, good.
**Trask Stalnaker** 03:14 Cool. Shall we start with? I saw you Jeremy, I saw you just push some updates. I haven't looked at them yet.
**Jeremy Corley** 03:27 Yeah, I think, Riley approved. I was just gonna wait till you take a look at the changes I made based on your comments as well. So
yeah.
**Trask Stalnaker** 03:40 If you don't mind, let's just
look quickly. So this was the section was.
oh, did you do a fairly good bit of re, let's see.
**Jeremy Corley** 04:02 Yes, just in that section.
Yeah, because the the original way that it was worded it was
The executable part was saying, if all of these are true.
Do these ced things. And the other one was like, if if any of these are not true, you know it was. It was this weird like, they're backwards from each other. So it was a little bit confusing. So and so I rewrote the
library part. So that looked like the 1st part, and then I made a simplified the bit about
dependencies.
We're dependencies.
**Trask Stalnaker** 04:47 True.
It's not true for Java. Not sorry, maybe. Hold on. I think I got my logic. Reverse does not merely reference.
This is maybe it's it's this is hard to parse.
because we've got a negative here, and then
**Jeremy Corley** 05:22 True. Yes, yes.
**Trask Stalnaker** 05:26 Okay. But we're saying the what it's trying to say is that
Yes, yes, you're saying this is probably true. And so then we have to move on. Yes, yes, okay, I understand. Okay, yes. I like this. I'll leave maybe a suggestion. I'll try to read it again and make a suggestion on wording and approve. Leave an approval
awesome.
**Jeremy Corley** 05:54 Sounds, great.
**Trask Stalnaker** 06:00 What did I add? Here, let's see.
Oh, yeah, yeah. I had seen. I just learned about this that this was a thing that existed.
It has some issues. I where did? Where?
Where is that?
I think? In the Security slam channel is where Eddie Knight had mentioned that this exists
and we were failing. A.
There's clearly some issues with it.
2 factor off.
Oh, yeah, this is for a specific repo. We can look
yeah, like it says we're failing the 2 factor, a multi factor off
but Eddie says that's a known issue. He was trying to convince them to turn this check off because you need a
they. It's not running with a high enough token to do this check so that
give me less excitement about it. Given that
But overall. It's kind of interesting.
I think we've got our hands full right now with the scorecard stuff. But I think this is kinda
a bunch of the just a bunch of the scorecard stuff, anyways, maybe. Oh, no. This is the stuff based on that that privateer
work that he was doing.
And so these are those security framework numbers.
anyway. Just wanted to share. I'm not planning to do anything with that at this point. But maybe
at some point, Riley security.
There was.
**Reiley Yang** 08:21 So I, I saw email notification haven't checked and given that, I've been on both email group of the Tc and the security sake. I still see emails coming to 2 different groups. I wonder if it's time for us to stop the Tc
email groove
and just move here. And I can notify the Tc member who still want to handle those emails
so they can join this group.
**Trask Stalnaker** 08:48 Did the
and come to the Tc. Group, the one that came recently.
**Reiley Yang** 08:59 i i i saw both emails coming like I saw emails coming to both groups during the weekend.
**Trask Stalnaker** 09:09 Why did I miss that?
Let me try to find?
Let me stop sharing.
Let's see, it should be under my Microsoft account.
Yeah.
So let me find that case.
See? You guys, oh.
okay, yeah, I need to fix up my inbox to like flag. Those
**Reiley Yang** 10:20 Okay, yeah, just I fly. If you haven't seen the email, there's something you probably need to fix. And
and we can agree that the right direction is just to move all the security, like the private emails, to this group. Then we should remove the Tca group, and I'll notify the Tc. About this.
**Trask Stalnaker** 10:41 Cool
It was a empty.
**Reiley Yang** 10:46 I haven't checked. I haven't like I I got probably 100 emails this morning. So still going through them.
**Trask Stalnaker** 10:53 Yeah.
**Reiley Yang** 10:54 The security got flagged. So I I got probably like 5 flagged emails. This is why I'm aware of this.
**Trask Stalnaker** 11:03 Yeah.
Think it might have gone to?
Oh, yeah, yeah, okay, yeah. Thanks.
It looks empty. It looks like spam. But yes, I will fix my notifications to for that. That's good.
Biweekly sure seems.
**Reiley Yang** 11:45 So I,
yeah, I feel number one is, if you look at the past like meetings, we don't seem to have packed agenda number 2 is I. I think some of the
the collaborations probably can happen faster if we can sync like on slack, for example, like Jeremy's Pr, we don't have to wait for a weekly meeting, right? So I hope having a bi-weekly meeting will help people to just give up on waiting for the next week meeting, so so they will encourage people just to ping on, slack and move faster.
**Trask Stalnaker** 12:19 I think by week I'm good with bi-weekly. I think it's still good to have at least bi-weekly, because it gives us. I think the meetings are sort of like these Mini deadlines.
**Reiley Yang** 12:29 Function.
**Trask Stalnaker** 12:30 Yeah, exactly.
But cool. I will update the calendar.
And we will cool.
Yeah, next week.
Cool?
yeah, I can share one other thing that I was starting to look at.
I was looking at the the security dashboard and splitting that by specific
topics. That they like the PIN dependencies. And let me pull up what?
Oh, I know I made a little gist out of it, that's what I can share.
So I had it spit out
for each one of those scorecard things.
Basically, any repos that don't have a 10 on it just to kind of look through. See?
what we might do I don't like. It's hard to know
who acquires like the C plus plus gets a 0 but
it's not really a 0. It's just that the Maintainers don't have the company
flag tag company set on their github profile.
So I don't know
how important that is. Really, we already list the company on the community on the readme page for them.
This is kind of interesting. But again, like, I know that
the some of these are not vulnerable. They use a vulnerable pattern, but are very careful to not be vulnerable.
So. But there's no way to override
the score and say, we, you know this is a false, positive
but anyway, some kind of interesting. I'm trying to figure out what I can do with this data. And oh, I know, there was the
update. Oh, yeah, dependency update tool. Yeah. Yeah. So this I noticed injector didn't have
either renovate or depend a bot. So I set them up with renovate on.
Anyway, if I find some interesting stuff to do with that all share.
**Reiley Yang** 16:00 Hey? Trust? I have a quick question. So do you feel like we have a solid understanding about
like? Are we trying to get all the repositories to score 10, or what's the bar? I remember previously. Like as part of the
the the Cncf graduation, it's like we have a curity list like very small, maybe like 6 projects, we want to put a higher bar. And for many other projects, we're saying, Yeah, like, open telemetry is a good place. We welcome people to come and put some initial stuff. It doesn't have to be either meeting any bar except for the code of conduct and those those things so technically like we don't put any bar. But
now, with all the dashboard and ranking here, so do you think like we, we are changing the position by saying, Hey, if you want to create a product under open telemetry, we expect you to get high score here, and if you're maintainers, you fail to keep a good score for a long period of time. Then we're going to kick you out, or we're going to find someone else like, what? What's the position here?
**Trask Stalnaker** 17:09 Yeah, that's essentially why I wanted to look at the breakdown by component. Because I don't wanna base it just on the score.
Because there's too many of the
I'd rather pick some
that we and make a baseline like require like I think I think we should require a dependent dependency update tool?
I think.
We should require
code review. The reason why most of these are not getting tens on code review is because they just don't have enough commits.
And they checked the last 30 commits. And
there's some initial pushes in these repos that didn't have them.
This being different, this one I actually investigated and found that they are doing some maintainer overrides and merging without any review.
So
I want to say, this is required.
With some.
**Jeremy Corley** 18:30 Caveats.
**Trask Stalnaker** 18:32 Oops!
**Reiley Yang** 18:33 It's hard.
**Trask Stalnaker** 18:42 what's another one? I wanna say, actually, want to say that token permissions is required. This is a lot of work to fix, but it
is something that is all. Repos should be able to score 10 out of 10. There's not really any reason.
Pin dependencies, I'd like to say is required.
Yeah,
this is basically Codeql.
tech is, it's gotta be on, gotta be set up in a certain way. So for example, some of these
have Code Ql, but it's not quite set up in the way that this recognizes. So
I'd like to say that Code Ql. Is required, and that this would work. But I'm I'm not quite sure yet.
**Reiley Yang** 19:40 Yeah, for a lot of this. I feel like, once the co-pilot coding agent can
could start to work. We can probably like, let it handle.
**Trask Stalnaker** 19:50 Delegate.
Yeah.
I haven't investigated this one enough. Oh, this one doesn't have a good enough token. But I'm testing that out in
Java. Contrib right now to see if I can fix that
It needs a higher permission.
So what I've done here as worth checking with you all is
created a a github app that has admin. Read permission is the permission required to do this
branch protection check.
And
so it's you know, it's admin. So that's a high, but it's level of permissions, but it's only read so I don't think that
it's I'm not too nervous about it, since it's only
need permission. So I think it's okay. But I
I will open. If I confirm once I confirm that it works
in a community repo issue just to kind of
public like, let people chime in if they have any objection to that.
So yeah, Riley, that's a
basically the I think we're in sync with that. That's the direction that I'd like to go of picking. You know 4 or 5 of these that are required, and that we
tried to get all repos to 10 for those specific ones.
**Reiley Yang** 21:43 Yeah. Thanks.
**Trask Stalnaker** 21:49 How is any that? So the co-pilot we're stuck right now on the easy Cla.
**Reiley Yang** 21:57 Yeah. So the the support folks they reach out to the developers of I'll see that if we can talk to them and understand what's the gap.
**Trask Stalnaker** 22:09 Okay, cause I was. I took a peek at the easy Cla source code on Friday. It
but it looked like from what I could tell, and that's why I didn't understand why.
Let's see easy. CLA.
So, from what I could tell, like a look at the
author id, then the username than the email. And so if they if they find it
and they'll use the author. Id. I don't understand why they even need the email cause. That seems like a fallback thing.
But I obviously don't understand the code cause. If if it's not working still,
**Reiley Yang** 23:09 I had a similar question for them, just waiting for their devs to confirm. Like I, I asked, can they just do a match on the Id.
The email keeps changing right, especially for boss, like every time they change, or at least like if the email like, they still want to keep the email, maybe just like double check or something. They can at least do some pattern matching like the the digits.
the the ticking.
No, it really doesn't matter.
**Trask Stalnaker** 23:39 Yeah, I mean, so the the email
it depends the way that they're getting it is they're getting it from the Github. Commit
rest. Api. They're getting the commit and its pieces.
and so that the author id is validated already. It's not like you can spoof that.
So, yeah, that's my question is, why can't they rely? Why, why do they even look at the email.
Okay, yeah. Yeah. Keep me in the loop on that.
Thought will be really cool to be able to use.
**Reiley Yang** 24:27 Yeah. And so far, so far, the status is as long as the maintainers. They set up the branch protection rule for co-pilot slash like asterisk, then copilot should be able to number one. Review pr, and give them comments. Number 2 is, send Pr and take issue. Fix bugs like that. The only issue is they cannot click the merge button in the end, so that that's already.
**Trask Stalnaker** 24:55 Oh!
**Reiley Yang** 24:56 Helpful and.
**Trask Stalnaker** 24:57 Oh, I see. And I can, yeah, take that.
**Reiley Yang** 25:00 Yeah. So work.
It's really like something they want to merge. They can always like, take the call and start their own.
**Trask Stalnaker** 25:07 Yeah, what is the
There's some get flag to override the existing author with yourself.
Reset author. That's the one.
**Reiley Yang** 25:25 Yeah. So I like, meanwhile, I'm I'm still following up. I like, I just give couple of maintainers heads up. They can try. I want to see if there's any other issue or anything we can learn.
**Trask Stalnaker** 25:37 Cool.
**Jeremy Corley** 25:41 One other thing. Sorry. My, my camera was going in and out. The
on on the security group email. So I I went and looked, and I see that. But when I click into like, see the email it it won't let me see it, because I think that I didn't have a
Google account tied to this email address.
And so it was saying, you know, I can't access the group.
So I quickly created account. But I I don't know if you have to like Re, add me to the
Security group in order for it to recognize my Google account, to let me into the group.
**Trask Stalnaker** 26:21 Let me check.
So did you create, you created a Google account associated.
shaded with your Microsoft email.
**Jeremy Corley** 26:36 Yeah, yeah, exactly.
I just did that because it wasn't there before. Yeah.
**Trask Stalnaker** 26:42 And you used Jay, Corley, or the like.
**Jeremy Corley** 26:47 Yeah.
**Trask Stalnaker** 26:48 The dot. Yes, Jake, okay.
**Jeremy Corley** 26:50 Yeah, yeah, yeah, cause it's interesting. It was sending me the emails. But then.
**Trask Stalnaker** 26:58 It was sending you the emails. Yes, yes, right? That makes sense. It was sending you the emails.
Let me send another test. Email. Because maybe let's see.
you're the At open.
Okay? So it just went out.
I see it in the group.
Let me know when you get it in your email.
**Jeremy Corley** 28:18 Yeah, I noticed when I go to groups in in my account. It says I'm not member of groups yet, and I had to click on something that said, allow administrators to add me to groups and things like that. So
I wonder if, when you originally added me.
**Trask Stalnaker** 28:31 Hmm, okay. Yeah.
**Jeremy Corley** 28:32 I didn't have an account number with the positions.
**Trask Stalnaker** 28:35 Okay, yeah, let me remove and re add you recording.
Okay?
So I've re-added you. Yeah, that's a good point. You should be able to see it. That group in your Google groups
lists. Yeah, just to.
**Jeremy Corley** 29:17 There we go. Yep.
**Trask Stalnaker** 29:18 Sweet.
**Jeremy Corley** 29:21 Yep.
Okay. Yep. Now I can see everything. I'm good.
**Trask Stalnaker** 29:26 Okay.
**Jeremy Corley** 29:26 Thank you.
Oh, one other item, I think.
**Trask Stalnaker** 29:34 Monday.
**Jeremy Corley** 29:35 On a pre. On a previous meeting we had a
Somebody had sent out Tyler Benson in our in the O. Hotel 6 security
**Trask Stalnaker** 29:49 Oh, yeah.
**Jeremy Corley** 29:49 Under slack
and and I think Trasky took a action to respond back to that. I just I just noticed we hadn't responded back to it, so.
**Trask Stalnaker** 29:57 Yeah, yeah. Thanks. What was I going to.
**Jeremy Corley** 30:03 He was asking about whether.
**Trask Stalnaker** 30:05 Where.
**Jeremy Corley** 30:06 To manage their G. Their Gpg. Keys independently, so.
**Trask Stalnaker** 30:11 Yes, yes, thank you. Let me just document
website was our recommendation
cool? Thank you.
**Jeremy Corley** 30:47 Cool alright thanks folks.
**Reiley Yang** 30:51 Thank you. Bye.
**Jeremy Corley** 30:53 Bye-bye.
