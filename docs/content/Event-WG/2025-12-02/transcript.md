SIG: Event WG
Date: 2025-12-02
Duration: 42 minutes
Zoom Recording URL: https://zoom.us/rec/share/GUYwogjiUHz72-R9TFwQ4kVYpfSv6icjvCrBT7gUwrDMlbIF2r3_TdRCw6gD38Eq.hu_PWuGXcsbT5IQA
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 02:57 Hello, Trask.
**Trask Stalnaker** 03:00 Hey, Lenmilla!
Here we are. Blogsick.
**Liudmila Molkova** 03:07 I'm not sure if Robert is around this week, I haven't seen him in this echo.
**Trask Stalnaker** 03:14 Oh, true.
He did some good triage last week.
Or the log sig.
**Liudmila Molkova** 03:36 Right.
**Trask Stalnaker** 04:04 Hey, we have… Topics, even.
Planning for… Why is new metric value types and limits? Yeah… I'm really… I know on the Java… So I'd really want to make these… The complex attributes table.
We have a GenAI instrumentation right now that wants to use complex attributes, and my… prototype only covered complex attributes on logs, I realized.
And I started working on it for spans, but it kind of spinning, like it's kind of… A lot to make it all work with incubating and kind of the structure we have.
Whereas it'll be really easy to do it stable, and Jack had actually was sort of hoping we didn't even need to do the logs incubating and go straight to stable because of… the… Effort for… Hiding things behind incubation.
**Liudmila Molkova** 05:29 Seeing… okay.
**Trask Stalnaker** 05:30 But we have Jan 15th. Jan 15th is our… Time, but where spec needs to be stable by then.
for us to be able to stabilize it in Java.
**Liudmila Molkova** 05:44 Right, and Robert was going to send a PR to stabilize, but we're blocked on the prototypes, and now it's blocked on me, and I didn't make any progress.
to make the PR mergeable.
**Trask Stalnaker** 05:57 Oh, okay.
Cool. Yeah, I don't think it necessarily has to be mergable, but it does need to have support from main Python maintainers, like…
**Liudmila Molkova** 06:12 It has two approvals from two Python maintainers.
**Trask Stalnaker** 06:16 Okay.
I mean, honestly, that… My understanding of the… Prototyping rules is that that would qualify.
**Liudmila Molkova** 06:29 And… It seems we're qualified, and we can try to… Push for stability.
Should I just mention it here?
**Trask Stalnaker** 06:53 Yeah, yeah.
Oh yeah, I don't think this doesn't mention the Python anywhere.
I moved on to the next one here, discuss… Recommend setting severity number for logs.
What… what I don't know is if this belongs in semantic conventions, since we're short of… Unless we're talking about events.
**Liudmila Molkova** 08:36 I… yeah, I agree with you, and I think… For events, this belongs in semantic conventions, and we… should… we are saying should specify a severity number, but we don't have any tooling support for this. We don't even have a field on events.
And we need to decide how? Because the severity is contextual, right? So if I'm recording a page view event.
It might have error severity if an error has happened, or a warning severity.
So we should probably document this point in the event convention.
**Trask Stalnaker** 09:24 Oh, expand on this.
**Liudmila Molkova** 09:27 Yeah.
**Trask Stalnaker** 09:31 That's fair. Just something like, it may be contextually… And made, forgiven event.
semantic convention that may… Pete.
I wouldn't say contextually aware, but…
**Liudmila Molkova** 09:56 So, maybe we can say that semantic conventions for individual events should specify the recommended severity I don't know, minimum severity level.
And… It can go… Higher?
The default severity level.
**Trask Stalnaker** 10:18 Why… why… why only hire?
**Liudmila Molkova** 10:26 You're right, so even the exception event can have debug severity as we… Learned.
Yeah.
So this is the default, but it can go any direction.
Where they can specify a range, or it doesn't matter. Maybe we can just say that.
**Trask Stalnaker** 10:42 should… should have one.
Oh, I see what you said. It should specify… Yeah, I understand what your complaint about this, is it's sort of suggesting it should specify one severity number.
It's like, events should have a severity number.
**Liudmila Molkova** 11:05 Yeah, so events should have a severity number, and in semantic conventions should specify a default one.
**Trask Stalnaker** 11:21 Okay.
**Liudmila Molkova** 11:23 And we can add a nice… I can add a nice weaver life check.
For events that don't have a severity note.
**Trask Stalnaker** 11:59 This part in spec, maybe… Do… does this capture your… do you agree with this?
**Liudmila Molkova** 13:32 Yeah, thank you.
I'm thinking we cannot make severity number required because it's a stable spec.
We cannot change the default, we… maybe the convenience API, the future Logger Convenience API, would requires version number.
**Trask Stalnaker** 14:01 Yeah.
Whoa, event API? Oh, the loopback. Let's wait… Let's give Jack… Time… Let's sweet.
Alright, and the log sig board… In review…
**Liudmila Molkova** 15:29 Oh, I forgot about this one.
**Trask Stalnaker** 15:53 You wanna both just take 5 minutes and…
**Liudmila Molkova** 15:55 Yeah.
**Trask Stalnaker** 15:57 Look at it.
Did you get through it?
**Liudmila Molkova** 22:11 Yeah… I mean… I like that it clarifies things, I… don't have major concerns. I would love somebody else, not us, to review it, like Bogdan, who created the issue.
**Trask Stalnaker** 22:30 I mean…
**Liudmila Molkova** 22:33 And most of the changes are actually… In the rhythmia and the non-normative.
So they're just… Information.
**Trask Stalnaker** 22:52 Easier to emit logs… yeah, okay, I just have some… I think mainly… And it's about… the log… There's a lot of discussion of logs following semantic conventions.
**Liudmila Molkova** 23:12 Right.
**Trask Stalnaker** 23:13 so I… would… Prefer to, change those to events, but yeah, I will leave… I left open areas that I'll leave some nits on, but… Cool.
Just ergonomic API update… Recording… doc… Where did we leave off here?
**Liudmila Molkova** 24:12 Oh… Yeah.
**Trask Stalnaker** 24:17 Do you feel like this is, the next… the… I know we have the bigger OTAP, Is this… Does this, overlap with the OTAP?
**Liudmila Molkova** 24:38 I think it does.
So, okay, I… I probably need to refresh my, memory on this one.
The thing that I don't like about it… The sore, though, tap.
Is that we… we have this confusion between error and exception.
And… I can understand there is an exception type, and there is an error type, and they are kind of different.
There's an exceptions tag trace.
But the message is when it really sucks.
Alright, so… I… thing… If we get through this one… Let me open it.
**Trask Stalnaker** 25:35 So… I guess, at a high level, my initial question here is just, does this… should this be… does this need to be merged into the OTEP?
**Liudmila Molkova** 25:51 It's… Should it… the outcome of this one, the perfect outcome, depends on the ATAP, so I think we should resurrect data first, and then maybe I can draft this one until we get a clarity on the ATAP.
**Trask Stalnaker** 26:08 Okay.
**Liudmila Molkova** 26:10 Let me do this… Oh, you're reviewing the issues.
**Trask Stalnaker** 27:59 I pulled up a couple that looked… Interesting.
Or it looked like we could maybe say something about… It looked easy.
Surrounding number beyond 24…
**Liudmila Molkova** 28:18 Why shouldn't it?
**Trask Stalnaker** 28:26 I mean, it's definitely legal at the proto-layer.
I guess some languages… I mean, maybe it's just a language bilingual, like, there's nothing wrong with it?
I don't think we have to tell languages… Maybe not to allow it?
**Liudmila Molkova** 28:52 Some don't allow it, for sure.
**Trask Stalnaker** 28:55 Yeah.
Had one more log level from 2019.
Okay, how did this get pulled in?
It's also undefined how to treat zero.
I thought we defined that.
**Liudmila Molkova** 30:02 Yes.
Oh, I think it should be closed.
Oh, how consumers should treat it.
What is it? 4540.
I'll just close it.
**Trask Stalnaker** 30:41 Yeah, I think so.
**Liudmila Molkova** 30:42 listed.
**Trask Stalnaker** 30:43 Yeah.
I'm going to add needs… Info…
**Liudmila Molkova** 32:23 And I kinda opened to… Request languages to allow arbitrary Numbers, but if there is some justification for it.
Okay, don't.
**Trask Stalnaker** 32:39 If we can reserve.
**Liudmila Molkova** 32:40 district.
**Trask Stalnaker** 32:41 Some have already done enums.
**Liudmila Molkova** 32:46 And they can't relax them, I would imagine.
**Trask Stalnaker** 32:52 I mean, for Java… not… very easily, I don't think.
I mean, not without changing the API.
To allow arbitrary… Let's see… My record builder… So, severity… I mean, certainly we could add an overload.
To pass an arbitrary int.
**Liudmila Molkova** 33:26 But then there is a constructor. It's not public, of course, but… There, there could be… hmm.
**Trask Stalnaker** 33:31 It's an enum.
**Liudmila Molkova** 33:33 And you can add a function to, you know.
from… from… Scenarity.
**Trask Stalnaker** 33:42 But we can't construct, and we can't instantiate a new enum.
We would have to list… statically list, all possible.
ints here.
**Liudmila Molkova** 33:58 Assuming you can… it probably doesn't matter, but if you can construct a severity, it doesn't have to be listed as a static.
**Trask Stalnaker** 34:07 that.
**Liudmila Molkova** 34:08 Cheers.
**Trask Stalnaker** 34:08 You, you, you aren't allowed to, enums… You aren't allowed to… Called the constructor arbitrarily.
In Java.
**Liudmila Molkova** 34:23 So we… we… oh, I see, we never used the names in Azure SDKs because of this.
**Trask Stalnaker** 34:29 They're not open. They're not open. Yeah. They are closed.
**Liudmila Molkova** 34:33 Yeah.
But yeah, it can still be done by accepting some, the int on the… Yeah.
But it's a lot of work for you to expand, that's why I would love to understand, like, the reason behind it, right? If there is a very good reason, we would… You would do the work, yeah.
**Trask Stalnaker** 34:56 Yeah, I think it's more just… compliance question.
It's more like spec language question, like, people want to know what it is so they can make sure that they conform As opposed to, like, a real user use case.
**Liudmila Molkova** 35:15 Yeah.
Okay, cool, yeah.
Makes sense.
**Trask Stalnaker** 35:24 This one… So we have a Java PR… So, I guess the question here was this, where there was some discussion about whether it should be arguments.
Or argument, or parameter.
Nothing too… Nothing probably too interesting.
I think arguments is… kind of makes sense to me for… Capturing an array, the array of arguments there.
**Liudmila Molkova** 36:18 Yeah, but having two different…
**Trask Stalnaker** 36:20 Names.
**Liudmila Molkova** 36:21 Names… Oh.
So you would… oh, wait, so log record arguments… Would be a single attribute.
Or would it be at.
**Trask Stalnaker** 36:32 Yeah.
**Liudmila Molkova** 36:33 A single attribute, I see. Okay.
And then parameters would be a template.
**Trask Stalnaker** 36:40 Well, we wouldn't have… I don't know if me… like, I haven't… scene… Name templates outside of… net…
**Liudmila Molkova** 36:58 I mean, I would imagine Python could have them, but yeah, I don't know.
Good question.
**Trask Stalnaker** 37:07 And so, I guess the question is, do we want both, or… For query parameters, we kind of said just we leaned into… they're generally named, and if they're not named, you can do .0.1.2, I think.
**Liudmila Molkova** 37:27 So remember what we have for the language we used for complex attributes. So whenever you can flatten down, you should flatten down.
And use primitives.
Whenever possible.
So in this sense, templates are… Always more preferable.
**Trask Stalnaker** 37:52 I see, Even if it's just to do .0.1.2.
**Liudmila Molkova** 38:09 Yeah, so indexes are not helpful.
**Trask Stalnaker** 38:13 Yeah…
**Liudmila Molkova** 38:15 Yeah, so for arguments, yeah, I think I agree with you. For the named ones, it probably should be a template. And then it kind of justifies having two different attributes.
Because they have different types.
**Trask Stalnaker** 38:32 True, yeah, Named… would you have… I mean, because you… we can have both like this.
**Liudmila Molkova** 38:56 -Oh.
**Trask Stalnaker** 38:57 We can have named arguments.
Like, are they named parameters?
In our named arguments.
I mean, they're both this one, obviously, but…
**Liudmila Molkova** 39:10 For… for Java, there is no named per… wait, the, the queue, the… SLF4J has structured login with named parameters.
**Trask Stalnaker** 39:24 Named in the template.
**Liudmila Molkova** 39:26 named… not in the template.
**Trask Stalnaker** 39:30 That's true.
**Liudmila Molkova** 39:30 Yeah.
**Trask Stalnaker** 39:32 But that'll just be captured as structured args.
**Liudmila Molkova** 39:37 Oh, I see.
They are… Attributes on its own.
They don't need a prefix. Okay, yeah.
So, it sounds like for the… At least right now, all you care about are the… Argument. List.
I mean, we don't need to boil the ocean and decide on parameters versus arguments right now. You're not blocked on this discussion.
**Trask Stalnaker** 40:09 No, I guess the, the… do we… want… yeah, and so I think we'll introduce… for Java, at least, we just probably want an array.
And we can leave the named… The named parameters, arguments, till later.
Trying to see if I can find answer to if they're… If there's… Kinda named arguments to templates.
Does look like Python.
Has… named… Placeholders… Okay, cool. No, I just thought that one was… that one was just relevant, because we've… It's come up… In Java… Alright, shall we call it?
**Liudmila Molkova** 42:03 Yeah, let's call it. So my next steps, if I have time, I will work on that tab.
**Trask Stalnaker** 42:13 Cool. Yeah, I think, I'd be interested in getting back Into that, slowly.
Paging it, start paging it back for it to… fall out over the holidays. Maybe, maybe start in… January.
**Liudmila Molkova** 42:37 Yeah.
**Trask Stalnaker** 42:38 So I got 2 weeks. Whatever, whatever works for you. I'm… I'm good. I will follow your pace.
**Liudmila Molkova** 42:45 I'll try my best, yeah.
Cool, then thank you. Have a great.
**Trask Stalnaker** 42:50 See ya.
**Liudmila Molkova** 42:50 of your day. See you later. You too.
