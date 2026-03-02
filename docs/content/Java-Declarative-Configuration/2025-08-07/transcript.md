SIG: Java Declarative Configuration
Date: 2025-08-07
Duration: 28 minutes
Zoom Recording URL: https://zoom.us/rec/share/w4UARbhDcVOQFgLhTqwhHKutF-plRKnr4Xs4MiNYw2kaYV2tq0cIwkkKzmaHtz70.8rhnPgRsVwqIF3oo
============================================================

## Zoom Recording Transcript

**Robert Niedziela** 01:51 Hello!
**GZ Gregor Zeitlinger** 01:56 Hello!
Let's see how many people we get during summertime.
**Robert Niedziela** 02:09 Yeah.
Is Jack back again? Or still.
**GZ Gregor Zeitlinger** 02:16 It's better.
**Robert Niedziela** 02:17 I haven't heard anything from him.
Trask is also on vacation.
**GZ Gregor Zeitlinger** 02:24 I don't know about Laurie.
**Robert Niedziela** 02:27 He was on vacation, but I'm not sure if it's if he's still out of office.
**GZ Gregor Zeitlinger** 02:39 Portal.
**Robert Niedziela** 02:49 In the meantime I have a question. Maybe you you could help me.
So in my project, our splunk staff, I actually import
one of the deliverables from
Java instrumentation, and it is the testing stuff.
And some time ago you added few providers.
Let me bring this Pr.
It's not better.
**GZ Gregor Zeitlinger** 03:27 Can also share your screen.
**Robert Niedziela** 03:29 Yeah, yeah, I will. I just need to find my the correct stuff.
**GZ Gregor Zeitlinger** 03:33 Right? Okay.
**Robert Niedziela** 03:37 Yeah, okay, I will have to make it smaller.
So you can see anything.
Okay, let me share this.
Yeah. So so in this. Now I have covered it with something else. And yeah.
on this pr, it was added,
stuff like this, content providers. And then they were
they they have some
Oh, gosh! It's maybe it's not this. Let me. I'm sorry for this.
**GZ Gregor Zeitlinger** 04:39 No worries.
**Robert Niedziela** 04:40 10 min, please.
No, it should be there.
Alright. So on this.
**GZ Gregor Zeitlinger** 05:14 You can also.
**Robert Niedziela** 05:14 I looked up this last week, you know. Sorry I forgot about
what I wanted to ask you.
**GZ Gregor Zeitlinger** 05:23 What is the problem that.
**Robert Niedziela** 05:25 Problem was that, this, providers were automatically imported into my tests. And when I when I started a kind of integration test where I called the auto auto automatic configuration
in it that is going to parse the parse.
The config file from the the provided argument right? And there was no
Some class was not loaded that actually, I need to find it. It's just really hard to to explain without it. Give me a minute, please. We don't have anyone else so.
**GZ Gregor Zeitlinger** 06:18 Yeah, sure.
**Robert Niedziela** 06:20 Stop the share for a minute.
Okay, I got it.
Just one more stuff to to find.
Yeah, okay, I will share once again.
Gregory. Yeah. So
that's the part. So so this kind of component providers are added right? And they in the create method they have required not null
and.
**GZ Gregor Zeitlinger** 08:04 Okay.
**Robert Niedziela** 08:04 This log record exporter is initialized in some some static initializer of another class. You probably remember that.
**GZ Gregor Zeitlinger** 08:14 Yeah, I remember that it was difficult to get right on. And I.
**Robert Niedziela** 08:18 Yeah, yeah.
**GZ Gregor Zeitlinger** 08:20 Get it right.
**Robert Niedziela** 08:21 Yeah. And actually, it causes my test, you know, to blow up on null pointer exception here, when parsing the Yaml file
in in Downstream project that.
**GZ Gregor Zeitlinger** 08:34 Right.
**Robert Niedziela** 08:34 Not not loading this static initializer.
It was here. No, I don't remember. It was some of other classes where it was added.
**GZ Gregor Zeitlinger** 08:49 This create method should only get called if you actually have an exporter was named Test.
**Robert Niedziela** 09:02 And it hmm!
**GZ Gregor Zeitlinger** 09:05 Sure.
so at 1st it checks for the name, so it calls getname to see if it is a correct provider, and only.
**Robert Niedziela** 09:15 If it's a.
**GZ Gregor Zeitlinger** 09:15 Direct provider it will call create.
So we have to figure out why you.
**Robert Niedziela** 09:23 Test. Yes. Well, the test provider! Why, it's triggered right.
**GZ Gregor Zeitlinger** 09:28 That where it comes from exactly.
**Robert Niedziela** 09:30 You know.
Okay, I will have to double check. Maybe I have some eye on
Provider somewhere in other tests that interfere with it.
That adds some tests comp the name with with I mean the component we've named. Test that triggers this one to fire.
**GZ Gregor Zeitlinger** 09:50 You can also share your.
**Robert Niedziela** 09:53 That's true.
**GZ Gregor Zeitlinger** 09:53 Project, and we can figure it out.
**Robert Niedziela** 09:56 I'm not sure, Gregory, if I should sorry.
**GZ Gregor Zeitlinger** 10:00 Not open.
**Robert Niedziela** 10:01 No.
**GZ Gregor Zeitlinger** 10:02 Okay, yeah, then, I understand.
Yeah, most most distributions are public. That's what I think. Most distributions are public. Of course, I don't know.
**Robert Niedziela** 10:15 I I will have to ask my product manager first, st if I can share on the public. This may be so.
**GZ Gregor Zeitlinger** 10:22 Yeah.
**Robert Niedziela** 10:22 Yeah, yeah, okay, okay. But that that makes some.
I wonder where this where I could add this test. I really don't remember that. But I will double check it, and maybe I will ask you once again, on, on! DM, on, on, slack! If I will still have issues with it.
**GZ Gregor Zeitlinger** 10:42 Yeah. And if you cannot share it, then maybe me too, spec trace or something.
**Robert Niedziela** 10:47 I would have to, you know, switch my branches. It's not worth it right now. But I have another case where I need fully initialized resource. So
yeah, again, in this downstream project that I'm working on. So
yeah, it it looks like we need properly initialized resource in the root of SDK that is available for listeners. And this this kind of of stuff.
**GZ Gregor Zeitlinger** 11:17 Yeah, I think there's already an issue for that.
**Robert Niedziela** 11:25 Yeah, yeah, actually, I even made some pull request with it.
Okay, Fix, but it's awaiting for approval. Jack is not available. So.
**GZ Gregor Zeitlinger** 11:39 Yeah, got it? Yeah.
**Robert Niedziela** 11:40 Inviting.
**GZ Gregor Zeitlinger** 11:43 And is your point request working.
**Robert Niedziela** 11:47 Is it working?
**GZ Gregor Zeitlinger** 11:48 Yeah.
**Robert Niedziela** 11:49 It. It was just don't like the idea of having this resource in the root of
what the configuration?
SDK, but we need.
We need it somewhere. We need this attributes to be accessible from different places.
**GZ Gregor Zeitlinger** 12:11 Yeah, maybe it's easier to convince them with the use case from the Java agent, because that
that is not like a distribution, because that is like the core.
**Robert Niedziela** 12:25 yeah. So so I have some listener where? Where? I need to extract this attributes and use the use it somewhere else. And you know I I don't have it without this change.
**GZ Gregor Zeitlinger** 12:37 But didn't he also say that
the implementation could be improved like with the return types? And this
I didn't follow it closely, but.
Returning tuple blah. Blah would require updates.
**Robert Niedziela** 12:59 Yeah. So we were talking about different ways how to solve this. But actually
there, there are either the staple which is
not nice, that, Jack said as well, or create one more resource and have 2 instances of resource, or it would require some really serious refactoring, because the interface of factory would have to be changed or something like that. So.
and there is no easy and very nice solution anyway.
No.
**GZ Gregor Zeitlinger** 13:39 Maybe I have another idea. Can I share my screen?
**Robert Niedziela** 13:42 Yeah, sure.
**GZ Gregor Zeitlinger** 13:44 Because I think I have. I had a related problem.
**Robert Niedziela** 13:48 Yeah, yeah, that I saw it in your Pr, so I put my comment on it. That, that you also seems like needing this this
resource.
**GZ Gregor Zeitlinger** 14:01 Where is it?
There are so many prs, so I better show.
**Robert Niedziela** 14:08 Oh yes!
**GZ Gregor Zeitlinger** 14:10 It could be something else.
Declarative conflict. Context. Yeah, this is what I mean.
but it's not in this. Pr.
I think it's here in this one.
Yep, it's it's here.
It's in a different Pr, but it doesn't matter. It's just about the idea.
Because I also have the meter provider that I need to pass around.
and I have a get and set meter provider
When this has been loaded. And I can show you how it's used.
So context, this object is passed around in all the create methods of factory.
And okay.
**Robert Niedziela** 15:40 A meet, up.
**GZ Gregor Zeitlinger** 15:41 Provider is then injected into here. What is it? The lock record processor, and also the span record processor and.
**Robert Niedziela** 15:50 Can you share the screen if you have it, or.
**GZ Gregor Zeitlinger** 15:54 Oh, is it not showing I'm sharing this screen? Maybe it's.
**Robert Niedziela** 15:56 Hold on because I have shared so replayed Current.
maybe I have to stop my sharing.
**GZ Gregor Zeitlinger** 16:05 There's also a button at the top where you can select what you want to view. If what? Which.
**Robert Niedziela** 16:11 Audio, okay.
**GZ Gregor Zeitlinger** 16:17 Okay. I see it now. Thanks.
So here, declarative config as the thing that we can pass
around. And here we get the media provider, and then we pass it to the builder
and on the and before we do that, we call setmeter provider, and that is in a different
class. This is this is basically the entry point,
where we check. If you have a meter provider configured and then
create the meter provider and then store it in the context for later use.
And maybe we can also do that for resource resource
factory is that the right one.
**Robert Niedziela** 17:16 Yes, resource, factory resource builder. And maybe we just need to do that here.
I'm not sure.
Huh!
**GZ Gregor Zeitlinger** 17:39 You can just try out if it works.
**Robert Niedziela** 17:44 Hmm.
oh, okay.
The only thing I'm worried about this context is that context over time tends to be, you know, a big workaround for
issues with passing objects.
**GZ Gregor Zeitlinger** 18:18 Yeah, in general, I agree.
I think we should leave it up to Jack to figure out if that is okay for this case?
So if we
put it here, then later, where would we want to get it out? I think it's here in the
now. Where is it?
This creates the SDK, so it should be. Here
is this one.
**Robert Niedziela** 19:08 This is yes, these are this, this resources that are then passed into the the shared object used by this meter providers and and tracer, provider and logger provider. There are
all put in the, you know, guts of this this classes, but not exposed outside. So you don't have access to it anywhere.
**GZ Gregor Zeitlinger** 19:32 Yeah, I just wanted to find the place where this is called. It's also using. Okay, this is used in many places.
but a lot of them are tests which we can ignore.
it's 1 of those.
It's either this one.
**Robert Niedziela** 20:05 Yeah. So that's the place where I where I applied my fix this get default the one that you showed.
**GZ Gregor Zeitlinger** 20:12 Yeah, this one.
**Robert Niedziela** 20:13 Yes, so I called here. I called here resource factory once again and put the resource created by the factory here. Instead of this, get default.
**GZ Gregor Zeitlinger** 20:25 Okay. So let's see, do we have this context? No, we don't have the context here, because we call
create method.
And we also don't have the context here.
We have the context here. It's 2 levels too deep.
Okay.
so we would have to pass in
the context. This is an internal method, so we could change it.
This one, this one is a public method. Okay, this is more difficult.
so we would have to add an additional argument here.
Maybe that's doable.
**Robert Niedziela** 21:27 Oh!
**GZ Gregor Zeitlinger** 21:28 We can just try it out for.
**Robert Niedziela** 21:30 Yeah, we can.
**GZ Gregor Zeitlinger** 21:31 More fun.
**Robert Niedziela** 21:35 The. The only thing is, I will have to drop off in 10 min, because I have another meeting.
But yeah, let's let's do it in this few minutes we have.
**GZ Gregor Zeitlinger** 21:53 Phone call.
Yeah, 10 min should be good.
**Robert Niedziela** 21:58 -
**GZ Gregor Zeitlinger** 21:59 So and then here we also pass it.
So we can even remove the spi helper then
this is used in reflection, okay, it makes it harder.
Oh, this class is not.
**Robert Niedziela** 23:02 Hi.
**GZ Gregor Zeitlinger** 23:02 Yeah.
**Robert Niedziela** 23:03 Yeah, there, there are lots of this kind of traps here.
**GZ Gregor Zeitlinger** 23:08 It's a minefield.
**Robert Niedziela** 23:09 Yes.
a lot of private classes.
**GZ Gregor Zeitlinger** 23:18 Because this is this is not in the incubating part. Okay, I get it.
I get it.
Oh.
that's why Jack said, it would have to return a time.
**Robert Niedziela** 23:32 Yeah, yeah, yeah.
that's really hard to find some really nice solution here.
And yeah, yeah.
**GZ Gregor Zeitlinger** 23:51 Another idea. I don't know if it's any better.
Is this extended SDK, that at Jack proposed
extended SDK, is to give you access to things that
that are incubating really. So that this is not about incubating
and the idea was to have the config provider be accessible in the extended SDK,
and you could also make the
resource available. But it's not incubating. So actually, you could. If you want to to have the resource, then you could just add it here.
I mean, the resource is stable.
and if we decide it's good to have it in the SDK, you can just add it here as a field.
So yeah, can just scrap the other idea.
**Robert Niedziela** 25:02 Okay, so.
**GZ Gregor Zeitlinger** 25:07 Is that an idea that we should pursue adding resource here.
**Robert Niedziela** 25:20 Could be.
**GZ Gregor Zeitlinger** 25:24 So we would.
Where was this place was here? Yeah, right here.
So here in the builder, we would have a new method.
**Robert Niedziela** 25:39 Hmm.
**GZ Gregor Zeitlinger** 25:41 Set resource. Yeah, would be just set resource. That's it.
Oh.
**Robert Niedziela** 25:53 That's it.
**GZ Gregor Zeitlinger** 25:56 I could just send you the patch of that, because that
that is enough to add this idea to the discussion.
**Robert Niedziela** 26:06 Okay. Okay, go.
**GZ Gregor Zeitlinger** 26:14 Raw.
**Robert Niedziela** 26:16 Rob Rob Sunday or Robert Nigella. Yeah. And then there is
just find Rob Sunday. Maybe you will find it.
Oh, you don't have it.
Hmm, hmm.
**GZ Gregor Zeitlinger** 26:32 Oh, I'm in the wrong select. That's why.
**Robert Niedziela** 26:34 Oh, okay.
**GZ Gregor Zeitlinger** 26:45 One.
**Robert Niedziela** 26:49 Let me check, I think, yeah, we we had some.
**GZ Gregor Zeitlinger** 26:53 Yeah, it's already. Yeah.
no, that is a github link that that's why it doesn't. It.
**Robert Niedziela** 27:19 Let me
**GZ Gregor Zeitlinger** 27:21 Are you in the slack here.
**Robert Niedziela** 27:24 I'm i i think I am.
but I will make I will call you I mean DM.
**GZ Gregor Zeitlinger** 27:37 That's a good idea.
**Robert Niedziela** 27:37 I just send you.
**GZ Gregor Zeitlinger** 27:42 Okay, it does not say Sunday here. Okay, okay, here's the edge.
all right. We made it in time.
**Robert Niedziela** 27:50 Yeah, thank you. Yeah. So I will disconnect and switch to other meeting. And I think we'll be on next one.
**GZ Gregor Zeitlinger** 27:58 Yep.
**Robert Niedziela** 27:59 Hopefully in half an hour, or I will be late a little bit, if current meeting will be longer.
**GZ Gregor Zeitlinger** 28:06 See you.
**Robert Niedziela** 28:06 See you all, bye.
