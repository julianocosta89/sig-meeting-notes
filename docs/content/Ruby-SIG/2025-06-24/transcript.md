SIG: Ruby SIG
Date: 2025-06-24
Duration: 33 minutes
============================================================

## Zoom Recording Transcript

**Kayla Reopelle** 00:08 Good morning, Hannah.
**Hannah Ramadan** 00:11 Hi! Good morning!
**Kayla Reopelle** 00:14 How's it going.
**Hannah Ramadan** 00:15 It's good.
**Kayla Reopelle** 00:17 Nope.
**Hannah Ramadan** 00:19 Definitely having some June gloom in San Francisco. It's like the weather, says, hazy as the the description.
**Kayla Reopelle** 00:26 Oh, wow!
**Hannah Ramadan** 00:28 Oops!
**Kayla Reopelle** 00:30 Yeah, we had a a little weekend of cold and rainy weather, but it seems to have gone away in Portland now, so I kind of feel like it was a little too short. I could have used a few more days of water for my plants.
**Hannah Ramadan** 00:45 Oh, yes. Okay.
**Kayla Reopelle** 00:47 Does it seem like it? Will. It will end anytime soon.
**Hannah Ramadan** 00:50 I don't know. I feel like this is the like gambling month of like, what are you gonna get like? Who knows.
**Kayla Reopelle** 01:21 My allergy, though my allergies have been killing me, though ever since the rain, I don't know just must have stirred up some pollen or something.
**Hannah Ramadan** 01:30 Yeah, I could see that.
**Kayla Reopelle** 01:34 Wow! Your weather right now is almost the same as a city on the border between Washington State and Canada.
**Hannah Ramadan** 01:44 That's funny.
**Kayla Reopelle** 01:45 Pretty amazing.
**Hannah Ramadan** 01:50 It really is. Sf. Is really its own little like climate.
**Kayla Reopelle** 01:55 Hmm, hey, Chuan?
Alright, let's get going.
Hmm!
Just a second. Gotta get my tabs in order.
Okay, cool alright. So today at the spec sig.
there were a lot of different topics that got covered.
This 1st one is like a pr for us to kind of keep an eye out. For as part of open telemetry. Graduating from an incubating project to a full project there, needs to be some standardization about how we publish who the Maintainers are. And so it sounds like Trask is gonna work on.
some automation to submit Prs to all the repos, to make things look a little more like they do for python.
So expect something like this soon.
The next one. I had a distraction at home, so I didn't really get to hear where this one was at.
Oh, I guess it was merged in so severity. Number 0 can be used to represent an unspecified value which I don't think contradicts with anything that we already have set up for logs.
The next one is that the declarative configuration project is approaching stability.
There was.
There have been some prototypes in various languages that are starting to feel pretty confident.
but the feedback during the meeting was that these implementations haven't really been closely analyzed with the spec to make sure that the implementations are consistent, even though you know there, there are multiple prototypes. So it seems like there's a little more work that needs to be done here before.
The specification will get marked as stable.
A reminder about this Pr about complex attribute values.
I.
yeah, I don't believe this will be a problem with Ruby, but I have not deeply reviewed the Pr. Yet. But if anyone else is interested in reviewing it.
you know, if you, if you have thoughts, maybe about like your back end, being able to support complex values it. It would be worth taking a look, though, I think, given how many approvals there are, it will probably happen regardless.
The entity SDK, working group is making some good progress. They are running into some issues with naming because it sounds like some languages have a resource provider, and they wanted that to be part of the overall scope.
But If you are interested in how entities are getting stored, this is something to keep an eye on an entity is an object associated with produced telemetry. I haven't really read too too much about this, so I'm not sure how it differs from a resource.
So yeah, that's some learning. I still need to do context propagation. I think that that was just like an alert, that the Pr was available.
And then.
Oh, okay. And then there was some talk of new samplers that folks are trying to get off the ground. This one is a probability sampler. So there's I believe that. Yeah, the Otep. It looks like it has been accepted.
so we'll probably see some more implementations of the probability sampler soon.
maybe it's called the composite sampler. I'm not sure what exactly it is, but more samplers that they it sounds like they want to have them in the core libraries rather than contrib. So it's something we should work on eventually.
Yeah, that was pretty much a specs. Anything in there that people want to take a closer look at.
**Hannah Ramadan** 07:38 Nothing for me on that one.
**Kayla Reopelle** 07:43 Cool sounds good.
I found a couple of things. While I was triaging. I'm really behind on my github notifications right now.
this discussion. I I don't remember if we've talked about this in a sig or not, but there was a an issue that Ariel made to, I believe, align the Otlp exporter, compression, default to some of the other languages.
But in the specification. It sounds like, you know, Sigs have some ability to be flexible here.
And it it sounds like the the answer in terms of whether we should change this or not. Was was No, and haven't had any further discussion on it. So my hunch is that we we may just want to like, communicate with the person who opened the Pr. And like, let them know that we're going to keep the current compression or I guess we could bring it back up again in the slack channel and see if people have any thoughts.
Yeah, I just, I feel bad. This person just wanted to contribute something simple and found an issue. And now they've been stuck in this kind of long thought discussion.
So, yeah, I guess. Does anyone have any suggestions about what you think we should do to break this stalemate?
**Hannah Ramadan** 09:45 And the the discussion is on this Pr.
**Kayla Reopelle** 09:48 Yes. Yeah.
**Hannah Ramadan** 09:49 Should probably go click into it. Yeah.
**Kayla Reopelle** 09:50 There's put it in the chat.
kind of like 2 comments, one from Francis and one from Ariel.
**Hannah Ramadan** 10:58 Think I need to like. Yeah, read Ariel's comments and understand what quote unquote. The plea is.
**Kayla Reopelle** 11:05 Bye.
**Hannah Ramadan** 11:05 It sounds like the yeah, the user or the the opener of the Pr, like doesn't really like I mentioned, feel free to close. It was just like looking for a contribution opportunity.
**Kayla Reopelle** 11:27 okay, yeah, so maybe we'll.
**Hannah Ramadan** 11:29 Do you have a do you have an understanding of the Ariel saying, There, I just can't read it that fast.
**Kayla Reopelle** 11:34 Oh, I'm sorry. Yeah. So my my sense of what Arielle is saying is that there's like many other sigs that have chosen a different default. And since. This is a little bit of ad living on my part. But since this environment variable could technically apply across multiple languages.
that having different defaults, then can cause unexpected behavior. So if you like the default in one of the languages, then you just might not set the environment variable at all.
and if we like, until then they would get different. Output right now for Java and Ruby, for example, as 2 2 different languages.
But Francis's point is that they're like users have relied on default compression for a while.
Making this change could erode some trust, and it sounds like there was, since since this part of the spec changed. They decided to change the default to Gzip.
Since from, you know, the team's understanding at that time that would be appropriate for most of the use cases. So it made sense as the default in Ruby.
**Xuan Cao** 13:17 Probably soon.
If the if the spec says.
does that mean that our other language is not one of the stuff.
**Kayla Reopelle** 13:30 Yeah, I guess. I think the spec has like it doesn't really define a default.
Allow implementations to use their own default so it could be anything.
None is the, I guess, documented default. But there are caveats that allow you to not have that as the default, like here.
**Xuan Cao** 14:18 I, I personally prefer default as a gmail. But if there's a better compression algorithm available there.
nomination and send it to the for other other languages, so.
**Kayla Reopelle** 14:39 I guess maybe this would be a good thing to discuss at the spec Sig. And see really just like where people are in terms of having this default like, is it really split down the middle cause? If that's the case, then you know, it probably doesn't matter. But also, I guess. Ask people like if we really want to have defaults for environment variables that cross multiple languages that aren't consistent.
It seems like the 2 options, though, are none. And Gzip. So at least there's only 2 potentials.
But yeah, I'm I am kind of surprised. It does feel like in my mind from different like ruby implementations of instrumentation, like, like new relic uses Gzip by default for compressing our data before we send it. So okay, thank you. That's that's helpful to hear?
So yeah, I guess maybe slack and Spec Sig could be the next steps.
Cool. Okay. So this issue? About like reestablishing a connection on an error came up again.
I do not have the bandwidth to look at this for for a while. But it sounds like I've I've seen this person use multiple signals. So it would be a shame if their company needed to essentially like drop open telemetry because of this problem.
So I just wanted to put it out there to see if anyone was interested in working on this.
But if if not, that's also completely fine and maybe I can encourage this person to help us out.
Okay?
And okay. And then, oh, I owe you an update on the Async metrics. Pr in core.
I only have like a partial review right now. But one thing I noticed that I think would be good to fix before moving forward. Is that We don't have. There aren't any updates to the metrics. Api in this pull request and I believe the Api classes for asynchronous instrument exist, but they don't currently include the observe method.
and generally we have.
you know, some nice like documentation in the Api for people to use, since people are generally calling the Api method so if if you wouldn't mind adding that for the the 3 asynchronous instruments, I think that would be really helpful.
**Xuan Cao** 18:54 Oh, yeah, definitely.
**Kayla Reopelle** 19:00 Yeah, but I'll actually like I can write that in a in a real comment, too. The only other thing I was like working on. I think this looks really good overall.
I'm just trying to better understand, like, how to use asynchronous instruments and need to finish like some, you know, examples that I've been trying to interact with, just to make sure I'm understanding it because the spec doesn't entirely make sense to me. So yeah, I think I think we're super close on this one. And no, yeah.
no strong blockers so far. But I should. I should be able to finish that example today.
**Xuan Cao** 19:52 Since back to the last issue.
So I think we do. We do have a exponential backup for each child. I I mean the exponential.
If if he mentioned the exponential. Pick out time for each trial.
I think, for the pick off function for the support we do have that.
**Kayla Reopelle** 20:12 Okay, yeah, that does sound right?
**Xuan Cao** 20:17 Oh, I can't let me just find them.
but the the other stuff, the the maximum. We tried bounce that one, you know. I think it's a like default 5, and then I'm not. I'm not sure how how you can maybe have another options for people to to sense.
Oh.
For the master. Try.
**Kayla Reopelle** 20:47 Okay.
yeah, the spec, since the spec doesn't describe it.
maybe that's worth trying to get added.
So add.
**Xuan Cao** 21:07 I'm I'm not sure this is one he's talking about. He's done talking about times.
Your account.
**Kayla Reopelle** 21:26 yeah, that does look like an exponential retry.
And yeah, so then the retry count is 5. So I guess whatever your timeout is to the 5th power is as long as the retry would be.
What's that?
That doesn't sound quite.
**Xuan Cao** 21:56 Say, yeah.
**Kayla Reopelle** 21:58 So you'd have. You've had 5 5 cycles of.
**Xuan Cao** 22:02 Yeah, yeah.
**Kayla Reopelle** 22:03 Exponentially.
**Xuan Cao** 22:05 Yeah.
**Kayla Reopelle** 22:07 Okay, thank you for finding that link.
I've got him.
**Xuan Cao** 22:15 But this doesn't really.
Oh, on his request, doesn't really solve the issue about the should we use the Http connections.
**Kayla Reopelle** 22:31 yeah, that is true.
Okay, yeah, it's probably just the closest thing, you could find, interesting, okay, thank you, I appreciate that.
okay, cool, are we? Any more thoughts? Are we ready to move into contribut cool?
Http span name fix oh, yes, thank you for opening this, Hannah? Did you want to talk about it? I forget. Did you add this, or didn't I add this.
**Hannah Ramadan** 24:05 I added it.
But yeah. So we released the Http. Semantic convention stability. Like opt in mode, I think last week for the Http library. Unfortunately, I missed on the like Migration guide at the very bottom. I think if you click on, there's a link in there just for?
So yeah, that should take us to the right place. Yeah. So at the very bottom of this page is the update for how span names should be named for the libraries working on. Essentially it is the route previously it was 8. I think it's the one.
**Kayla Reopelle** 24:53 Wait. I think you mean the the method down here.
**Hannah Ramadan** 24:56 Oh! What did I say?
**Kayla Reopelle** 24:57 The route.
**Hannah Ramadan** 24:58 Oh, yes, yes, sorry. I was probably reading the method. Thank you. Yeah. So basically, it's dropping the Http part of the name and only including the method, so that Pr is just a a follow up to the other work for the spans under the stable conventions, as well as if anyone chooses to do the opt-in mode where they're receiving both attributes for old semantic and new semantic conventions so pretty like easy or like. Hopefully, the Pr, it's really just ripping out that Http string from instrumentation.
**Kayla Reopelle** 25:50 Yeah, I think this.
I think this looks good. Sean, if you have a chance to review this, I would love to reviews before I merge it in But if not, then I can merge it in on Wednesday, if nobody else has reviewed.
**Hannah Ramadan** 26:09 Yeah. And and thank you guys for like reviewing those they're they're long. Prs, just there's just so many.
There's just so much like to look at with these stability. Prs, so I just want to like, Thank you for the extra set of eyes. I think it's usually pretty simple work.
but it is a lot of like details, so I appreciate it.
**Kayla Reopelle** 26:36 Yeah, thank you for taking this on. I did have one idea when I was reviewing the other day to maybe like, make the reviews a little.
A little easier is, I was wondering if you could like add comments around where attributes are set, at least in the dupe and stable sections, so that we can focus on reviewing those. I think that might make it a little simpler if you know where they are, or if it's only in a couple of spots.
**Hannah Ramadan** 27:06 Yeah, I can do that. That is a really good idea. The old the files that are under the old folders usually are, are pretty much just a copy and paste of the original instrumentation, no outside of the module, adding, like the the name change for that at the very top but yeah, let me, I'll add some additional comments. Just to hopefully like guide people through review, because it is a lot and it's not easy to see the changes, because they're all new files.
**Kayla Reopelle** 27:39 Yeah, yeah, that's the bummer about the new files, it's like wait, how can I get diff with the old request, file cool. Thank you. Yeah, that would be a nice experiment, at least for one of them.
**Hannah Ramadan** 27:51 Yeah, let me do that. I think I have 2 other that are open, and I'll go. I'll go through and add comments.
**Kayla Reopelle** 27:57 Cool.
**Xuan Cao** 28:01 So I have a, I have a 2 questions the environment, the environment variable hotel. So if I set this up to Http, does that apply to all?
The client has to be libraries.
**Hannah Ramadan** 28:27 Oh!
**Kayla Reopelle** 28:28 No go ahead, Hannah. Sorry.
**Hannah Ramadan** 28:30 Yeah, yes, it it should. If there's support for it. We're kind of back at one at a time.
**Xuan Cao** 28:36 Okay.
**Hannah Ramadan** 28:36 That should be for all of them.
**Xuan Cao** 28:39 Okay, thanks. Oh, and then are you planning to add those some call frozen right in the future?
**Hannah Ramadan** 28:53 I'm sorry. Can you repeat the question?
**Xuan Cao** 28:55 Oh, for the for the server side! Library in Iraq, Iraq.
**Hannah Ramadan** 29:02 We should talk about that. I actually just noted that yesterday, when I was going through what needs to be done. I think we probably should do server side as well.
that I think that like does fall under, they are omitting currently old attributes. So that should be updated. Yeah.
yeah, there's a lot of places. If you just like search for some of the old Santa convention attributes. They're pretty laced throughout Contrib. So there's some work to do there to get us to stability, for across all of contribs.
**Kayla Reopelle** 29:52 So do you think you want to choose a rack stuff after the Http. Clients.
**Hannah Ramadan** 30:00 I mean, good.
Yeah, yeah.
All of August kind of just having a running.
Thanks.
But yeah, ideally, they're all kind of up to date, and on the same page within, like a a pretty tight timeline. I'd love that definitely. Don't want to have like support for one for like 6 months, and then not get to the chance to like to do another one and make it kind of weird time wise. So I'm hoping to kind of get them all wrapped up kind of in close sequence.
**Kayla Reopelle** 30:49 Oops.
Cool, cool. Yeah, that looks like everything we had on our agenda.
I don't think there's oh, shoot. Okay.
These stale guys need a review.
I guess I've already reviewed this one. I have no memory of it.
I think this is all related to kind of that logging level issue discussion that we had a while back about what level failures to detect resources should be logged at.
Okay? Oh, and then on the 0 code instrumentation. We've been chatting about that one Did you hear from Ariel at all? Did he want to take another?
Oh.
**Xuan Cao** 32:08 I. I sent a message to earlier today. But I you haven't, replied anything but.
**Kayla Reopelle** 32:14 Okay.
**Xuan Cao** 32:15 Oh, let me just wait this until it's okay with you.
**Kayla Reopelle** 32:18 Cool. Sounds good.
Yeah, and if I like miss his review or something, and and you're just waiting on getting it merged, let me know.
Alright. I think that might be everything. I'm just opening up these others to see if there were any new issues.
And it doesn't seem like there are. So yeah, anything else that people want to talk about today.
Cool? Nice. Well, thank you. Guys for coming. Thanks for the discussion and looking at those issues.
yeah, I suppose we will see each other next week.
**Hannah Ramadan** 33:19 Perfect. I'll see you later.
**Xuan Cao** 33:22 Okay.
**Kayla Reopelle** 33:22 Thank you. Bye.
**Hannah Ramadan** 33:23 Right.
