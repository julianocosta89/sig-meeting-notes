SIG: FAAS WG
Date: 2025-06-18
Duration: 66 minutes
Zoom Recording URL: https://zoom.us/rec/share/HoLBk7grDNRDyblArjasBzw3-msK56WuAdRAvOLDydP02CgmHVK87GJgb9nYCcnc.k2inXpd92XzKR3dx
============================================================

## Zoom Recording Transcript

Tyler Benson 00:02:15 Good morning, everyone.
We're gonna give everyone a couple of minutes before we get started.
Message wrap a message, Cirken. Oh, there he is!
Hey, Sarkin!
Serkan Ozal 00:02:34 Hey? Tyler? Hello, everyone.
Maxime David [AWS] 00:02:39 Hi! Everyone.
David Allen 00:02:47 Hi, everybody my name's David. I'm with Grafana. I'm just joining to
learn about the the working of the Sig and see what's being focused on right now.
I can talk more later if
you're interested in what we got going on, but thanks for having me.
Serkan Ozal 00:03:09 Welcome, David!
Raphael Manke (Dash0) 00:03:18 I can go next. So I'm Raphael I'm engineer at. And also being part of the Aws community and been in software engineer for service architectures for more than 5 years now, and I want to join this. This is my 1st sick meeting.
and I'm doing all the aws integration, specialty serverless ones now for. So I wanted to join the group and see what's going on here. Hi!
Tyler Benson 00:03:44 Welcome.
So I just pasted a link to the the meeting notes. So feel free to add yourself as as an attendee as well as any agenda items you might want to cover.
So the the part up above is the the the template.
So look for the one with the date for today.
David Allen 00:04:32 Gotcha reading comprehension can be challenging. Sorry about that.
Tyler Benson 00:04:37 No worries.
Serkan Ozal 00:04:48 Okay, I think.
And we can start worry will not be able to join. Not sure about the Ivan.
Yeah, I think we are we are. We are good to start
in first.st I want to ask. I mean Raphael and the David better. I mean.
they have any topic to discuss, or I mean any question.
David Allen 00:05:22 Yeah, I don't wanna hijack. So I'll be brief. I'm just here to be a fly on the wall. So I work in developer advocacy at Grafana, and I'm just interested more broadly in serverless environments in hotel we do a lot with all kinds of different serverless functions. Certainly on ramp, on lambda, but on a lot of other serverless runtimes as well. And I'm interested in the architectural issues surrounding.
you know, like, for example, lifecycle runtime hooks that you have to do for lambda in order to make sure that everything gets flushed and reported appropriately. And I'm basically here to
kind of figure out scope of what this Sig cares about and where things are more broadly. That's it.
Raphael Manke (Dash0) 00:06:11 If we have time, I would have some questions about the status about the telemetry Api part of the Lambda function extension, and that is consuming the information from the telemetry. Api. What's the status there? Could we? Would you accept a contribution to that to extend some of the features? And why isn't it part of the default configuration that is advocated for the collector setup.
Serkan Ozal 00:06:40 Yeah, actually, I think there was a there was an issue about the our telemetry. Api, I mean.
actually, the our collector has dependency to the telemetry Api. But the telemetry Api is not available in the I mean local, I mean lambda environments
by the by, the base images provided by the aws, lambda actually, I mean, I have been thinking to to talk about that issue as well.
And then, at the same time, we can also talk about the telemetry Api. I think.
Raphael Manke (Dash0) 00:07:13 All right.
Serkan Ozal 00:07:17 Okay, let me share my screen.
There are a few issues I want to. I mean, discuss. And
first, st let me share my screen.
Yeah.
okay, I think, this is the one Raphael is talking about.
And as far as I know, I mean, yeah, we we already, I mean commented on on the issue. And then, just today, I had checked the issue and then and provided my comment too.
And in summary, the issue is that when the lambda runs with the provided base images by the aws
the, because, since the telemetry Api is not available.
and our collector extension also, I mean, looks for connecting and listening to telemetry. Api. It fails.
And when I check the availability of the telemetry Api provided by the Lambda runtime inter runtime runtime interface emulator. I mean, there's an open issue on that which is not supported as of now. So this means that I mean until that is I mean done our collector will not be able to find, and I mean
up and running telemetry Api
so that is the that is the issue here. But the good point is that our collector extension doesn't have heart dependency to the telemetry Api. But I mean, we are mostly dependent to the extension Api.
Because we need to be aware of the lambda container lifecycle so the
the option I have seen for this issue is that I mean just we can introduce a new configuration, or select to to be able to disable the telemetro api dependency to the collector
extension. So once that configuration is disabled, our collector ex extension will not talk to talk to the telemetry Api, like, for example, if the users are running their lambda functions on their local like the like, by by Aws, Sam, or or or some other tools.
because, as I said the telemetry Api is not provided out of the box by the base images of the Aws lambda
so that might be an option to me, and also want to listen. I mean your your suggestion on that. If you have something different.
Raphael Manke (Dash0) 00:10:14 So I noticed I actually meant a different part of the collector, the telemetry Api receiver. But we can just discuss that later. So for this issue. I'm a little bit reluctant to really say that we config. We make a special configuration for the local State, because it. It also
takes into account the the life cycle of the lambda function. And if those events are not available anymore, I'm not sure if the collector would flush the data correctly in the local setup, because it will be probably still be frozen between invocations
I would rather advocate, for do not mount the extension and send it to a separate collector running on your local machine.
Serkan Ozal 00:11:00 Actually. So you are talking about the extension Api, right? Because I mean.
Raphael Manke (Dash0) 00:11:05 Yes, now we're focusing on this issue. And
Serkan Ozal 00:11:08 Yeah, okay, so, based on this specific issue, I mean, do you or or or anyone have
agreed on? I mean introducing new flag to to disable the telemetry api dependency
for the ones who are running the Lambda function locally.
So before coming to the telemetry Api improvements, I just wanted to to be sync. And on this issue about the about solution.
because the issue here is
about the unavailability of the telemetry Api in the base images provided by the lambda.
Maxime David [AWS] 00:11:51 And second, maybe I can. I can bring that to the team. It's not directly. My, the team I'm working on with response, which is responsible for this. But I have good contact with them. So I always this issue internally to see if we can do something about that. Because, yeah, I've I've heard this
this kind of issue a lot before. So yeah, if we have a strong community push for that, maybe I'll be able to influence that.
Serkan Ozal 00:12:21 Okay?
And in the meantime, should we wait for response from the lambda team? Or should we just introduce, I mean, what do you think new flag to to be able to disable the
telemetry Api dependency on the collector.
Maxime David [AWS] 00:12:38 No, I think we can have the flag meanwhile. Yeah.
Serkan Ozal 00:12:40 Yeah, yeah. Because, as I said, I mean
as far as I see, I mean, I need to double check. But there's a very light dependency
to the telemetry. Api, but I mean more, I mean,
harder dependency to the extension Api, because I mean, you know, especially for for the the couple of processor. We need to. I mean, be aware of the
lifecycle events.
Okay,
any question or feedback on this specific issue, or
we can talk about the the the telemetry Api improvements. I think
Raphael has some ideas and some some opinions on that.
Raphael Manke (Dash0) 00:13:34 No further questions on this issue.
Serkan Ozal 00:13:36 Okay.
can you? I mean, Rafael, can you? I mean, please, elaborate, I mean your I mean your opinions on the on the telemetry Api improvements.
Raphael Manke (Dash0) 00:13:47 So I'm not talking about yeah, yeah, improvements in in general. So I'm I'm asking about the telemetry Api receiver. This is a different receiver that is available only in the open telemetry collector. 1st of all, I'm curious why, it is part of an internal component of the collector, and it's something everyone could reuse as a normal receiver.
And then the second step is we at the 0 see some potential, but would need to make some further adjustments to to the Api, for example, try to add the the span Ids, or something like that for the lock records to correlate locks with the traces. And if these contributions would be appreciated or being yeah, accepted.
Serkan Ozal 00:14:43 Yeah. For the for your second question, yeah, I mean, that will be appreciated. I mean, I think I mean, at least I mean by me for the 1st question.
I really don't know the reason why the the receiver, the telemetry Api receivers an internal module, I mean, I don't know the history of that. That telemetry Api. Maybe Tyler, I mean might provide I mean more information on that. I mean
he has been here I mean longer than me.
Tyler Benson 00:15:17 Well, the that particular thing
came about before I even started participating in the sig.
But what was the question again?
Raphael Manke (Dash0) 00:15:30 So if we could make it somehow
public available. So I can just build it into my own collectors. So if I want to build my own collector. I'm not able to use this receiver at the moment.
Tyler Benson 00:15:45 So I'm not exactly so I'm personally not very familiar with go
library dependency management stuff. So I'd be curious what process would be required to to make that available.
I don't think I'd be opposed to that.
But the other thing to keep in mind is that I don't think we follow as strict of
versioning and
I don't think we follow as strict a versioning process as like the the the upstream collector, Sig does
in terms of breaking changes and such.
Not that there's a lot of active development going on there, but it. I'm just pointing that out, because that's something that we don't necessarily
monitor as as closely.
Raphael Manke (Dash0) 00:16:51 Okay, that's still helpful.
What I get out of it is currently it's like a little bit like a lost child. No one has it on the radar and could be improved if someone takes up the work.
Serkan Ozal 00:17:06 Raphael, maybe I mean also I mean neither me and nor Tyler I mean as the I mean we don't have. I mean much go experiences. Maybe you can post a message to the slack, or maybe create an issue. I mean about your your opinions on the
on that. And then some other folks in the in the fast
community might provide their opinion, and then we can also check I mean ourselves. But I think it might be, I mean better for for getting, I mean
the opinions of others.
Raphael Manke (Dash0) 00:17:38 Makes sense will do.
Tyler Benson 00:17:40 So your desire is to make it so that it's linkable and embeddable in a custom build of the collector.
that you that you create and manage right.
Raphael Manke (Dash0) 00:17:53 It would at least make sense, I think, to have it treated as a regular receiver up in the perfect situation. Maybe even part of the contract, but for the first.st
Tyler Benson 00:18:04 That was gonna be. My next suggestion is maybe the right approach here is actually advocating moving it over to the collector, contribute.
Maxime David [AWS] 00:18:18 Yeah, because I don't know if you were referring to like build flags or something like that. I've looked at go repo for open telemetry, and
I'm not sure that they're a big fan of Go, go build flags because it introduced a lot of complexity in testing as well.
So if the receiver is small enough. Maybe maybe it should be part of the country. Yes.
if that makes sense to you.
Raphael Manke (Dash0) 00:18:46 Okay. So I will open up with the the An issue, with the idea to move the telemetry Api to the contract, and then we can can discuss it. There.
Serkan Ozal 00:18:57 Yeah.
Raphael Manke (Dash0) 00:18:58 Cool.
Tyler Benson 00:19:01 Are there any other components currently in our repo that would make sense to move over.
or just that one.
Raphael Manke (Dash0) 00:19:11 I think that's the only one. I'm not sure the life cycle, but the the lifecycle is.
no, I think that's the only one that makes sense to move out.
Tyler Benson 00:19:28 The.
So one thing I think that you would
one, I think important piece of functionality you would potentially be missing by not using our collector is the the decouple processor
which allows for reporting spans without blocking the response
a submission from the original lambda.
That's true, anyway, I don't know if that's important to you. But something else to look into.
Raphael Manke (Dash0) 00:20:08 Okay, I will think about it. And I will create an issue or start with making contributions to the existing code.
Tyler Benson 00:20:18 Sounds good.
Raphael Manke (Dash0) 00:20:19 Cool.
Serkan Ozal 00:20:25 Okay?
And before I mean passing to the next next issue I think, Max, I mean
you are. I mean, you know, I mean going. I'm better than me and the Tyler. Do you mind? I mean
owning this issue, or or handling this issue?
I mean the extension I mean.
Maxime David [AWS] 00:20:50 Yep, yeah, please assign it to me.
Serkan Ozal 00:20:52 Okay, okay, thank you.
Okay, the, yeah, the another
issue is from the same same user. Yeah, actually, still, I mean, I think we need to. We need to get some feedback from the from the user. But the issue is that according to the report issue, when the lambda function is deployed as the
and docker image with the open telemetry, I mean layers the Nodejs layer and the collector layer. It does not report any. Any depends. And also, as Raphael pointed out, and
I have asked it to, as far as I see from the logs.
There is no, I mean.
open telemetry. SDK, log is presenting there. So
so I think the open telemetry no, Jess layer is not, I mean, activated at all, even to the aws, lambda, exec wrapper and moments where I will it.
said.
Maxime David [AWS] 00:22:05 Yeah, my my understanding is that maybe I'm wrong. But this the open telemetry lambda
repo, does not export to X-ray. It logs to the console. But I'm not sure that we have a piece of code which actually take that telemetry and put X-ray segments via the SDK. So I'm not sure that I think it's a required feature, and but not a bug.
Serkan Ozal 00:22:34 Yeah. And also, I mean, I even not sure that
actually don't think that the open telemetry and Node Js layer is activated here, because
this is the because the user is using the the latest and not just layer version. And then in that version, I expect.
Maxime David [AWS] 00:22:53 I mean.
Serkan Ozal 00:22:54 These these log in any case. Yeah. And and I didn't see that log here because it just.
But it should be there just after the start log. Here.
Maxime David [AWS] 00:23:06 Yeah.
Serkan Ozal 00:23:07 So I believe that somehow it is not activated at all. As far as I know, I'm not. I mean 100% sure. But the aws, lambda, exec wrapper environment variable is supported by the
even by the base docker images. But I am not, I mean fully sure on that. So that might be the issue or might not be, I don't know.
And we, we ask the same same suggestion, similar suggestion to the user by by Rafael by just enabling the debug log. So we can provide more more understanding whether the the SDK is activated or not. And if it's activated.
so what might be the issue. And also I couldn't fully understand whether this issue happens only on local or on Aws, lambda environment or on board. So anyway, I mean, we can. We can wait for for the user feedback. And also the good thing is that user also provided a reproducer, a repo. So that is good, so this should be able to reproduce it by following the steps here.
Actually, I mean, personally, I don't have any experience by running the open telemetry, I mean,
any open telemetry layer with the docker based lambda functions, but
not sure. I mean, anyone has tried that
The next issue is that I was about to ask. I mean, are, I mean everyone good to to merge this Pr. By Max.
and I think he did good job, and then address all the all the feedbacks on the review commands.
and, as far as I know.
me, and worry has approached, and
Ivan has some some some feedbacks. Not sure they are. They are all addressed or not, but we can still ask Ivan whether to approve.
and if I mean he's okay to. I think we are. We are good to to merge this, because I mean, personally, I mean, I'm using the aws cdk for I mean as deployment tool. But I mean, you know.
for the most of the places in the open telemetry organization the terraform is being used so still, I think we we should keep the terraform files con deployments, but it is still good to to have the cdk and deployment to.
Maxime David [AWS] 00:25:40 Yeah.
yeah, I think I've addressed all the feedback, but I don't mind waiting for like the formal approval. But that's fine. I think there is one way, one nit about the Nodejs version in package. I don't think that's a blocker, but yeah, I don't mind waiting for a formal approval.
Serkan Ozal 00:25:59 Okay, I can ping Ivan one more. One more time to check it out. And then
upon that, I mean, I think we can. We can merge.
Maxime David [AWS] 00:26:08 Sounds good.
Serkan Ozal 00:26:12 okay, did another issue about the the python Runtime, you know, I mean, in the Nodejs layer. We had added more instrumentation packages
out of the box, and then, of course, they are not activated by default because of the cold start effect, but still they are. They are in the bundle and they are in the layer. So based on the user configuration, they can be activated. And this user
has also been asking to similar similar things. I'm not sure, even though they are not activated by default for the python. Talking about the python runtime for those additional instrumentation packages, whether they will have called start effect or not. But
I think that's a fair request to to have more broader. I mean many instrumentation packages available out of the box in the layer itself, and then
they can be activated. I mean, upon request.
So yeah, personally, this makes sense to me, but
not sure whether what you are thinking about this.
Tyler Benson 00:27:20 So I I'm
I don't have a strong opinion either way. Personally, I know that you put a lot of effort into minimizing that cold start time and adding these would potentially increase the bundle size. I just don't know how much of an impact that would have.
Serkan Ozal 00:27:38 Yeah, that is the yeah. That is the topic we need to. We need to find out first, st whether I mean, even though they are not activated. If still those packages are there, whether you'll have some effect or not on the call to start.
Maxime David [AWS] 00:27:50 Yeah, so yeah, so the bigger the package is, the longer the call starts will be, it will not show up as in its duration, because this file will not be part of the we won't be loading that file at Runtime, but still we like aws when it starts needs to
download the package size, and this will increase the duration like end-to-end latency. So you won't be able to see that in any duration. But if you do like performance testing with end-to-end, like curling from Api gateway. You will see a bit of a delay. I think we need to do some, maybe small performance testing about how
big the package diff will be if we include those those package. If it's small enough, I think it's super safe if it's adding more than 1 MB, and maybe maybe we should reconsider. That's that's.
Serkan Ozal 00:28:45 Yeah, especially for the for the python runtime. And I mean there might be some some native dependencies for some libraries I'm not sure about. I mean, as you said, that I mean.
I mean, even though there's no big difference in the reported in iteration. Still.
we might we should check the the actual, I mean latency effect. And to end because of the I mean package size increase.
If it is, I mean huge because of the the new library dependencies or not. So, yeah, this is that is something we need to. We need to check.
Raphael Manke (Dash0) 00:29:24 I see the bigger difference between the Nodejs version and the python is that Nodejs could be bundled with es build or webpack, and thereby be minified somehow in Python. I don't know if there is a mini fire or anything, so it would be the full fledged instrumentation code being added to the to the layer.
and if it's getting too much, we need to also consider if the layer gets too big, not only latency, how much space is left for the customer code that is deployed, because in the end the full size of the lambda function can't exceed 250 MB, and if we are contributing with the layer a big portion of it, then customer has less space for their own application code.
Serkan Ozal 00:30:12 Yes, specifically for this issue. I don't think the trading instrumentation will require additional.
I mean, we'll bring additional dependency, but not sure about the Asyncao. But
we need to check it out.
Okay to the next one.
Okay, so this is not very new issue. But I mean from the last, from the last month
the user had asked the disabling, the the lambda experimentation actually at 1st mean it
didn't make sense to me. But after then, I mean, you know.
for the distributed tracing propagation issue we have been talking about like.
for example, when there are, I mean when and lambda function is is invoked with, I mean, multiple Sps messages, and each Sps messages is coming from from different trays.
So this means that there are multiple upstream traces. And then for the lambda invocation depend, which trace Id. We can propagate because there are multiple ones.
So the the general consensus was that I mean, still, I mean, I'm thinking, that is, that is the best options we have, I think.
like, for for the processing of the each Sps message, we can create individual spends
propagating the trace Id from the Processed Sps message
for the Lambda invocation Japan. I think we still
should generate it, because I mean.
some people might might depend on that
lambda invocation span for for some, I mean for some metrics and insights like I mean, how many times that lambda function is, I mean counted, I mean called, or what is the average duration of something like that?
But that C. Pen can be added as the with the link to the Sps processing depends.
I think. I mean that is the best approach. I mean.
we can provide as of now, and
I believe that these will address most of the cases.
But the thing is that as as of now, I mean, actually, this will also require some some changes in the
upstream Javascript report, because aws lambda instrumentation is there. So this means that for for these cases we need to find a mechanism to
to wrap some parts or on the lambda Repository side.
I think this can be done by the lambda instrumentation configuration
but I just couldn't find time to to verify that. And then, once I can provide I mean my opinions step by step, on what can we do? But first, st I just wanted to be sync on
what? What should be the right approach
for for the context propagation in such cases, like
lambda is innoced with the multiple messages from multiple traces like Sqs. It might be the Sns in theory, but, as far as I know, Sns is always
involved with the single message in the lambda in practice. Like, for example, the kinesis
and the and the other lambda events with the batch of with the batch support. So yeah, I think the
this will be the the best approach. I mean creating individual spans for the processing of each
single record message, or whatever we, we say.
and so each individual trace will continue with their processing
in the lambda function itself. But the lambda function itself. But but lambda function cpan itself
will be an individual span, link it to those processing spans.
And
but I want to to to check this idea. I mean one more time with you. I mean with you guys.
Just to be sure that we are on the same page and based on that, I can provide some, some some roadmap, I mean some
as some steps to be able to issue that result.
Tyler Benson 00:34:50 So, as I mentioned, I think, in the issue or on the chat. Maybe I think this is already how Java functions. The way that we were just describing. So it was kind of surprising to me that Javascript doesn't already do that.
But if it doesn't, then I support you know, making that change so that it aligns in the same way.
Serkan Ozal 00:35:19 Yeah, in the Java layer. I mean, we provide, I mean, different base base handler classes, I mean, in the layer itself. So user, I mean user can can extend their handler like for the Sps messages, and the things from that base class, and then overwrite the individual. I mean processing method.
But
is might not be, I mean, easy or restrictive, I mean for the for the Javascript users, because I mean
so that is the that is one of the points I'm thinking about. I mean, what kind of approach we can. We can provide?
For for a method or or contract
of the processing of each, each item for different numbers.
Tyler Benson 00:36:06 1. 1 thing that Java doesn't do that I was suggesting is that
unless we can somehow detect that the the X-ray lambda propagator is being used.
It might make sense to, you know. Just always use that propagator to create a span link.
For the X-ray, for the active, tracing span.
Serkan Ozal 00:36:37 Actually one more point on that. I mean, as far as I know.
Yeah. The Java layer creates, I mean, individual traces for for each item, each message, but also I'm not sure it will produce the the invocation span to link it to the, to the, to those processing spans.
so I think that might not be
working in that way for the for the Java. But, as I said.
we need to check it out.
Raphael Manke (Dash0) 00:37:08 How would you get generate a span for each record in a or for each message in a batch? Because you have no control about how the users, iterating over the messages.
Serkan Ozal 00:37:21 Are you asking for for the Java or the the Nodejs?
Raphael Manke (Dash0) 00:37:25 In general. I'm not sure how Java works in no. Js, definitely the the. You have no control over the iterating of the messages you would have to provide a separate handler repa, or something.
Serkan Ozal 00:37:38 Actually that is the that is the point I'm talking about in the Java, I mean, you know, there are. There are base classes. And then, like, for example, let's say that you have the you you are extending from the handler class, and then in that case there, there's a handle request method, which is for for the whole invocation, but also those handlers override.
I mean that handler methods.
but also in a like, for example, in the for loop for each message they just call another. I mean abstract methods. And then abstract method needs to be implemented by the user.
So user basically instead of the handler method user, just implementing the hand, I mean, like the handle item or handle message method for for each message, and then that since that individual method is wrapped and controlled by the I mean by the whole, I mean by the
whole handler handler method, by the Java layer. It can just start and stop spans for the processing of each message. Because I mean, you know.
to control and to to enforce such behavior to the user over the base classes in Java is easier. But in the node js, I mean in the Javascript especially.
and I mean it doesn't have to be the type secret, and it is, I mean, a little bit complex. It will be so. That is the thing that I need to think think on that.
Raphael Manke (Dash0) 00:39:06 The only suitable way, I would say, for the Nodejs Runtime would be that you can read the incoming event because that's part of the instrumentation that you have access to the the event itself, and then you can manually iterate over all the messages and the message ids, and then extract the the context and add all these links to the outer or the 1st band that is generated for the lambda function invoke.
and then all subsequent
spans are, you can somehow correlate them. But that's part of the user library that is, iterating over the messages.
It could be something like power tools for aws lambda that is then doing the the actual linking for the messages. But I don't see the instrumentation itself providing an iterator over messages.
Serkan Ozal 00:39:59 Yeah, actually for the node, Jeff. I had checked the I had.
sorry guys, I need to. We need to answer the door. I mean, we we can just continue sorry for that.
Be right back. Just give me a minute.
Tyler Benson 00:40:20 I guess, while we wait for him. I just wanted to follow up on my action item from last week regarding signing keys Maxime or Max. I I think I posted about this in the the issue you created. But
I think that so what I discovered is like, for example, in the Java repo, where they also have signing keys that they use. Each sig is kind of responsible for their own keys.
Maxime David [AWS] 00:40:50 Okay.
Tyler Benson 00:40:51 So we wanted to. We could create our own and publish the the signing keys. But I like the option of avoiding the keys altogether by using github's attestation functionality.
So I think you said you were, gonna look into that. But I just wanted to close that the action item.
Maxime David [AWS] 00:41:16 Yeah, yeah, definitely, it was. So yeah, let me. I didn't have time to to have a look at that this week. But yeah, I agree. Like, if we can avoid maintaining rotating the keys that, that definitely is better. So yeah, let me have a look at this, and I'll create a new action item for for next week.
Serkan Ozal 00:41:38 Hey? Sorry, guys, I just came back. Yeah. Actually, I was talking about the I mean.
I mean, what kind of I mean Api or mechanism we can provide by the
open telemetry layer to for the
for having control of the each processing message.
So actually, I mean, I was thinking to like
in the wrapper handler, I mean.
without changing the the event signature. So let's say that we have the Sps event object in the Javascript.
And then let's say that it has. I mean, 10 messages
without changing the the event structure, the event properties.
We can just split the the event into the the individual.
For actually, we can just, I mean, have the multiple instances of the same event with single messages
inside itself. And then by using that single message
events to the lambda handler to the user handler one by one. And then in this way, user handle, we see that the Sps itself is calling. I mean themselves with the single Sqs. Messages, and then they can just
continue processing the Sqs. Messages as single by single, but from the open telemetry wrapper, Js, layer perspective. We are getting all the messages at once, and then we can just, I mean, control on the trace context propagation of each messages.
I think that might be easy approach for the for the users, because
we don't need to provide some some additional handlers or or things to to override.
and then still they will get the same event structure. But they just, I mean, see, when they handlers, we just see. See that as the
single messages Sqs. Events. But, on the other hand, we will manage. I mean to open the Gs. Layer the nodes layer. We'd manage the
this, the processing depends.
I mean itself by creating and ending discipline after each processing step.
Actually, yeah, that is the that is the that is the idea I mean, I have been taking on that. But, as I said, still it needs to
some some refactoring in the in the upstream Javascript Repository.
Raphael Manke (Dash0) 00:44:17 I would not go that way, because, 1st of all, we would recreate the features that power tools for aws lumber already has solved, and they took quite some time into it, because there are a lot of edge cases, because you also have to consider reporting partial batch failures and things like that.
So I, personally would rather have like an auto instrumentation for power tools, for example, and then direct people in, hey? If you wanna have a a processor that is, handling multiple message. Use this library and load the instrumentation.
Yeah.
Serkan Ozal 00:44:55 Actually, in that case, I think. Still, the the batch item, failure should work. Because
from the user handler perspective. Still, the handle will report whether that single
messages will fail or not, and then they can be combined in our handler
while returning to the to the lambda function itself.
So is that the I mean concern you are talking about, or something different.
Raphael Manke (Dash0) 00:45:26 I'm thinking we are reinventing the wheel at that point. And you would also, yeah, that's my main issue in that point. Because if customers expecting to get a full batch and maybe build their their own iterating logic to do things in parallel. Maybe they do some external Api calls or something like that. Then this behavior would change when you load the the instrumentation.
Serkan Ozal 00:45:49 Actually, this will not be the default behavior I'm talking about. This will be activated by a configuration
but if the user wants to wants to process
all the messages at once. And then this means that
in that case that user needs to needs to handle the the context propagation himself. So the default behavior still will be, as is, I mean, like the current approach
but for the for the approach we are talking about about on the context. Verification?
Each messages need to be processed in their own trace context. Scope So
that is the so I think that needs to be
done in this way, because I mean that is the that is the request from the users. But, as I said, this will not be activated by default
users which want to see the trace of the each individual processing. Sps messages link it to the to the upstream traces
they can configure, they can enable the flag, and then, in that case, we will invoke the user handler one by one, but otherwise by the default. We will, we will continue as is.
do you, for for handling both cases, I mean.
user will be able to process the messages, I mean as batch, but still want to want to. I mean, link each individual
processing of sepends to the upstream traces one by one. Do we have any.
I mean opinions on that. To to address this.
Raphael Manke (Dash0) 00:47:43 No.
so from from the idea, I'm totally fine with it, having like one span for London vocation, and then several spans for each message process, and each of these span is then linking back to the actual sender. That's what you're posing right.
Serkan Ozal 00:47:59 Yeah, yeah.
Raphael Manke (Dash0) 00:48:00 That I'm totally fine.
Serkan Ozal 00:48:02 Yeah, as I said, and this will not be the default behavior. Right? So I understand your your concern, because
once we once we change the default behavior. It might have
some effects on the users code, I mean, as you said, they might have some some optimizations to to process the messages, I mean in parallel, maybe, or or something different, and then that might affect their
their functions performance. So, therefore, so that is the reason that why I am thinking of introducing this new behavior activated by a flag, and then you also will document the some possible consequences upon these. These change. So user will be will be aware of that.
Otherwise, I mean, as a 3rd option user is user himself need to handle this context propagation by himself. By, I mean just
creating the creating participants individually, I mean for for each the processing messages. Maybe, if I mean they are processing the messages in parallel or or sequentially
back to the point. Why, I just mentioned about this issue.
Yeah, for such cases, I mean, user, want to handle
those cases by himself without enabling the flank, but still want to see the different traces for the processing of each messages as they are processing the message themselves.
We can allow user to disable the the lambda function. Invocations depend.
And then in that case, user can can produce their own processing spans
instead of the single lambda invocation span.
So that is the reason that why I just bring this this issue into table.
Raphael Manke (Dash0) 00:49:59 So you would allow, disabling the Aws lambda instrumentation.
Serkan Ozal 00:50:04 Actually, instrumentation still needs to be there. But the but it will not produce to spend, because the lambda instrumentation, actually, the wrapper is coming from the upstream repository.
and then it is required for for wrapping the the user handler. So still the instrumentation should be there. But we can just disable the behavior of creating the invocation route. The invocation roots depend there.
Because, I mean, if we want to to control something or extract some trace context or do something. We need to wrap the wrap, the user handler
and the app. The current approach is that
for the raping. I mean
there there are some other approach to for dripping, like changing the handler to to your hand, I mean to our handler, and then in our handler just loading the user handler and then calling by ourselves. So this is the. This is the one approach. But to open telemetry is not following this approach because it has some some some disadvantages instead. They are just intercepting the loading of the user handler during the model initialization.
And then they are patching and wrapping the user handler method at that point. So I think we still should follow the same approach.
But, as I said.
we may not need to create the cpan for the invocation if the user configured to
to, not to do that.
So that's that's my point.
Raphael Manke (Dash0) 00:51:51 Okay, make sense.
Serkan Ozal 00:51:53 Yeah.
okay, actually, there, there was 1 point I mean, actually, I was not planning to to talk in this, in this, in this meeting because we are. We are always very close to
to the end. But you know, I mean.
actually, I mean, I have not been working on the cost sort of optimization for for the for the last I mean 2 or 3 months
I mean, I we had made some some optimization in the Nodejs layer, especially focusing on Nodejs layer, but also I have some some plans to to improve the call. Start
performance on the Java layer 2 especially with the snap start, because, as of now, the snap start. Actually the open telemetry Java layer is not aligned with the with the snap start because of the some. Some issues in the Java agent core itself.
but with the newer version of the Java Runtime, I think it. It is.
Johan, 24, or 25,
not sure. 25. When has released Sga so there will be some improvements required in the Java agent core. So we can. We can use the
snapstart for saving the snapshot of the
Java agent. Open telemetry, Java agent layer, and then resume from from that point in the.
in the invocation itself.
And also I want to start discussing about what we can do for for the
yeah, for the collector optimization. I know that Max has sent some some Pr to the upstream repositories. And he analyzed some some initialization time. Actually, I mean, I had did this similar similar I mean analysis on the on the
I mean initialization time of the core modules from coming from the upstream collector
repository. We can talk about what we can do at that point. But I'm not
sure that I mean, even though we we improved a few cases
still. I'm I'm not fully confident that we'll be able to dramatically reduce the the existing collector overhead.
Because still, you know, because as long as we have dependency to the upstream collector.
Yeah.
Maxime David [AWS] 00:54:38 Yeah, I do agree with that. And, for instance, in my previous company, we did some very intensive
work with go and auto optimize and looking at. Go in it. Modules and stuff like that.
Serkan Ozal 00:54:53 Okay.
Maxime David [AWS] 00:54:53 And at the end we took the drastic decision to migrate that to rust, because.
well, you know, like extremely fast starting time, memory management. It's it's a big move, and I'm not sure we want to do that. But just just to say that, due to the fact that
go as an internal runtime that you cannot shave. If you look at the symbol table, you will see that the 1st biggest symbol is actually the runtime which, under garbage collection, and all of that like, go internal go routines, mechanism, and stuff like that. And this is heavy in memory and cannot be shaved.
Serkan Ozal 00:55:34 Yeah. Yeah. I mean, I know that the I think it was the data. Doc. They, I mean, they have.
Yeah, they have their own I mean rust collector extension. And then
I think I mean, the the rust will be the the best solution for for this issue. But, on the other hand, this means that we need to have a fork of the open telemetry collector in Rust.
Maxime David [AWS] 00:56:02 Yeah, it's it's huge in terms. Yeah.
Serkan Ozal 00:56:06 Yeah, for every component we we need to. I mean, implement ourselves in rust. So that is the that is the main concern of me.
Maxime David [AWS] 00:56:13 Oh, yeah, yeah, definitely, it's yeah. It needs to be like a huge move like, we need contributor. And on the long run. So yeah, it's I'm not sure it's best idea right now.
Serkan Ozal 00:56:23 So. And yeah, also, I mean, I have some another idea. I want to discuss it. My idea is that still
we will keep using the the collector existing collector. But the thing is that in front of the the real collector we might have
a kind of the light wave collector which initially starts.
and then the the manage, the the other one I mean asynchronously.
as I know. I mean, I'm not giving too much details as of now. But the but I want to, I mean, discuss with I mean with you guys to on that idea about
so my main target is that can we still use the existing open telemetry collector without without latency? Because as long as we we start we start the collector.
Still it, I mean, even though we start the collectors during the initialization, even though it is running in parallel, still it will consume the CPU and affect the call. Start. But my idea is that just can we have a kind of light where collector it might be written in go or or rust?
That collector will be, I mean during the call, start that collector will be the the collector in use by the SDK, but also that collector will will, sipping up the real collector after the 1st invocation.
and then for the subsequent invocations, the real collector will be used by the SDK.
Maxime David [AWS] 00:57:52 So what you're describing is moving. The issue of call starts into the actual runtime of the 1st or subsequent invocation. So the the sum of the overhead would be the same, or maybe a bit extra, because there is another binary. But at least for call starts, the impact would be would be less drastic. This is what you mean, right?
Serkan Ozal 00:58:17 Yeah, actually, I am talking about the moving, the the real collector initialization overhead to the post invocation.
Maxime David [AWS] 00:58:27 Yeah.
Serkan Ozal 00:58:28 But for the subsecutive location
that collector, that real collector, will be used. But during the initialization is, the the collector initialization overhead will will not be in the frame location, but in the posting location.
Maxime David [AWS] 00:58:42 Yeah.
Serkan Ozal 00:58:44 Then you yeah, sorry, I see, like your raised end. So please go ahead.
Raphael Manke (Dash0) 00:58:49 Yeah. So
I like the idea of second. And it would be beneficial to also maybe consider what aws itself is considering for this solution. Maybe they offer a proper Otlp endpoint in somewhere future. Then a lot of these collector work would be not needed at the moment.
Serkan Ozal 00:59:12 Yeah, actually, guys, what I am talking about with you is that I mean, as I mentioned before, I'm not the I don't have much calling and the rest experience
so I mean I will. I mean, I was thinking to to ask help from from you, or I mean from you, Max, or or Ralph, or or anyone in the go, or the rest experience in in the community? Because I mean, actually, I have this idea. I mean since the the end of the last year, but I mean, since it will require some some effort for me just to to get more more expertise in going and the rest. And then just I mean
with the idea first, st I mean, I want to talk about some details of the idea. And then, once we are, we are agree on that about from technical point of view. Actually, I was thinking to, I mean
to us coming for for development, I mean, of this idea. But you know, I mean, this is, I think, because I mean, even though we like, for example, we we improved the call start performance of the Javascript player, but still, because of the collector called Start. Still, it feel, I mean
almost I mean 500 ms because of the collector.
All right.
Maxime David [AWS] 01:00:30 What about maybe drafting like a Rvc in text mode in and open as issue? So we can review and comment on this. I don't know how it's usually done.
Serkan Ozal 01:00:42 Yeah, yeah.
Raphael Manke (Dash0) 01:00:44 Thank you.
put in the comments. A project from someone that was running and or writing a rust. Open telemetry collector for Lambdas.
Serkan Ozal 01:00:53 Know. Yeah.
yeah, I mean, if I mean the reusing the existing components from the from the upstream collector repository, I believe that the rust. I mean building the collector, for we trust from scratch will be the best option. I and I don't think there will be any. I mean concern. I mean there will be any I mean concern on that. But you know the reason is that I mean we don't want to maintain another. I mean fork of the collector.
Maxime David [AWS] 01:01:23 Yeah, I would be curious also. And maybe the the official collector written in go in the open territory. Maybe they have some similar thoughts. I don't know. Maybe they're working on on something, and we can get details or timeline about what what they're doing. I don't know.
Serkan Ozal 01:01:43 Okay, thank you guys, I think we we are running out of time. Thanks for your time.
Maxime David [AWS] 01:01:49 Thank you so much. Have a good one.
Raphael Manke (Dash0) 01:01:51 You. Thank you. Everyone. Bye.
