SIG: Ruby SIG
Date: 2025-07-15
Duration: 40 minutes
Zoom Recording URL: https://zoom.us/rec/share/JUaNIhO6vLuZzSj8dNyj8QsNZPzNF9N1hd_wQ_LbPOKHTBOpv_poVEdd-uD7x92J.I7azrxq-hOutbVfn
============================================================

## Zoom Recording Transcript

**Xuan Cao** 02:29 Hello!
**Eric Mustin** 02:34 How are you?
**Xuan Cao** 02:36 Goods.
**Eric Mustin** 02:41 I have not been to the meetings in a while.
I assume some folks will join.
**Hannah Ramadan** 02:52 Hi! Everyone.
**Eric Mustin** 02:56 Hello!
**Hannah Ramadan** 03:02 I know Kayla is on her way. She's mentioned. She's having some Internet problems.
**Eric Mustin** 03:16 Cool. No worries. I'll I
I've not been in 6 months or so, but so I don't have any pressing.
**Hannah Ramadan** 03:42 Yeah, we might not have too much today. Anyways, I know Kayla was out at rails Comp. Last week, so I'm sure she's just kind of getting back in the swing of things, too.
**Eric Mustin** 03:56 I am.
I don't know Ariel message me earlier.
Figured he would join. I
Maybe it's firefighting right now, or something.
**Kayla Reopelle** 04:13 Hey, folks, I'm still having some weird Internet problems. But I you're on my phone.
Would someone else be able to share their screen and do the agenda. Since I'm not able to connect on my computer.
**Hannah Ramadan** 04:43 Yeah, I can do that.
**Kayla Reopelle** 04:44 Awesome. Thanks, Hannah.
**Hannah Ramadan** 04:46 Eric, did you say someone else was joining too.
**Eric Mustin** 04:50 No, Arielle had messaged me complaining about
protos recently. So I today. So I assumed he would join. But maybe he's complaining about it in the context of a incident on which he's having to work on or something. So I you know, I'm sure we can get started. I don't. I didn't have a specific agenda item that
you know. I known you wanted to discuss.
**Kayla Reopelle** 05:15 OP.
**Eric Mustin** 05:17 Oh!
**Kayla Reopelle** 05:24 And yeah, I have not caught up on all the like notifications and stuff from the last week. I'm just kind of getting started. So
I don't have any items to discuss right now, either.
**Hannah Ramadan** 05:45 Do we? Wanna look over the specs? I know it kind of classic.
**Kayla Reopelle** 05:49 Sure. Oh, yeah, I I did go to that this morning.
a lot of it was discussion about like
kind of how specs move forward and along.
this measurement processor for metrics may or may not happen.
it's it's kind of similar to span processor. But for individual metrics.
It seems like it has a decent number of approvals. But the the sense was more like in this tentative
happy to test this out in development state, not really sure if we actually need it or not.
**Hannah Ramadan** 06:43 Okay.
**Kayla Reopelle** 06:44 The let's see
what else. So one thing that's important to call out the bottom one, the extending attributes to support complex values that's actually officially getting merged today, if it hasn't been merged already. So
This has been under discussion for a little over a month now.
and or I guess longer than that.
But you know, previously there was kind of some limitation on the values that could be supported by attributes, and people were kind of
shoving things into json strings to accommodate it. But now
now more values can be supported.
and I have not actually
looked at this with Ruby to see if we need to make any adjustments to support this or not.
But but yeah, it's been the topic of a lot of discussion.
**Hannah Ramadan** 07:52 Do when when things like this happen, do
does like a language, go 1st in like their implementation of things, where they would like, kind of say what they needed to do? Or is it kind of like a decision made? And then each agent is responsible for going to figure out
if it affects them, or what changes need to happen.
**Kayla Reopelle** 08:12 So I think a little a little bit of both. When there is
a new specification, I think there is sometimes an implementation attached to it. I don't know if that is a requirement, though but that puts it in development mode, and in order for it to become stable. It needs a few implementations from different languages to make sure that the spec can be understood and that it's repeatable.
but ultimately it's up to. I think each individual language to actually implement it. It's just your timing. If you want to be part of that spec
editing and refining phase, adding that feature, while it's in development, gives you an opportunity to maybe have a little more feedback than when the spec has been marked. Stable
that that's my take on it. But yeah, I don't know if other people have other opinions on it, too.
**Hannah Ramadan** 09:17 Yeah, that makes sense. Seems like, maybe something to
as like a I don't know. Follow up or like ticket to like, make sure we go look at.
**Kayla Reopelle** 09:29 Yeah, yeah, I do think that's an area I know I've been lagging in is actually making issues for the changes to the specification that we need to adopt. I know there's a massive backlog there.
But this would be one thing that I think we should consider working on.
**Eric Mustin** 09:55 Yeah, I
I recently joined elastic and learn that I'll have to
get up to date on the sampling specification that
and some of the changes ongoing there.
So that would be a good
not not specific to ruby just into, you know, learning about their implementation. So
it gets a good, useful, a good use of the time.
**Kayla Reopelle** 10:27 Nice, and congrats on the move to elastic. That's awesome.
**Eric Mustin** 10:33 Thanks. I'm not my official job isn't like it's a architect which is like, maybe. Just fancy consulting. I'm not. I'm still learning what the job is, you know. But but it's so. It's not like open source engineering. But I assume well, some
be able to, you know, I put the meetings back on my calendar and
especially during the onboarding period. I'm not, you know, exactly,
you know, inundated. So I would like to be able to
since I did put this on my resume.
I you know, I guess I ought to do some some country inside. But I I will need to start trying to attend more regularly. But yeah, Hannah, I noticed you have a bunch of the I should
we should put that as a line of mine the stability opt in one, so I can start there and review some of those Prs.
**Hannah Ramadan** 11:25 Yeah.
**Eric Mustin** 11:26 And then, you know, next week I'll ask you guys for help with the sampling stuff.
**Kayla Reopelle** 11:31 Sounds good.
Nice? Yeah. And I think pretty much. The rest of the Prs were just requesting reviews. It was kind of rapid fire and fast. Not a lot of discussion
in the spec sig, so nothing immediately jumped out as something that felt concerning for
Ruby that I would want to like, stop, or interfere with so.
**Hannah Ramadan** 12:01 Okay.
cool, because we can move on
like Sean has something, a pull request to go over.
**Kayla Reopelle** 12:33 Oh, nice!
This is for the exponential bucket histogram.
**Xuan Cao** 12:44 Yeah. So when- when we were in testing do we found some like, really, really big number one, the scale is all over the range cause some issue
in our sites. And then we found out we didn't have a like the check when the rescale starts
to make sure that whenever you rescale, you should
inside those range include, including the the bucket size, should I?
Should have also have a range as well.
So yeah. And then
so for the python and Javascript, they both, through the exception, so they don't say rescue it, and then give a default number. They don't do it. They just so like. In that case, if something happened in the case, then they don't send data at all because it failed.
So I just follow their
their logic. Just sort of the exception.
And once reception it don't, it doesn't break the apps. It just gave the arrow. Yeah.
**Kayla Reopelle** 13:58 Cool. Thank you.
I will take a look at this.
**Xuan Cao** 14:14 Sorry. And then there's another pr, I just, I just opened because I just finished testing today. Is, I think I just opened. Yeah, so that this one is still expensive is like improvements based on the merge
logic.
And the
Oh, wow!
Users start using the cumulative
temporarily. So most of the case, I would say user would prefer use delta.
So they just clean up the data out of the one after the export, but then.
if sometimes they do cumulative, then you will. You probably will create issue because the other sticks again. Still, the issue is related to the scale.
So when they do cumulative, then the scale will be very
well, or jump and jump and jump and down a lot because they store all the data. So that's why one to the community have to have the merge.
Because, we can't guarantee the users collector side. They have the merge logic. So
if they don't have like merge logic in their collector, then
and then they still use them cumulative. Then they will create issue.
So we'll say, Okay, just to add the community. And then
this is a little bit different from the python, even though I, I just copy from Python because our the ruby metric SDK, data structure is different from the python data structure.
It's it's very different because we based on the data points like the hash to do the all the like storing data. But they don't use external
like the hash to store data. They just it's it's very different. So yeah, I haven't checked the Javascript.
I think Javascript is similar to the python.
The reason why I kept using this data structure because it was the 1st time when I 1st to jump into the measures is is there? So I just
do it. It may not be the best, but then the time to
But I mean later on in the future, if people think it's the data structure is not that best, it's just too slow. It costs so many memories. And we definitely need to refactor.
**Eric Mustin** 16:57 Sounds like a cumulative will be a requirement of many organizations.
it's better to just make it work and then worry about making it fast, as you said so
I it's it's awesome to see you continue to work.
Thanks for sharing.
**Hannah Ramadan** 17:45 Okay, do you wanna jump over into contribut.
**Kayla Reopelle** 17:51 Yeah, can we start with the 0 code?
**Xuan Cao** 17:57 This one. I don't have anything. I just I asked Ariel to do another round of a review. But he haven't.
I mean, if maybe like, get up, you can help me to to ask her
to. Yeah.
And that's pretty much pretty much it for the Pr. Event.
**Kayla Reopelle** 18:17 Yeah, I can check in.
**Hannah Ramadan** 18:22 Okay, so just looking for reviews.
**Eric Mustin** 18:38 Yeah, I can. I'll pick up a couple.
I appreciate it's it's like monotonous sometimes to have to do it across all the repos. And
it's not the Http. Implementations are all
you know, layers of tech depth from different times. So it's a the
I can I can. I think I remember a few at least I can chip in on
but I don't. You know I
appreciate the work. It reminded me of something that came up in the slack chat. Actually
that maybe it was worth talking about here at the end. Let me try.
**Kayla Reopelle** 19:25 For the 0 code, Eric, or the is that what you're.
**Eric Mustin** 19:29 Oh, no, sorry. I'll add something to the there was a question that came through the Cncf slack.
**Kayla Reopelle** 19:35 Oh, okay.
**Eric Mustin** 19:36 That just talking about those Prs just for some reason reminded me of I was
got it? Let me grab the link.
Just add it to the agenda.
Bear with me, we can move, you know. I have nothing else to add. Obviously.
**Kayla Reopelle** 19:52 Yeah, think all these? Yeah, some comp issues are are great. I am not sure where the stability is at for those
those like categories of semantic conventions. So we just might want to check them before we
start adding things to make sure we're not
breaking things or kind of mixing too much in terms of stable and unstable conventions.
**Hannah Ramadan** 20:25 Yeah, I don't. I'll look into this stuff, too.
See where these are at.
**Kayla Reopelle** 20:33 I don't know if they're all messaging conventions, but I think some of them are.
**Hannah Ramadan** 20:42 Yeah, like, these aren't.
**Eric Mustin** 20:45 Alright, I'm having trouble finding the comment
which I don't have. I'm not logged into Cnc. Slack on the
my current laptop at work. So I'm juggling my phone with my laptop.
**Hannah Ramadan** 21:05 Yeah, it's kind of like we're like, I recognize these like Net Pyon.
**Kayla Reopelle** 21:09 And.
**Hannah Ramadan** 21:10 As Http. Attributes.
**Kayla Reopelle** 21:13 Which they might apply to both. You know it could be
that's included in the messaging convention as well.
**Hannah Ramadan** 21:20 Yeah.
lot of work with semantic conventions.
**Kayla Reopelle** 21:30 Joy is misaligning our data.
Meaningful requests in the trip.
How's the some kind of stuff? And then, yeah.
**Hannah Ramadan** 21:53 Yeah, I can. I can go ahead and talk about that.
let's see, Eric, do you? Do you know the kind of like strategy we're going for for this. I can also.
**Eric Mustin** 22:03 At a high level. I I think it's like there's a sort of a deprecation path.
But you have to set. And basically the environment variable. And then there's a period of time that elapses.
And then there's some other environment variable setting that needs to be applied or default that occurs, or something along those lines. But besides that, not
really
**Hannah Ramadan** 22:28 Yeah, yeah, that is pretty.
**Eric Mustin** 22:29 Is okay. I know I was. Gonna say, please, feel free to
don't hesitate to explain why I don't know. I I truly haven't. I'm not trying to pretend as though I've been paying attention in the past since the the last meeting, you know. So I'm
I have been absent for 6 months, so.
**Hannah Ramadan** 22:49 Right.
**Eric Mustin** 22:49 The the 5 year old.
I am.
**Hannah Ramadan** 22:51 I just don't wanna go over things if you already had taken a look. But yeah. So just in general, basically totally right on that, like we for migrating from old semantic conventions to new ones, we need to provide people with the option to use old semantic conventions, the new ones or duplicate use both. So each of these Prs
basically has the same exact description here. That kind of goes over that
probably about a year ago. Now, the python team made this did this migration, and the way that they chose to do it was basically adding methods that would check each time an attribute needed to be added if they needed to emit the old new, or both. That was kind of the approach initially, but we got some feedback that maybe that was like kind of heavy to be doing those calls every time.
and so looked for a different way, where we would only have to make that decision one time which which semantic convention we were admitting and that kind of
came. We came up with this pattern of basically looking at the environment burial one time.
Inside instrumentation and making that decision
on startup, and then only patching and requiring the my, the module with not the module.
I guess it is. I think it's modules with the attributes that need to be emitted. So it is because of that.
There's a lot of like duplication
and file creation with each of these Prs. Which do make it kind of hard to to look at. Kayla mentioned that she had been pulling them down and looking at the diffs, making it a bit easier to just double check, to make sure the attributes
that need to be included are, and the ones that aren't are also so. They are like heavy prs to look at, but they are hopefully pretty simple. So like inside these patches, we have 3 new folders.
dupe, old and stable, with the module
and those attributes that need to be added. So it is just kind of a lot of like detailed look, I think, for a lot of these Prs.
But the format between them is exactly the same where we have new folders with dupe, old stable patches.
the instrumentation making that decision on which to require. And then the tests that have been updated
and the way we're keeping that kind of like clean. We were originally finding some, you know. We were like multi patching a lot of the instrumentation because it is so much that we've been using appraisal
kind of like keep those separate. So those are the 3 like big changes that
exist between each of these Prs.
**Eric Mustin** 26:09 And what's the calendar
like in in? Is there a follow on Pr that we have associated with this, or an issue, or something like, how does it close the in 6 months? I don't. I'm actually not.
What's the sort of like road. I don't know what roadmap. What's the roadmap.
**Hannah Ramadan** 26:29 Yeah. So we are required just to keep that bridge open for 6 months. So we're talking about once. All these are done looking at, I guess. Early next year. January. The good part about these types of Prs is, there isn't a follow up right now. But the change. To get us onto the stable. Symmetric conventions is pretty easy. We'd really just come in here and delete
the old and dupe and revert everything except for the stable files.
**Eric Mustin** 27:00 Right makes makes sense. Yeah, I think,
whatever open issue or something. So we don't forget. But yeah, cool. This is really straightforward. Thank you for the
yeah. The the directory structure should. I appreciate the
context, and I'll try to. Whenever take
45 min an hour and work through these. And
you know I I I guess.
I. Every time I talk about these repos I I always am like, Oh, did you see some opportunity for, like, you know, abstracting stuff, or like simplifying in into some shared library? But I'll just avoid going down the rabbit hole for everyone's sake.
**Kayla Reopelle** 27:48 We did. Yeah, we did. Hannah's 1st iteration was,
all abstraction and using that method situation. But it just made it more complicated in the end. Yeah.
**Eric Mustin** 28:00 Yeah, yeah, you'll never. It's the it's fun to never ship
**Kayla Reopelle** 28:04 Yeah, yeah.
**Eric Mustin** 28:05 Yeah, yeah, cool. Yeah. As you can tell, I haven't been here. So it makes.
**Kayla Reopelle** 28:10 Oh, yeah.
**Eric Mustin** 28:11 I I apologize again, for when, Kayla, I think when you joined I I'm the 1st thing we suggested.
Yes, sir.
Why don't you take a look at the dB, or what was it? Yeah, it was like the the dB
share gem, and that just turned into a 2 year time suck or whatever. So I get it.
yeah, these look good to me. Thanks for thanks for the work. Awesome.
**Hannah Ramadan** 28:33 Yeah, of course, I feel like sometimes these things are just like the lesser lesser of evils, like they're all kind of rough. But that's actually just kind of.
**Eric Mustin** 28:42 Just be a maintainer. Sometimes it gets stuff done. It's awesome.
**Hannah Ramadan** 28:46 But it's a good reminder for me. I think. One thing I need to do is create some kind of like notice, or I don't know some
something for people to to be aware that this exists and that changes happening. In 6.
Once, once we're all merged, I need to figure that one out.
**Kayla Reopelle** 29:04 Yeah, I think, yeah, you could start creating companion issues just as an idea you don't. You don't have to do this as we merge in the semantic conventions environment variable opening a new issue. That is like, okay, we're going to remove this and kind of the the relevant date another way that we've
tried communicating things. I don't know how much it actually gets seen, but the Github discussions parts of the repos. That's another place where you could announce things
and the slack channel as well.
Yeah, cause you're thinking right now, you want to pull them all out at once. You don't wanna kind of pull them out based on 6 months for the Individual Library.
**Hannah Ramadan** 29:52 Yes, yeah, I think that'd probably make the most sense.
**Kayla Reopelle** 30:00 Next year.
**Hannah Ramadan** 30:01 Yeah, we have. I mean, like.
**Eric Mustin** 30:04 I've I've heard the slacks going away, so don't I but I'm sure anything is a
is a. It's a it's a tool to, you know. So it's a they're all useful they're all useful tools. And
just a matter of
Yeah. Well,
try to show back up in 6, whatever it is, 6 months, and make sure it's done. It's a weird
it's is there a tracking project or something for the. It's it's a, you know. Maybe there's a spec issue or something, but I don't know. I think it's all. It's all good
strong opinions at all. Obviously, I can't find the other issue I was talking about, by the way, so I I'll just
oh, darn okay, it's it was in the slack. Some guy had a question about sampling, and
I couldn't give him a good answer.
**Hannah Ramadan** 30:57 You know, have tracking ticket as well, actually.
**Kayla Reopelle** 31:02 Yeah, do you have, like all the libraries? Maybe add, Yeah.
everybody's there to check them off.
**Hannah Ramadan** 31:08 Yeah, I hadn't been editing or opening. Okay, so that's
here's the issue. I'm going to.
**Kayla Reopelle** 31:16 Got it.
**Hannah Ramadan** 31:17 Can I?
I'm not sure.
**Kayla Reopelle** 31:19 If you can't, I should be able to. You can just tell me.
oh, it's because I created the issue.
Yeah, okay, I can make it, Hannah, just let me know what you want.
**Hannah Ramadan** 31:31 Okay, that sounds great. I'll send you the info for that. But I agree one tracking ticket would be great. I know python had a similar kind of like.
well, where they had a 1 large ticket and a bunch of little ones. It was quite the project. But yeah.
**Kayla Reopelle** 31:51 So, Eric, yeah, I guess. Is there anything about the sampling issue that you remember that you wanted to chat about?
Oh, I'm I'm jumping ahead, too, I guess. Were there other Pr's, we should look at.
**Eric Mustin** 32:01 It was related to it was similar work that the contrib aws remote whatever that mode, sample.
**Kayla Reopelle** 32:10 Protocol that's being implemented is somebody wanted that for Jaeger.
**Eric Mustin** 32:14 Jaeger is a remote protocol, and at some point it was mentioned as being something that will get done
like in the earth, you know, from some issue from years ago, and it got it
not done for various reasons, probably because nobody uses and so yeah, someone mentioned it, and said they wanted the feature. So whatever like, let's reopen the issue.
**Kayla Reopelle** 32:38 More.
**Eric Mustin** 32:39 Broadly. It seemed like what they could
like. Maybe it wasn't necessary for their specific use cases. Maybe I sort of went down a rabbit hole trying to solution them something, but which didn't.
Then. I was so was sort of like here. Just write a custom sampler
on which you make a sampling decision based on the route they want a route based, or, you know, in a
I think it was like A, you know. Let's call Http target based
sampling ability so they could sample out. I guess some, you know, routes in there, whatever rails app or or I think Sinatra actually. But the sampling decision was being made on the rack span, which was then being enhanced later by the like Sinatra route.
And so in the custom sampler. They were having trouble making sampling rules based on, like the downstream.
what the Sinatra route would be
repopulating the value as of that attribute.
so it actually seemed like enough, I was like, Oh, okay, actually, you know, have rabbit hole in here and can't give you a straightforward answer. And maybe the
thing you want should be supported. So I didn't. I just kind of didn't answer at that point.
**Kayla Reopelle** 33:49 Okay.
**Eric Mustin** 33:50 So, he commented on one of these issues. But I'll find it when I can. Not multitask, I guess, and I'll just I just have to log in. I, I have a new computer
humble break. So IA new background is, and yeah, yeah.
So oh, yeah, there's all sorts of fun, sense and so I just need to set up some of the other slack you know, slack things on here.
**Kayla Reopelle** 34:14 Cool. Yeah.
**Eric Mustin** 34:15 I'll share it in the yeah. I'll share the link when I get it.
**Kayla Reopelle** 34:18 Cool.
**Eric Mustin** 34:20 You know. In the
at least, I'll find the related issue. I think, he commented on an issue on
one of these. But
anyway.
I don't have we, you know, I don't have anything relevant that we need to get, you know. Take up
20 min of meeting time to to discuss on it. I just was.
It occurred to me that you know, the bug reports thing it kind of was like a bug report. Maybe.
I don't know.
**Kayla Reopelle** 34:55 So.
**Eric Mustin** 34:56 That's all I got there the remote sampling. Is that no,
I wasn't prepared ahead of time. I apologize, guys.
**Kayla Reopelle** 35:07 Yeah, that's all good.
This is a very chill meeting. So any anything, anytime?
Yes, I
and I must have just intellectually reviewed this and not literally hit the button, so I should go back and take another look. Thanks for putting this one out.
**Eric Mustin** 35:32 Oh, yeah, I think this guy had commented recently, asking for.
**Kayla Reopelle** 35:36 Okay. Oh, yeah.
**Eric Mustin** 35:37 There's some interest.
**Kayla Reopelle** 35:39 Oh, nice requesting review. I think that person has reviewed other Prs related to this, and they're in aws.
**Eric Mustin** 35:48 I?
yeah, it's a you know, for what it's worth. I'm trying to also mention to the folks internally who do contribute to open telemetry here to
try to provide some more resources to, you know, at least support contrib more seriously.
**Kayla Reopelle** 36:08 Seriously.
**Eric Mustin** 36:10 So hopefully I can get
But I I won't pretend to have any context on using aws remote remote sampling.
But it. It would be nice if it seems like there's a little bit of cognitive dissonance
between what was like. Sort of like to sampling strategies from 5 years ago.
Where they were sort of having agents communicate.
You know, these updates to sdks and apps with
open telemetry is now sort of like standard or like future path, seems to be where they're attaching
all the sampling information to the
the spans and distributed tracing metadata, and then hoping that it can be
resampled or upsampled within collectors based on those, you know. Piece of metadata. But yeah, for
you know, up sampling of metrics. But it. It seems like there's a little bit of a cognitive distance in the fact that nobody's actually maintaining these other older ways of doing like sampling
ostensibly, you know Jaeger, or aws, or whoever supports
So I guess we'll see where this it seems like.
seems like it would be difficult to maintain some of these features in contrib like a Jaeger like I certainly wouldn't volunteer to maintain a Jaeger remote
sampler.
**Kayla Reopelle** 37:40 Yeah, yeah, nor nor would I.
**Hannah Ramadan** 37:43 So.
**Kayla Reopelle** 37:44 But our Ariel had written a really great guide in contributing kind of like
outlining the requirements. If you want to contribute a new gem like what you need to be willing to commit to. And so, if that person is interested, it could be good to pass that Doc over to them.
**Eric Mustin** 38:05 I? Yeah, it's well, I think
I don't think they have any interest. I just felt bad because it sounds like they did have a
sounds like they're using our gem. And you know, they're whatever
they're instrumentated. They're probably paying too much for their traces. That's okay. Anyway.
So yeah.
**Kayla Reopelle** 38:47 yeah, I think
I think I just need to spend a day or 2 getting, reacquainted with the prs,
not a problem thanks for scrolling through this.
Yeah, like, I know, there's a few other discussions that might be good to bring back up. But my brain's not
fully ready for that quite yet related to like errors on resource detection, and
I think a few other things suppressing internal spans. So
it'd be nice to wrap those conversations up.
Yeah, I think unless anyone else has anything, they wanna go over.
**Hannah Ramadan** 39:55 Yep, I got nothing else.
**Eric Mustin** 40:03 I'm good sorry for.
**Kayla Reopelle** 40:05 No.
**Hannah Ramadan** 40:05 Doing 20 min of stand up, but it's good good seeing y'all.
**Kayla Reopelle** 40:09 You, too. Yeah, thanks for coming.
**Eric Mustin** 40:10 Yeah.
**Kayla Reopelle** 40:11 We try to.
**Eric Mustin** 40:11 Try to be here next week, and, you know, actually do the action items. I said, I do.
**Kayla Reopelle** 40:17 Next.
**Eric Mustin** 40:17 Right there.
**Kayla Reopelle** 40:19 Cool.
**Eric Mustin** 40:20 Alright! Take it easy all.
**Kayla Reopelle** 40:21 Bye, see ya.
**Hannah Ramadan** 40:23 Everyone.
**Xuan Cao** 40:23 Fine.
