SIG: CI/CD SemConv SIG
Date: 2025-06-26
Duration: 29 minutes
Zoom Recording URL: https://zoom.us/rec/share/fopsJ4W84GPKORI458ItjWB0UfGkAI1dTeVplfXyXwS2gqThztvJ2_fq4F6LdXya.3pH7G5JJhtFjvGcs
============================================================

## Zoom Recording Transcript

**Johannes Koch** 00:13 A wonderful good morning.
**Adriel Perkins** 00:17 Hey? Good day! How are you?
**Johannes Koch** 00:19 I am doing fine.
What about yourself?
**Adriel Perkins** 00:23 Doing? Okay? Thank you.
**Johannes Koch** 00:26 Any any special longer time off, or was it just like one or 2 days.
**Adriel Perkins** 00:33 No, it was actually like almost a whole week. I got sick. So ended up being longer than I expected supposed to just be the like. A long weekend.
**Johannes Koch** 00:48 Yeah, I'm going to summer vacation soon. So, looking forward to that.
**Adriel Perkins** 00:52 Nice, I see. Yes, it's it's really important to have that like mental reset time.
**Johannes Koch** 00:58 Yeah, it's it's gonna be longer than most us people take. So I have 3 weeks this year.
**Adriel Perkins** 01:05 Sweet.
**Johannes Koch** 01:06 It's really cool. Yeah.
So how many people do you usually expect? I think it's not that much right?
**Adriel Perkins** 01:20 Yeah, usually it's just a couple but we're in a odd period of time where not a lot of people are able to attend this and more people want to attend. So what is the survey doing?
It's sitting there.
That's an answer.
**Johannes Koch** 01:43 Yeah.
**Adriel Perkins** 01:43 I need to review it need to figure out where I put it to. What's that survey utility call I use survey.
there you'll find it.
These are all great questions.
hey? Let me pull up survey
**Johannes Koch** 02:12 Question as always.
I think questions are a contribution as well.
**Adriel Perkins** 02:18 Oh, yeah, 100% 100% strap.
**Johannes Koch** 02:23 I really still, I really still struggling how to how to do anything, to be honest. But to be honest, I got distracted and started to build something on my own again. And if you kind of get into that mood, then you forget other things around that right? So.
**Adriel Perkins** 02:42 Yeah, it's it's nice to build stuff. Sometimes. I miss doing it so regularly
**Johannes Koch** 02:50 If.
**Adriel Perkins** 02:50 This is the poll. Thi! This seems to be the best time. However.
I need to talk to Christoph. I need to see if
**Johannes Koch** 03:06 What's his? His role?
**Adriel Perkins** 03:09 So he's he's 1 of the most active people in the Sig. He is helped build a lot of the conventions he used to work with Jenkins quite a bit. I think he was a Maintainer, or at least an active contributor. But he he's a pretty active contributing member to Cicd. He's foundational and getting a lot of the stuff the metrics and conventions through the door, and he's, I think, one of the only people also listed as an approver. But he switched jobs. So after that, that, the timing change and I need to see if we can maybe make this time work.
**Johannes Koch** 03:49 Christoph Kamphaus.
**Adriel Perkins** 03:51 Yes.
**Johannes Koch** 03:56 I think I know him.
I'm just trying to figure out. Where do I know him from?
But I haven't seen him in slack, at least.
whether that's a i don't know. It's just a common.
**Adriel Perkins** 04:10 Yep.
New jobs.
**Johannes Koch** 04:14 That's take away time.
That's why I didn't switch job for 20 years.
**Adriel Perkins** 04:21 Wow!
**Johannes Koch** 04:27 I don't know if that's a good or a bad thing.
Christopher.
**Adriel Perkins** 04:32 It's all in how you view it. It might be a good thing if you view it as a good thing.
The perspective is in the eye of the beholder on this one.
That's correct.
**Johannes Koch** 04:47 Funny.
He he studied in the same university as I did.
**Adriel Perkins** 04:52 Oh, wow!
**Johannes Koch** 04:56 But I can't remember that I saw him.
Our video, by the way, underperformed so far.
**Adriel Perkins** 05:15 I haven't. I haven't looked.
**Johannes Koch** 05:17 No, no, I'm just telling you it underperformed. I expected a little bit more reaction.
**Adriel Perkins** 05:21 Oh, we got it so far.
**Johannes Koch** 05:23 That's okay. Right? It's more like, oh, so so now you're looking at the board right.
**Adriel Perkins** 05:28 Yes.
Still waiting on response for that one. Let's see.
**Johannes Koch** 05:48 Remaining to do.
**Adriel Perkins** 05:51 So this looks like it's waiting for approval.
**Johannes Koch** 05:54 Is this something that you would be reviewing or.
**Adriel Perkins** 05:57 Yeah.
**Johannes Koch** 05:58 Or I could be reviewing as well.
**Adriel Perkins** 06:00 You can review it absolutely.
Anyone. Anyone can review it.
**Johannes Koch** 06:06 Can you ping it to me.
**Adriel Perkins** 06:09 Just that. I don't need to look for it.
Yep, absolutely.
**Johannes Koch** 06:13 But that's the kind of stuff that I can do.
**Adriel Perkins** 06:16 Yup, absolutely giving feedback super super super critical.
The problem.
**Johannes Koch** 06:31 The problem is that you cannot really subscribe to to open telemetry and pull requests being created right? So it's like too much noise.
**Adriel Perkins** 06:41 Yeah, you'd have to do it. If you wanted to do subscribe to it, you'd have to subscribe to it with the area Cicd label.
**Johannes Koch** 06:51 Okay.
**Adriel Perkins** 06:52 Which may or may not be there when the Pr is opened.
**Johannes Koch** 06:57 Okay. Yeah.
**Adriel Perkins** 06:58 You think it's it gets automatically added. So let's see. Alright. So that needs to be reviewed. I'll take a stab at that as well.
he's been waiting a while for that.
This one has been updated.
and this is almost done. I'm still waiting for.
Got 2 pull request reviews.
I need to resolve conflicts. I'll take care of that this morning.
**Johannes Koch** 08:47 how did you get there? I missed that part.
So there's a pull request, how did you get there from which story.
**Adriel Perkins** 08:55 So, adding in var propagator decorator, I went all the way to the bottom, and I went to Dimension this 2 weeks ago and clicked on that pull request.
Oh!
**Johannes Koch** 09:15 This is why I find it confusing that the interface for issues and pull requests is the same.
and that Github trains them the same in the background, but you still get the different number that's.
**Adriel Perkins** 09:28 Hmm.
**Johannes Koch** 09:29 Anyway, I got it.
**Adriel Perkins** 09:33 Cool. Yup. No, that was it took me a while to get used to that.
Okay, so that needs to be reviewed. And I need to make the adjustments Robert mentioned.
**Johannes Koch** 09:52 But this is really just semantics and conventions that we are setting up here right? So.
**Adriel Perkins** 09:59 In which.
**Johannes Koch** 10:00 And and well, it's the specification is the comments that we have over there is like more.
I don't know. It doesn't seem to be technical.
It's more would.
Which is what I'm trying to say. Like.
**Adriel Perkins** 10:17 Yes, it is.
Yeah. So the semantic conventions are the attributes and how you express telemetry. That repo is how your Sdks behave and interact with everything. And so that spec is a lot of words. But it defines all the behaviors and how the SDK is supposed to behave. So that's that specific spec change is supplementary guidance for the sdks. And it's the reason it's I've been working on that as part of this group is in batch systems. It's not possible today to propagate context between processes unless it's over Http headers. But environment variables as the propagator carriers is been long requested, and this group has helped bring that to actually being completed. So now, like you can do open tofu tracing, you can natively. You can like. Github doesn't allow for it right now, but if it if they did, and if it was implemented, you'd actually be able to have trace propagation directly in the runner code for github and get lab so but yes, it's it's word verbiage to define how the sdks behave or the languages behave.
**Johannes Koch** 11:43 Okay, got it?
**Adriel Perkins** 12:44 Yeah, that's definitely a to do.
we need to make a github. Md.
**Johannes Koch** 12:55 Why?
**Adriel Perkins** 12:58 So not every piece of not every attribute that we get out of Github and put in github traces matches, a semantic attribute, also github calls.
**Johannes Koch** 13:17 Got it.
**Adriel Perkins** 13:18 Github workers or workflows what we call Cicd pipelines. And so this is to map what those concepts mean for the general audience, so that when they're like well, what the heck is a Cicd pipeline and github they can say, Oh, it's a github workflow.
**Johannes Koch** 13:38 Got it.
**Adriel Perkins** 13:40 And it's it would just be in addition to the semantic conventions.
**Johannes Koch** 13:47 Stupid thing right? But here's what would help would be so, because there is a help wanted thing added. Now.
**Adriel Perkins** 13:56 Yes.
**Johannes Koch** 13:58 What would help would be.
This is how I would solve it right? So if you already have in mind what needs to be done.
it would be cool to add, like, okay, this would be a pull request for the semantic conventions, because that's where we're going to need to add that Github, Md. Otherwise that I'm not. I'm not into it well enough to understand.
The story is what I'm trying to say.
**Adriel Perkins** 14:28 Okay. Yeah.
**Johannes Koch** 14:29 I'm gonna get there. I'm just saying.
**Adriel Perkins** 14:32 No, no good good call good call. That's end user feedback. Imo.
That is important to have.
**Johannes Koch** 14:42 It's maybe stupid. But I think that's yeah. Anyway. Okay, makes sense now. And now I understand what needs to be done. Right? So.
**Adriel Perkins** 15:17 Yep, no. I wrote that that note down. That's, I think, good information to have and and good things to to do. Basically, it would be copying the way database SIM conf works, and add a github. Md. That maps the 2 concepts together.
**Johannes Koch** 15:34 Okay, that makes sense.
**Adriel Perkins** 15:36 That is here. That's what the database does. Right? So they have, like, technology is defined for aws dynamo.
You click on aws dynamo.
And we would essentially do kind of like a mapping.
**Johannes Koch** 15:54 Okay?
And another very stupid question on the on the Pr. That you linked earlier from Christoph.
Why are we calling it Cicd without a slash in between, because I always use a slash in between. Is that a convention that we have.
**Adriel Perkins** 16:14 The forward slash!
**Johannes Koch** 16:15 Yes.
Sorry.
I just.
**Adriel Perkins** 16:24 No, I'm thinking.
**Johannes Koch** 16:25 48, line 46, line 48, right? I was like, okay, I would comment, okay, I missed the slash, which is like stupid thing, but for me it's a difference.
**Adriel Perkins** 16:40 comment on it.
**Johannes Koch** 16:43 I will. I was just trying to.
**Adriel Perkins** 16:46 Comment on it right.
**Johannes Koch** 16:47 Because I see in the Ci CD matrix in the markdown that already exists, we have a bunch of already, like Ci, where we use the same thing like.
anyway, I'll I'll look at it, make sense.
**Adriel Perkins** 17:01 Yeah, no words are important. Meaning is important. Consistency is important as it relates to semantic conventions. So if if you ask the question, hey? Why aren't we using a forward slash since that's generally how it's referred to in the industry. And should we use that here?
that'd be great my guess. I feel like we might have had this conversation before my memory might be failing me. My guess is that, like we're not putting ci slash CD in the actual attribute names, because that would be a the forward slash would be a problem.
**Johannes Koch** 17:40 True.
**Adriel Perkins** 17:40 But so we might just call it that in in the same place. But you know it, it doesn't hurt to ask that question. I think that's a great question.
**Johannes Koch** 17:49 But you already have used Ci CD. Without the forward slash in all other places, at least in the semantic conventions. Right? So I think the question is already answered, like it doesn't make sense to adjust everything if you already have or other places the other way around.
But anyway, I'll I'll.
**Adriel Perkins** 18:07 Okay.
**Johannes Koch** 18:07 Thank you for explaining that.
**Adriel Perkins** 18:11 Yeah, yeah, no problem. I mean, I I think it's still be good to ask. We can always go make changes to the other places. If if someone feels strongly that it should be ci slash CD
**Johannes Koch** 18:25 I don't feel strongly, but anyway, I'm sorry to disturb you.
**Adriel Perkins** 18:29 No, no, no, no disturbance. You're fine. This is great.
We need feedback. We need. We need different perspectives and different points of thought, it's like, it's good.
Yeah, this is a help wanted. It's not a good 1st issue, but it's a help wanted.
Okay? I think it's did I draft up phase 2 yet.
Excuse me. Hiccups.
I guess I didn't draft up phase 2. 0, I know where I draft. It's it's in a slack message. Okay?
So yeah, I think the key things like, obviously, we're running little Slim. Where did my dot go? Sorry.
And the okay, I think that's all I got.
Is there anything you wanted to talk about?
**Johannes Koch** 21:31 No just lurking to be honest.
**Adriel Perkins** 21:34 Okay.
**Johannes Koch** 21:35 Think there, I think I don't know. We still meet. We still don't have that like as a group. We're going to make something happen feeling. At least that's what I see. I don't know if you had that before.
**Adriel Perkins** 21:48 Yeah, when there was more people we definitely like, you know, I mean, we had more work. We would talk about more things people would want to talk about and more progress we were being made. But with the the time changes and everything, it's been been difficult.
So it's just been doing doing the work, but more silently, less publicly. If that makes sense.
**Johannes Koch** 22:16 Yeah, of course it does.
**Adriel Perkins** 22:20 So yeah, no, it's definitely time for, like a phase 2, which I hope reinvigorates it anyway. So
**Johannes Koch** 22:28 while we're still on this one. Just a quick question like that pull, request that someone brought up on Monday, or whatever that was, let me put that into the chat. This one. This is now something that you would be reviewing because you have been writing the Github receiver.
**Adriel Perkins** 22:45 Yes, I'm a code owner in that.
**Johannes Koch** 22:47 You're the code owner.
And what do you? What are you looking at?
If you go through that.
**Adriel Perkins** 22:55 Well, there's a few different things.
I haven't fully reviewed this yet.
Let's see, I do need to approve these, I think.
Oh, can I not approve them anymore? Shoot?
Cause I'm not a maintainer. That's why.
**Johannes Koch** 23:20 What do you mean?
**Adriel Perkins** 23:21 There's a difference between an improver and a Maintainer.
Maintainers are the only ones able to trigger runs in the work.
**Johannes Koch** 23:30 And you're not. You're not a maintainer anymore for the call.
**Adriel Perkins** 23:34 Never was.
**Johannes Koch** 23:35 You never wear. Okay.
**Adriel Perkins** 23:37 Yeah, it's it's a debt. It's a nuance and and term no onsome term.
But like I'll give you an example when we went to Kubecon. Dot and I submitted our talk the Cncf. Were like, Hey, you're not maintainers. We don't see you listed in the main list of Maintainers for the Open Telemetry Project and the open Telemetry Project Maintainers, the Gc. The Tc. Were like, No, no, no, no! Like like they are. They're maintainers like, that's their job. They're just not maintainers in Github. If that makes sense.
**Johannes Koch** 24:18 It does make sense. Yeah.
**Adriel Perkins** 24:19 So specifically, I mean here a Github Maintainer Maintainer on the in the Github Repo has permission.
**Johannes Koch** 24:28 Has a different permission. Yeah, okay.
**Adriel Perkins** 24:29 Yeah. And I, I'm only approver code owner within the.
**Johannes Koch** 24:35 How do you get Maintainer by reviewing Prs. I guess.
**Adriel Perkins** 24:38 Yes, yes, doing a lot of work, and then someone will nominate you, and then you'll do more work.
This. I I have to I, for I don't, for what I'm looking for. I don't know.
I have to actually grok this this pull request there, but I'll give you a general sense of things. I look for cleanliness, you know, like readability. The usual stuff. Yeah, the usual stuff.
**Johannes Koch** 25:08 But so.
**Adriel Perkins** 25:09 But also.
**Johannes Koch** 25:10 In this case I would be triggered by the 1st 2 imports, like right, because they are adding 2 imports. And this is something that I think you don't want potentially right.
**Adriel Perkins** 25:21 Yeah, I don't. Format. I probably know what those are for.
Yeah, yeah, format, the okay string. That's that's Standard Library. Same with unicode. But why is unicode there?
Oh, that's interesting!
**Johannes Koch** 25:42 Down there.
400.
**Adriel Perkins** 25:45 Yeah.
Yeah. So like this, I'm not. I'm not sure that we should do that.
I'm not. I'm not sure I'm not sure we should enforce to Snake Case. I'm not sure we shouldn't.
But it's it's kind of an odd one like this one I might defer defer to.
How open telemetry as a community has chosen to handle like arbitrary values that people can set whether or not they force them. They kind of try to shoehor them into a convention.
I like, you know.
The thing about some of these attributes is they should be dots.
But obviously like we would have to convert.
I'm not sure it should be 2 2 snakes. So that's something that I have to think about deeply to be able to make an argument for.
and I don't.
**Johannes Koch** 27:02 Sense.
**Adriel Perkins** 27:03 I don't know yet. Obviously, he's got tests here, which is great and it is a smaller change like it's it's essentially just saying like, Hey, let's make sure we support custom properties to attributes in general. We already had support for that. We just didn't have it generalized. We had it as like service.name, etc.
Okay, we'll have to review it, though. I don't.
I can't say that I would review it as part of the Sig.
I just have to review it as part of my normal responsibilities.
but the Sig. Is more than welcome to review it. Anyone is welcome to take a look at pull requests and put a comment on them anyone in the community which I love. How open that is about about about the.
**Johannes Koch** 27:55 Yeah, that's true.
**Adriel Perkins** 27:56 Open symmetry.
Yeah. No good good question anything else.
**Johannes Koch** 28:08 No, no, I'm just as I said, looking and learning and looking at how you could guys organize things and let's see cool. Then I would be dropping if that's okay.
**Adriel Perkins** 28:24 Sounds good.
**Johannes Koch** 28:25 Next week. Is there a call as well? I don't think so right.
**Adriel Perkins** 28:30 Oh, holiday us!
Maybe not.
**Johannes Koch** 28:33 No, I I wasn't remembering if it's every week. So I think if it's next, yeah, it's a around. Okay, then I'll I'll try to be around, and otherwise I'll because I'll be off most of July.
**Adriel Perkins** 28:44 Okay.
**Johannes Koch** 28:46 Then I'll try to be here next week, otherwise I'll see you in August.
**Adriel Perkins** 28:50 Cool, cool. Did you fill out? Yes, you did. Awesome. You filled out the survey.
**Johannes Koch** 28:54 Of course.
Thank you for everything. Thank you for joining. I appreciate it.
